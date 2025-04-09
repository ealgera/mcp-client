"""
API routes definition.
"""
from fastapi import APIRouter, HTTPException, Depends, Request, status
from typing import Dict, List, Optional, Any

from mcp_client.core.mcp.client import MCPConnectionManager, MCPServerConnection
from mcp_client.api.models import (
    HealthCheckResponse, ServersResponse, ToolsResponse, ResourcesResponse, 
    PromptsResponse, ServerInfoSchema, ToolResponse, ResourceResponse, 
    PromptResponse, ToolSchema, ResourceSchema, PromptSchema
)
from mcp_client.api.chat_routes import chat_router


# Create API router
api_router = APIRouter()

# Include chat routes
api_router.include_router(chat_router, prefix="/chat", tags=["chat"])


# Helper function to get MCP manager
async def get_mcp_manager(request: Request) -> MCPConnectionManager:
    """Get the MCP connection manager."""
    if not hasattr(request.app.state, "mcp_manager"):
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="MCP connection manager not initialized",
        )
    return request.app.state.mcp_manager


# Routes

@api_router.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """Health check endpoint."""
    return HealthCheckResponse(status="ok")


@api_router.get("/mcp/servers", response_model=ServersResponse)
async def get_mcp_servers(
    mcp_manager: MCPConnectionManager = Depends(get_mcp_manager)
) -> ServersResponse:
    """Get all connected MCP servers."""
    servers = {}
    
    for name, server in mcp_manager.servers.items():
        servers[name] = ServerInfoSchema(
            name=name,
            url=server.config.url,
            transport_type=server.config.transport_type,
            connected=server.connected,
            tools_count=len(server.available_tools),
            resources_count=len(server.available_resources),
            prompts_count=len(server.available_prompts),
        )
    
    return ServersResponse(servers=servers)


@api_router.get("/mcp/tools", response_model=ToolsResponse)
async def get_mcp_tools(
    server_name: Optional[str] = None,
    mcp_manager: MCPConnectionManager = Depends(get_mcp_manager)
) -> ToolsResponse:
    """Get all available tools from all connected MCP servers."""
    tools = []
    
    if server_name:
        if server_name not in mcp_manager.servers:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Server not found: {server_name}",
            )
        
        server = mcp_manager.servers[server_name]
        for tool in server.available_tools:
            tools.append(
                ToolResponse(
                    server_name=server_name,
                    tool=ToolSchema(
                        name=tool.name,
                        description=tool.description,
                        input_schema=tool.input_schema,
                    )
                )
            )
    else:
        all_tools = mcp_manager.get_all_tools()
        for tool_info in all_tools:
            tool = tool_info["tool"]
            tools.append(
                ToolResponse(
                    server_name=tool_info["server_name"],
                    tool=ToolSchema(
                        name=tool.name,
                        description=tool.description,
                        input_schema=tool.input_schema,
                    )
                )
            )
    
    return ToolsResponse(tools=tools)


@api_router.get("/mcp/resources", response_model=ResourcesResponse)
async def get_mcp_resources(
    server_name: Optional[str] = None,
    mcp_manager: MCPConnectionManager = Depends(get_mcp_manager)
) -> ResourcesResponse:
    """Get all available resources from all connected MCP servers."""
    resources = []
    
    if server_name:
        if server_name not in mcp_manager.servers:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Server not found: {server_name}",
            )
        
        server = mcp_manager.servers[server_name]
        for resource in server.available_resources:
            resources.append(
                ResourceResponse(
                    server_name=server_name,
                    resource=ResourceSchema(
                        uri=resource.uri,
                        name=resource.name,
                        description=resource.description,
                        mime_type=resource.mime_type,
                    )
                )
            )
    else:
        all_resources = mcp_manager.get_all_resources()
        for resource_info in all_resources:
            resource = resource_info["resource"]
            resources.append(
                ResourceResponse(
                    server_name=resource_info["server_name"],
                    resource=ResourceSchema(
                        uri=resource.uri,
                        name=resource.name,
                        description=resource.description,
                        mime_type=resource.mime_type,
                    )
                )
            )
    
    return ResourcesResponse(resources=resources)


@api_router.get("/mcp/prompts", response_model=PromptsResponse)
async def get_mcp_prompts(
    server_name: Optional[str] = None,
    mcp_manager: MCPConnectionManager = Depends(get_mcp_manager)
) -> PromptsResponse:
    """Get all available prompts from all connected MCP servers."""
    prompts = []
    
    if server_name:
        if server_name not in mcp_manager.servers:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Server not found: {server_name}",
            )
        
        server = mcp_manager.servers[server_name]
        for prompt in server.available_prompts:
            prompts.append(
                PromptResponse(
                    server_name=server_name,
                    prompt=PromptSchema(
                        name=prompt.name,
                        description=prompt.description,
                        arguments=prompt.arguments,
                    )
                )
            )
    else:
        all_prompts = mcp_manager.get_all_prompts()
        for prompt_info in all_prompts:
            prompt = prompt_info["prompt"]
            prompts.append(
                PromptResponse(
                    server_name=prompt_info["server_name"],
                    prompt=PromptSchema(
                        name=prompt.name,
                        description=prompt.description,
                        arguments=prompt.arguments,
                    )
                )
            )
    
    return PromptsResponse(prompts=prompts)