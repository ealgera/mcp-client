"""
Chat API routes.
"""
import logging
from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, status, Depends, Request
from fastapi.responses import StreamingResponse
from starlette.responses import Response
import json

# Custom SSE implementation in case sse_starlette has issues
class SimpleSSEResponse(Response):
    media_type = "text/event-stream"
    
    def __init__(self, generator, status_code=200):
        super().__init__(content=None, status_code=status_code)
        self.generator = generator
    
    async def __call__(self, scope, receive, send):
        await send({
            "type": "http.response.start",
            "status": self.status_code,
            "headers": [
                [b"content-type", b"text/event-stream"],
                [b"cache-control", b"no-cache"],
                [b"connection", b"keep-alive"],
                [b"access-control-allow-origin", b"*"],
            ],
        })
        
        try:
            async for chunk in self.generator:
                if chunk:
                    # Format as plain text data without JSON
                    if isinstance(chunk, dict) and "data" in chunk:
                        data = f"data: {chunk['data']}\n\n"
                    else:
                        data = f"data: {chunk}\n\n"
                        
                    await send({
                        "type": "http.response.body",
                        "body": data.encode("utf-8"),
                        "more_body": True,
                    })
        except Exception as e:
            # Log exception and end response
            logger.error(f"SSE error: {str(e)}")
            error_data = f"data: Error: {str(e)}\n\n"
            await send({
                "type": "http.response.body",
                "body": error_data.encode("utf-8"),
                "more_body": True,
            })
        finally:
            # Send end message
            await send({
                "type": "http.response.body",
                "body": b"data: [DONE]\n\n",
                "more_body": True,
            })
            # Close connection
            await send({
                "type": "http.response.body",
                "body": b"",
                "more_body": False,
            })

# Also keep the original SSE implementation
try:
    from sse_starlette.sse import EventSourceResponse
except ImportError:
    # Fallback to our simple implementation
    EventSourceResponse = SimpleSSEResponse

from mcp_client.api.models import (
    ChatSession, Message, CreateSessionRequest, CreateMessageRequest,
    ChatSessionsResponse, ChatSessionResponse, MessageResponse,
    ChatSessionSummary, TextContent, MessageRole, MessageContentType
)
# Switch to the database-backed chat store
from mcp_client.database.chat_store import get_chat_store, DatabaseChatStore


logger = logging.getLogger(__name__)
chat_router = APIRouter()


# Routes for chat sessions
@chat_router.post("/sessions", response_model=ChatSessionResponse)
async def create_session(
    request: CreateSessionRequest,
    chat_store: DatabaseChatStore = Depends(get_chat_store)
) -> ChatSessionResponse:
    """Create a new chat session."""
    try:
        session = chat_store.create_session(request)
        return ChatSessionResponse(session=session)
    except Exception as e:
        logger.error(f"Error creating chat session: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create chat session: {str(e)}",
        )


@chat_router.get("/sessions", response_model=ChatSessionsResponse)
async def get_sessions(chat_store: DatabaseChatStore = Depends(get_chat_store)) -> ChatSessionsResponse:
    """Get all chat sessions."""
    try:
        sessions = chat_store.get_all_sessions()
        return ChatSessionsResponse(sessions=sessions)
    except Exception as e:
        logger.error(f"Error getting chat sessions: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get chat sessions: {str(e)}",
        )


@chat_router.get("/sessions/{session_id}", response_model=ChatSessionResponse)
async def get_session(
    session_id: UUID,
    chat_store: DatabaseChatStore = Depends(get_chat_store)
) -> ChatSessionResponse:
    """Get a chat session by ID."""
    try:
        session = chat_store.get_session(session_id)
        return ChatSessionResponse(session=session)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting chat session {session_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get chat session: {str(e)}",
        )


# Routes for messages
@chat_router.post("/sessions/{session_id}/messages", response_model=MessageResponse)
async def create_message(
    session_id: UUID,
    request: CreateMessageRequest,
    chat_store: DatabaseChatStore = Depends(get_chat_store)
) -> MessageResponse:
    """Create a new message and get a response."""
    try:
        # Process the message and get assistant response
        assistant_message = await chat_store.process_user_message(
            session_id=session_id,
            content=request.content,
        )
        
        return MessageResponse(message=assistant_message)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing message for session {session_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to process message: {str(e)}",
        )


@chat_router.post("/sessions/{session_id}/messages/stream")
async def stream_message(
    session_id: UUID,
    request: CreateMessageRequest,
    chat_store: DatabaseChatStore = Depends(get_chat_store)
):
    """Create a new message and stream the response."""
    try:
        # Create generator function for streaming
        async def event_generator():
            async for chunk in chat_store.stream_user_message(
                session_id=session_id,
                content=request.content,
            ):
                if chunk:
                    yield {"data": chunk}
        
        return EventSourceResponse(event_generator())
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error streaming message for session {session_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to stream message: {str(e)}",
        )


@chat_router.get("/sessions/{session_id}/messages/stream")
async def stream_message_get(
    request: Request,
    session_id: UUID,
    content: str,
    role: str = "user",
    chat_store: DatabaseChatStore = Depends(get_chat_store)
):
    """Create a new message and stream the response (GET version)."""
    try:
        logger.info(f"Starting stream for session {session_id} with content: {content[:30]}...")
        
        # Create generator function for streaming
        async def event_generator():
            try:
                logger.info(f"Starting generator for session {session_id}")
                async for chunk in chat_store.stream_user_message(
                    session_id=session_id,
                    content=content,
                ):
                    if chunk:
                        short_chunk = chunk[:30] + "..." if len(chunk) > 30 else chunk
                        logger.debug(f"Streaming chunk: {short_chunk}")
                        yield {"data": chunk}
                logger.info(f"Completed streaming for session {session_id}")
            except Exception as e:
                logger.error(f"Generator error: {str(e)}")
                yield {"data": f"Error: {str(e)}"}
        
        # Create the SSE response
        try:
            response = SimpleSSEResponse(event_generator())
            return response
        except Exception as e:
            logger.error(f"Failed to create SSE response: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error streaming message for session {session_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to stream message: {str(e)}",
        )