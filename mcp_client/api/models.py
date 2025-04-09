"""
API response models.
"""
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

from pydantic import BaseModel, Field, ConfigDict


# MCP Models
class ToolSchema(BaseModel):
    """Schema for a tool."""
    name: str
    description: Optional[str] = None
    input_schema: Dict[str, Any] = Field(default_factory=dict)


class ResourceSchema(BaseModel):
    """Schema for a resource."""
    uri: str
    name: str
    description: Optional[str] = None
    mime_type: Optional[str] = None


class PromptArgumentSchema(BaseModel):
    """Schema for a prompt argument."""
    name: str
    description: Optional[str] = None
    required: bool = False


class PromptSchema(BaseModel):
    """Schema for a prompt."""
    name: str
    description: Optional[str] = None
    arguments: List[Dict[str, Any]] = Field(default_factory=list)


class ServerInfoSchema(BaseModel):
    """Schema for server information."""
    name: str
    url: str
    transport_type: str
    connected: bool
    tools_count: int
    resources_count: int
    prompts_count: int


class HealthCheckResponse(BaseModel):
    """Health check response."""
    status: str = "ok"


class ServersResponse(BaseModel):
    """Servers list response."""
    servers: Dict[str, ServerInfoSchema]


class ToolResponse(BaseModel):
    """Tool response."""
    server_name: str
    tool: ToolSchema


class ToolsResponse(BaseModel):
    """Tools list response."""
    tools: List[ToolResponse]


class ResourceResponse(BaseModel):
    """Resource response."""
    server_name: str
    resource: ResourceSchema


class ResourcesResponse(BaseModel):
    """Resources list response."""
    resources: List[ResourceResponse]


class PromptResponse(BaseModel):
    """Prompt response."""
    server_name: str
    prompt: PromptSchema


class PromptsResponse(BaseModel):
    """Prompts list response."""
    prompts: List[PromptResponse]


# Chat Models
class MessageRole(str, Enum):
    """Message role enum."""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class MessageContentType(str, Enum):
    """Message content type enum."""
    TEXT = "text"
    IMAGE = "image"
    RESOURCE = "resource"
    TOOL_CALL = "tool_call"
    TOOL_RESULT = "tool_result"


class TextContent(BaseModel):
    """Text content model."""
    type: MessageContentType = MessageContentType.TEXT
    text: str


class ImageContent(BaseModel):
    """Image content model."""
    type: MessageContentType = MessageContentType.IMAGE
    url: str
    alt_text: Optional[str] = None


class ResourceContent(BaseModel):
    """Resource content model."""
    type: MessageContentType = MessageContentType.RESOURCE
    uri: str
    mime_type: Optional[str] = None
    name: Optional[str] = None


class ToolCallContent(BaseModel):
    """Tool call content model."""
    type: MessageContentType = MessageContentType.TOOL_CALL
    tool_name: str
    arguments: Dict[str, Any] = Field(default_factory=dict)
    server_name: Optional[str] = None


class ToolResultContent(BaseModel):
    """Tool result content model."""
    type: MessageContentType = MessageContentType.TOOL_RESULT
    tool_name: str
    result: Any
    is_error: bool = False
    server_name: Optional[str] = None


MessageContent = Union[TextContent, ImageContent, ResourceContent, ToolCallContent, ToolResultContent]


class Message(BaseModel):
    """Chat message model."""
    id: UUID = Field(default_factory=uuid4)
    role: MessageRole
    content: Union[str, MessageContent, List[MessageContent]]
    created_at: datetime = Field(default_factory=datetime.now)
    
    model_config = ConfigDict(
        json_encoders={
            UUID: str,
            datetime: lambda v: v.isoformat(),
        }
    )


class CreateMessageRequest(BaseModel):
    """Create message request."""
    content: str
    role: MessageRole = MessageRole.USER


class ChatSession(BaseModel):
    """Chat session model."""
    id: UUID = Field(default_factory=uuid4)
    title: str
    messages: List[Message] = Field(default_factory=list)
    model: Optional[str] = None
    provider_name: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    model_config = ConfigDict(
        json_encoders={
            UUID: str,
            datetime: lambda v: v.isoformat(),
        }
    )


class ChatSessionSummary(BaseModel):
    """Chat session summary for listings."""
    id: UUID
    title: str
    message_count: int
    created_at: datetime
    updated_at: datetime
    model: Optional[str] = None


class CreateSessionRequest(BaseModel):
    """Create session request."""
    title: str
    model: Optional[str] = None
    system_prompt: Optional[str] = None


class ChatSessionsResponse(BaseModel):
    """Chat sessions list response."""
    sessions: List[ChatSessionSummary]


class ChatSessionResponse(BaseModel):
    """Chat session response."""
    session: ChatSession


class MessageResponse(BaseModel):
    """Message response."""
    message: Message