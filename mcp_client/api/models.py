"""
API response models.
"""
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field


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