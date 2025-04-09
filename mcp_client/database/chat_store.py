"""
Database-backed storage for chat sessions.
"""
from typing import Dict, List, Optional, Union, Any
from uuid import UUID, uuid4
from datetime import datetime
import logging
import json

from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc

from mcp_client.database.base import get_db_session
from mcp_client.database import models
from mcp_client.api.models import (
    ChatSession as ChatSessionSchema,
    Message as MessageSchema,
    MessageRole,
    TextContent,
    MessageContentType,
    CreateSessionRequest,
    ChatSessionSummary,
    MessageContent as MessageContentSchema,
)
from mcp_client.llm.base import Message as LLMMessage, provider_registry


logger = logging.getLogger(__name__)


class DatabaseChatStore:
    """Database-backed store for chat sessions."""
    
    def __init__(self, db_session: Session):
        """Initialize the store with a database session."""
        self.db = db_session
    
    def create_session(self, request: CreateSessionRequest) -> ChatSessionSchema:
        """Create a new chat session."""
        # Get the provider name from the model if available
        provider_name = None
        if request.model:
            if any(request.model.startswith(prefix) for prefix in ["claude", "anthropic"]):
                provider_name = "anthropic"
                logger.info(f"Session created with Anthropic provider for model {request.model}")
            elif any(request.model.startswith(prefix) for prefix in ["gpt", "text-", "openai"]):
                provider_name = "openai"
                logger.info(f"Session created with OpenAI provider for model {request.model}")
            else:
                logger.info(f"Session created with default provider for model {request.model}")
        
        # Create database model with string UUID (not UUID object)
        session_id = str(uuid4())
        new_session = models.ChatSession(
            id=session_id,
            title=request.title,
            model=request.model,
            provider_name=provider_name,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        
        # Add to database
        self.db.add(new_session)
        self.db.commit()
        self.db.refresh(new_session)
        
        # Add system message if provided
        if request.system_prompt:
            system_message = models.Message(
                id=str(uuid4()),
                session_id=new_session.id,
                role=MessageRole.SYSTEM.value,
                simple_content=request.system_prompt,
                created_at=datetime.now(),
            )
            self.db.add(system_message)
            self.db.commit()
        
        # Convert to schema and return
        return self._db_session_to_schema(new_session)
    
    def get_session(self, session_id: UUID) -> ChatSessionSchema:
        """Get a chat session by ID."""
        # Convert UUID to string for database query
        session_id_str = str(session_id)
        # Query the database
        db_session = self.db.query(models.ChatSession).filter(models.ChatSession.id == session_id_str).first()
        
        # Check if session exists
        if not db_session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Chat session not found: {session_id}",
            )
        
        # Convert to schema and return
        return self._db_session_to_schema(db_session)
    
    def get_all_sessions(self) -> List[ChatSessionSummary]:
        """Get all chat sessions."""
        # Query the database
        db_sessions = self.db.query(models.ChatSession).order_by(desc(models.ChatSession.updated_at)).all()
        
        # Convert to schema and return
        return [
            ChatSessionSummary(
                id=session.id,
                title=session.title,
                message_count=len(session.messages),
                created_at=session.created_at,
                updated_at=session.updated_at,
                model=session.model,
            )
            for session in db_sessions
        ]
    
    def add_message(self, session_id: UUID, message: MessageSchema) -> MessageSchema:
        """Add a message to a chat session."""
        # Get the session - convert UUID to string for database query
        session_id_str = str(session_id)
        db_session = self.db.query(models.ChatSession).filter(models.ChatSession.id == session_id_str).first()
        
        # Check if session exists
        if not db_session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Chat session not found: {session_id}",
            )
        
        # Create the database message
        db_message = self._schema_message_to_db(message, session_id_str)
        
        # Add to database
        self.db.add(db_message)
        self.db.commit()
        self.db.refresh(db_message)
        
        # Update session timestamp
        db_session.updated_at = datetime.now()
        self.db.commit()
        
        # Convert back to schema and return
        return self._db_message_to_schema(db_message)
    
    def get_messages(self, session_id: UUID) -> List[MessageSchema]:
        """Get all messages for a chat session."""
        # Convert UUID to string for database query
        session_id_str = str(session_id)
        # Get the session to check if it exists
        db_session = self.db.query(models.ChatSession).filter(models.ChatSession.id == session_id_str).first()
        
        # Check if session exists
        if not db_session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Chat session not found: {session_id}",
            )
        
        # Get messages
        db_messages = self.db.query(models.Message).filter(
            models.Message.session_id == session_id_str
        ).order_by(models.Message.created_at).all()
        
        # Convert to schema and return
        return [self._db_message_to_schema(message) for message in db_messages]
    
    async def process_user_message(self, session_id: UUID, content: str) -> MessageSchema:
        """Process a user message and generate an assistant response."""
        # Get the session
        session = self.get_session(session_id)
        
        # Create and add user message
        user_message = MessageSchema(
            role=MessageRole.USER,
            content=TextContent(
                type=MessageContentType.TEXT,
                text=content
            ),
            created_at=datetime.now(),
        )
        self.add_message(session_id, user_message)
        
        # Get all messages for the session
        messages = self.get_messages(session_id)
        
        # Convert messages to LLM format
        llm_messages = self._convert_to_llm_messages(messages)
        
        # Get the specified model or default
        model = session.model
        
        # Use the stored provider_name if available, otherwise determine from model
        provider_name = session.provider_name
        if not provider_name and model:
            # Only set provider_name if it's not already set in the session
            if any(model.startswith(prefix) for prefix in ["claude", "anthropic"]):
                provider_name = "anthropic"
                self._update_session_provider(session_id, provider_name)
                logger.info(f"Using Anthropic provider for model {model}")
            elif any(model.startswith(prefix) for prefix in ["gpt", "text-", "openai"]):
                provider_name = "openai"
                self._update_session_provider(session_id, provider_name)
                logger.info(f"Using OpenAI provider for model {model}")
            else:
                logger.info(f"No specific provider for model {model}, using default")
        elif provider_name:
            logger.info(f"Using stored provider: {provider_name}")
        else:
            logger.info("No model or provider specified, using default provider")
        
        try:
            # Log available providers
            available_providers = provider_registry.get_available_providers()
            logger.info(f"Available providers: {available_providers}")
            logger.info(f"Default provider: {provider_registry.default_provider}")
            
            # Get appropriate provider
            provider = provider_registry.get_provider(provider_name)
            logger.info(f"Selected provider: {provider.__class__.__name__}")
            
            # Generate response
            try:
                response_text = await provider.generate(
                    messages=llm_messages,
                    model=model,
                )
            except ValueError as ve:
                logger.error(f"Error with provider {provider.__class__.__name__}: {str(ve)}")
                # If the provider fails due to missing API key, try to fall back to mock
                if "API key" in str(ve):
                    logger.warning(f"Falling back to mock provider due to API key error")
                    # Only fall back if the original provider wasn't already mock
                    if provider.__class__.__name__ != "MockProvider":
                        from mcp_client.llm.mock import register_provider as register_mock
                        register_mock(default=True)
                        provider = provider_registry.get_provider("mock")
                        logger.info(f"Using fallback provider: {provider.__class__.__name__}")
                        response_text = await provider.generate(
                            messages=llm_messages,
                            model=model,
                        )
                    else:
                        raise
                else:
                    raise
            
            # Create and add assistant message
            assistant_message = MessageSchema(
                role=MessageRole.ASSISTANT,
                content=TextContent(
                    type=MessageContentType.TEXT,
                    text=response_text
                ),
                created_at=datetime.now(),
            )
            return self.add_message(session_id, assistant_message)
            
        except Exception as e:
            # Create error message
            error_message = MessageSchema(
                role=MessageRole.ASSISTANT,
                content=TextContent(
                    type=MessageContentType.TEXT,
                    text=f"Error generating response: {str(e)}"
                ),
                created_at=datetime.now(),
            )
            return self.add_message(session_id, error_message)
    
    async def stream_user_message(self, session_id: UUID, content: str):
        """Process a user message and stream the assistant response."""
        # Convert UUID to string for database query
        session_id_str = str(session_id)
        
        # Get the session
        session = self.get_session(session_id)
        
        # Check if the last message is already this user message
        # to avoid duplicates when using both POST and SSE
        messages = self.get_messages(session_id)
        user_message_exists = False
        if messages and len(messages) >= 1:
            last_message = messages[-1]
            if last_message.role == MessageRole.USER:
                if (isinstance(last_message.content, TextContent) and 
                    last_message.content.text == content):
                    user_message_exists = True
        
        # Add user message if it doesn't exist
        if not user_message_exists:
            user_message = MessageSchema(
                role=MessageRole.USER,
                content=TextContent(
                    type=MessageContentType.TEXT,
                    text=content
                ),
                created_at=datetime.now(),
            )
            self.add_message(session_id, user_message)
            # Refresh messages
            messages = self.get_messages(session_id)
        
        # Convert messages to LLM format
        llm_messages = self._convert_to_llm_messages(messages)
        
        # Get the specified model or default
        model = session.model
        
        # Use the stored provider_name if available, otherwise determine from model
        provider_name = session.provider_name
        if not provider_name and model:
            # Only set provider_name if it's not already set in the session
            if any(model.startswith(prefix) for prefix in ["claude", "anthropic"]):
                provider_name = "anthropic"
                self._update_session_provider(session_id, provider_name)
                logger.info(f"Stream: Using Anthropic provider for model {model}")
            elif any(model.startswith(prefix) for prefix in ["gpt", "text-", "openai"]):
                provider_name = "openai"
                self._update_session_provider(session_id, provider_name)
                logger.info(f"Stream: Using OpenAI provider for model {model}")
            else:
                logger.info(f"Stream: No specific provider for model {model}, using default")
        elif provider_name:
            logger.info(f"Stream: Using stored provider: {provider_name}")
        else:
            logger.info("Stream: No model or provider specified, using default provider")
        
        # Initialize assistant message
        assistant_message = MessageSchema(
            role=MessageRole.ASSISTANT,
            content=TextContent(
                type=MessageContentType.TEXT,
                text=""
            ),
            created_at=datetime.now(),
        )
        # Add initial empty message
        db_message = self._schema_message_to_db(assistant_message, session_id_str)
        self.db.add(db_message)
        self.db.commit()
        self.db.refresh(db_message)
        
        try:
            # Log available providers (for stream)
            available_providers = provider_registry.get_available_providers()
            logger.info(f"Stream: Available providers: {available_providers}")
            logger.info(f"Stream: Default provider: {provider_registry.default_provider}")
            
            # Get appropriate provider
            provider = provider_registry.get_provider(provider_name)
            logger.info(f"Stream: Selected provider: {provider.__class__.__name__}")
            
            # Get streaming response
            full_text = ""
            
            try:
                # Try with the selected provider
                async for text_chunk in provider.generate_stream(
                    messages=llm_messages,
                    model=model,
                ):
                    full_text += text_chunk
                    
                    # Update the message in the database
                    # For performance, we'll batch these updates to avoid too many DB hits
                    # Yield the chunk first, then update the DB occasionally
                    yield text_chunk
                    
                    # Update in database periodically (every few chunks)
                    if len(text_chunk) > 50:  # Arbitrary threshold, adjust as needed
                        # Use the message ID directly (it's already a string in the database)
                        self._update_message_content(db_message.id, full_text)
                    
            except ValueError as ve:
                logger.error(f"Stream: Error with provider {provider.__class__.__name__}: {str(ve)}")
                # If the provider fails due to missing API key, try to fall back to mock
                if "API key" in str(ve):
                    logger.warning(f"Stream: Falling back to mock provider due to API key error")
                    error_msg = f"Unable to use {provider.__class__.__name__} (API key missing), falling back to mock provider.\n\n"
                    yield error_msg
                    full_text += error_msg
                    
                    # Only fall back if the original provider wasn't already mock
                    if provider.__class__.__name__ != "MockProvider":
                        from mcp_client.llm.mock import register_provider as register_mock
                        register_mock(default=True)
                        provider = provider_registry.get_provider("mock")
                        logger.info(f"Stream: Using fallback provider: {provider.__class__.__name__}")
                        
                        # Update session to use mock provider
                        self._update_session_provider(session_id, "mock")
                        
                        async for text_chunk in provider.generate_stream(
                            messages=llm_messages,
                            model=model,
                        ):
                            full_text += text_chunk
                            yield text_chunk
                            
                            # Update in database periodically
                            if len(text_chunk) > 50:
                                self._update_message_content(db_message.id, full_text)
                    else:
                        # Re-raise the error if we can't use the fallback
                        raise
                else:
                    # Re-raise other errors
                    raise
            
            # Final update to ensure everything is saved
            self._update_message_content(db_message.id, full_text)
            
            # Update session timestamp - use the string version of the UUID
            db_session = self.db.query(models.ChatSession).filter(models.ChatSession.id == session_id_str).first()
            db_session.updated_at = datetime.now()
            self.db.commit()
            
        except Exception as e:
            # Create error message
            error_text = f"Error generating response: {str(e)}"
            
            # Update the message in the database
            self._update_message_content(db_message.id, error_text)
            
            # Update session timestamp - use the string version of the UUID
            db_session = self.db.query(models.ChatSession).filter(models.ChatSession.id == session_id_str).first()
            db_session.updated_at = datetime.now()
            self.db.commit()
            
            # Yield the error
            yield error_text
    
    def _update_message_content(self, message_id: UUID, content: str) -> None:
        """Update message content in the database."""
        message_id_str = str(message_id)
        db_message = self.db.query(models.Message).filter(models.Message.id == message_id_str).first()
        if db_message:
            db_message.simple_content = content
            self.db.commit()
    
    def _update_session_provider(self, session_id: UUID, provider_name: str) -> None:
        """Update session provider in the database."""
        session_id_str = str(session_id)
        db_session = self.db.query(models.ChatSession).filter(models.ChatSession.id == session_id_str).first()
        if db_session:
            db_session.provider_name = provider_name
            self.db.commit()
    
    def _convert_to_llm_messages(self, messages: List[MessageSchema]) -> List[LLMMessage]:
        """Convert API messages to LLM messages."""
        llm_messages = []
        
        for message in messages:
            content = message.content
            
            # Handle different content types
            if isinstance(content, TextContent):
                text = content.text
            elif isinstance(content, str):
                text = content
            elif isinstance(content, list):
                # For now, just concatenate text content
                text = " ".join([
                    item.text if isinstance(item, TextContent) else str(item)
                    for item in content
                    if hasattr(item, 'text') or isinstance(item, str)
                ])
            else:
                # Default to string representation
                text = str(content)
            
            llm_messages.append(
                LLMMessage(
                    role=message.role,
                    content=text
                )
            )
        
        return llm_messages
    
    def _schema_message_to_db(self, message: MessageSchema, session_id: str) -> models.Message:
        """Convert MessageSchema to database Message model."""
        content = message.content
        simple_content = None
        
        # Handle different types of content
        if isinstance(content, TextContent):
            # For simple text content, save directly
            simple_content = content.text
        elif isinstance(content, str):
            # For string content
            simple_content = content
        
        # Create the database message with string UUID (not UUID object)
        message_id = str(message.id)
        db_message = models.Message(
            id=message_id,
            session_id=session_id,
            role=message.role.value,
            simple_content=simple_content,
            created_at=message.created_at,
        )
        
        # For complex content, store in the content_items
        if isinstance(content, list) or (isinstance(content, dict) and not simple_content):
            # We'll add content items after the message is saved
            # This is handled by relationships
            pass
        
        return db_message
    
    def _db_message_to_schema(self, db_message: models.Message) -> MessageSchema:
        """Convert database Message model to MessageSchema."""
        # For simple content, convert to TextContent
        if db_message.simple_content:
            content = TextContent(
                type=MessageContentType.TEXT,
                text=db_message.simple_content
            )
        elif db_message.content_items:
            # For complex content, convert content_items to MessageContent
            # This is a placeholder for more complex conversion
            content = [self._db_content_to_schema(c) for c in db_message.content_items]
        else:
            # Fallback to empty text
            content = TextContent(type=MessageContentType.TEXT, text="")
        
        # Convert string ID to UUID
        return MessageSchema(
            id=UUID(db_message.id),
            role=MessageRole(db_message.role),
            content=content,
            created_at=db_message.created_at,
        )
    
    def _db_content_to_schema(self, db_content: models.MessageContent) -> MessageContentSchema:
        """Convert database MessageContent to MessageContentSchema."""
        # This is a placeholder for more complex conversion
        content_type = db_content.type
        content_data = db_content.content
        
        if content_type == MessageContentType.TEXT.value:
            return TextContent(type=MessageContentType.TEXT, text=content_data.get("text", ""))
        
        # For other types, we'd need more implementation based on the actual types
        return TextContent(type=MessageContentType.TEXT, text=str(content_data))
    
    def _db_session_to_schema(self, db_session: models.ChatSession) -> ChatSessionSchema:
        """Convert database ChatSession to ChatSessionSchema."""
        # Get messages for this session
        db_messages = db_session.messages
        
        # Convert to schema, converting string ID to UUID
        return ChatSessionSchema(
            id=UUID(db_session.id),
            title=db_session.title,
            model=db_session.model,
            provider_name=db_session.provider_name,
            messages=[self._db_message_to_schema(msg) for msg in db_messages],
            created_at=db_session.created_at,
            updated_at=db_session.updated_at,
        )


# Dependency to get a chat store
def get_chat_store(db: Session = Depends(get_db_session)) -> DatabaseChatStore:
    """Get a chat store instance."""
    return DatabaseChatStore(db_session=db)