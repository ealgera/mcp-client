"""
In-memory storage for chat sessions.
"""
from typing import Dict, List, Optional
from uuid import UUID, uuid4
from datetime import datetime
import logging

from fastapi import HTTPException, status

from mcp_client.api.models import (
    ChatSession, Message, MessageRole, TextContent,
    CreateSessionRequest, MessageContentType
)
from mcp_client.llm.base import Message as LLMMessage, provider_registry


logger = logging.getLogger(__name__)


class ChatStore:
    """In-memory store for chat sessions."""
    
    def __init__(self):
        """Initialize the store."""
        self.sessions: Dict[UUID, ChatSession] = {}
    
    def create_session(self, request: CreateSessionRequest) -> ChatSession:
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
        
        session = ChatSession(
            id=uuid4(),
            title=request.title,
            model=request.model,
            provider_name=provider_name,
            messages=[],
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        
        # Add system message if provided
        if request.system_prompt:
            system_message = Message(
                role=MessageRole.SYSTEM,
                content=TextContent(
                    type=MessageContentType.TEXT,
                    text=request.system_prompt
                ),
                created_at=datetime.now(),
            )
            session.messages.append(system_message)
        
        self.sessions[session.id] = session
        return session
    
    def get_session(self, session_id: UUID) -> ChatSession:
        """Get a chat session by ID."""
        if session_id not in self.sessions:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Chat session not found: {session_id}",
            )
        
        return self.sessions[session_id]
    
    def get_all_sessions(self) -> List[ChatSession]:
        """Get all chat sessions."""
        return list(self.sessions.values())
    
    def add_message(self, session_id: UUID, message: Message) -> Message:
        """Add a message to a chat session."""
        session = self.get_session(session_id)
        session.messages.append(message)
        session.updated_at = datetime.now()
        return message
    
    def get_messages(self, session_id: UUID) -> List[Message]:
        """Get all messages for a chat session."""
        session = self.get_session(session_id)
        return session.messages
    
    async def process_user_message(self, session_id: UUID, content: str) -> Message:
        """Process a user message and generate an assistant response."""
        session = self.get_session(session_id)
        
        # Create and add user message
        user_message = Message(
            role=MessageRole.USER,
            content=TextContent(
                type=MessageContentType.TEXT,
                text=content
            ),
            created_at=datetime.now(),
        )
        session.messages.append(user_message)
        
        # Convert messages to LLM format
        llm_messages = self._convert_to_llm_messages(session.messages)
        
        # Get the specified model or default
        model = session.model
        
        # Use the stored provider_name if available, otherwise determine from model
        provider_name = session.provider_name
        if not provider_name and model:
            # Only set provider_name if it's not already set in the session
            if any(model.startswith(prefix) for prefix in ["claude", "anthropic"]):
                provider_name = "anthropic"
                session.provider_name = provider_name
                logger.info(f"Using Anthropic provider for model {model}")
            elif any(model.startswith(prefix) for prefix in ["gpt", "text-", "openai"]):
                provider_name = "openai"
                session.provider_name = provider_name
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
            assistant_message = Message(
                role=MessageRole.ASSISTANT,
                content=TextContent(
                    type=MessageContentType.TEXT,
                    text=response_text
                ),
                created_at=datetime.now(),
            )
            session.messages.append(assistant_message)
            session.updated_at = datetime.now()
            
            return assistant_message
            
        except Exception as e:
            # Create error message
            error_message = Message(
                role=MessageRole.ASSISTANT,
                content=TextContent(
                    type=MessageContentType.TEXT,
                    text=f"Error generating response: {str(e)}"
                ),
                created_at=datetime.now(),
            )
            session.messages.append(error_message)
            session.updated_at = datetime.now()
            
            return error_message
    
    async def stream_user_message(self, session_id: UUID, content: str):
        """Process a user message and stream the assistant response."""
        session = self.get_session(session_id)
        
        # Check if the last message is already this user message
        # to avoid duplicates when using both POST and SSE
        user_message_exists = False
        if session.messages and len(session.messages) >= 1:
            last_message = session.messages[-1]
            if last_message.role == MessageRole.USER:
                if (isinstance(last_message.content, TextContent) and 
                    last_message.content.text == content):
                    user_message_exists = True
        
        # Add user message if it doesn't exist
        if not user_message_exists:
            user_message = Message(
                role=MessageRole.USER,
                content=TextContent(
                    type=MessageContentType.TEXT,
                    text=content
                ),
                created_at=datetime.now(),
            )
            session.messages.append(user_message)
        
        # Convert messages to LLM format
        llm_messages = self._convert_to_llm_messages(session.messages)
        
        # Get the specified model or default
        model = session.model
        
        # Use the stored provider_name if available, otherwise determine from model
        provider_name = session.provider_name
        if not provider_name and model:
            # Only set provider_name if it's not already set in the session
            if any(model.startswith(prefix) for prefix in ["claude", "anthropic"]):
                provider_name = "anthropic"
                session.provider_name = provider_name
                logger.info(f"Stream: Using Anthropic provider for model {model}")
            elif any(model.startswith(prefix) for prefix in ["gpt", "text-", "openai"]):
                provider_name = "openai"
                session.provider_name = provider_name
                logger.info(f"Stream: Using OpenAI provider for model {model}")
            else:
                logger.info(f"Stream: No specific provider for model {model}, using default")
        elif provider_name:
            logger.info(f"Stream: Using stored provider: {provider_name}")
        else:
            logger.info("Stream: No model or provider specified, using default provider")
        
        # Initialize assistant message
        assistant_message = Message(
            role=MessageRole.ASSISTANT,
            content=TextContent(
                type=MessageContentType.TEXT,
                text=""
            ),
            created_at=datetime.now(),
        )
        session.messages.append(assistant_message)
            
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
                    # Update the message content
                    if isinstance(assistant_message.content, TextContent):
                        assistant_message.content.text = full_text
                    else:
                        assistant_message.content = TextContent(
                            type=MessageContentType.TEXT,
                            text=full_text
                        )
                    
                    # Yield the chunk
                    yield text_chunk
                    
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
                        session.provider_name = "mock"
                        
                        async for text_chunk in provider.generate_stream(
                            messages=llm_messages,
                            model=model,
                        ):
                            full_text += text_chunk
                            # Update the message content
                            if isinstance(assistant_message.content, TextContent):
                                assistant_message.content.text = full_text
                            else:
                                assistant_message.content = TextContent(
                                    type=MessageContentType.TEXT,
                                    text=full_text
                                )
                            
                            # Yield the chunk
                            yield text_chunk
                    else:
                        # Re-raise the error if we can't use the fallback
                        raise
                else:
                    # Re-raise other errors
                    raise
            
            # Update session timestamp
            session.updated_at = datetime.now()
            
        except Exception as e:
            # Create error message
            error_text = f"Error generating response: {str(e)}"
            if isinstance(assistant_message.content, TextContent):
                assistant_message.content.text = error_text
            else:
                assistant_message.content = TextContent(
                    type=MessageContentType.TEXT,
                    text=error_text
                )
            
            # Update session timestamp
            session.updated_at = datetime.now()
            
            # Yield the error
            yield error_text
    
    def _convert_to_llm_messages(self, messages: List[Message]) -> List[LLMMessage]:
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


# Global chat store instance
chat_store = ChatStore()