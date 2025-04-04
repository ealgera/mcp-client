"""
MCP Client implementation.
"""
from typing import Dict, List, Optional, Any, Callable
import json
import logging
from pathlib import Path

# Import from the MCP Python SDK
# Note: This is a placeholder for actual MCP SDK imports
try:
    from mcp.client import Client as MCPClient
    from mcp.transport import Transport, SSEClientTransport, StdioClientTransport
    from mcp.types import Tool, Resource, Prompt
except ImportError:
    # Mock classes for development without the SDK
    class Tool:
        def __init__(self, name, description="", input_schema=None):
            self.name = name
            self.description = description
            self.input_schema = input_schema or {"type": "object", "properties": {}}
        
        def __repr__(self):
            return f"Tool(name='{self.name}', description='{self.description}')"
        
    class Resource:
        def __init__(self, uri, name, description="", mime_type=None):
            self.uri = uri
            self.name = name
            self.description = description
            self.mime_type = mime_type
        
        def __repr__(self):
            return f"Resource(uri='{self.uri}', name='{self.name}')"
    
    class Prompt:
        def __init__(self, name, description="", arguments=None):
            self.name = name
            self.description = description
            self.arguments = arguments or []
        
        def __repr__(self):
            return f"Prompt(name='{self.name}', description='{self.description}')"
            
    class Transport:
        """Base transport class."""
        async def start(self):
            pass
            
        async def send(self, message):
            pass
            
        async def close(self):
            pass
        
    class SSEClientTransport(Transport):
        """Mock SSE transport."""
        def __init__(self, url, headers=None, *args, **kwargs):
            self.url = url
            self.headers = headers or {}
            
        async def close(self):
            pass
            
    class StdioClientTransport(Transport):
        """Mock Stdio transport."""
        def __init__(self, command, *args, **kwargs):
            self.command = command
            
        async def close(self):
            pass
            
    class MCPClient:
        """Mock MCP client."""
        def __init__(self, transport):
            self.transport = transport
            self._connected = False
            
        async def connect(self):
            self._connected = True
            return True
            
        async def close(self):
            self._connected = False
            await self.transport.close()
            return True
            
        async def list_tools(self):
            """Return mock tools."""
            return [
                Tool(
                    name="search_web",
                    description="Search the web for information",
                    input_schema={
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"},
                            "limit": {"type": "integer", "default": 5}
                        },
                        "required": ["query"]
                    }
                ),
                Tool(
                    name="execute_command",
                    description="Execute a shell command",
                    input_schema={
                        "type": "object",
                        "properties": {
                            "command": {"type": "string"},
                            "args": {"type": "array", "items": {"type": "string"}}
                        },
                        "required": ["command"]
                    }
                )
            ]
            
        async def list_resources(self):
            """Return mock resources."""
            return [
                Resource(
                    uri="file:///example/document.txt",
                    name="Example Document",
                    description="An example text document",
                    mime_type="text/plain"
                ),
                Resource(
                    uri="file:///example/image.png",
                    name="Example Image",
                    description="An example image",
                    mime_type="image/png"
                )
            ]
            
        async def list_prompts(self):
            """Return mock prompts."""
            return [
                Prompt(
                    name="analyze_code",
                    description="Analyze code for improvements",
                    arguments=[
                        {"name": "language", "description": "Programming language", "required": True},
                        {"name": "code", "description": "Code to analyze", "required": True}
                    ]
                ),
                Prompt(
                    name="summarize_text",
                    description="Summarize text content",
                    arguments=[
                        {"name": "text", "description": "Text to summarize", "required": True},
                        {"name": "max_length", "description": "Maximum summary length", "required": False}
                    ]
                )
            ]

from mcp_client.config.settings import MCPServerConfig


logger = logging.getLogger(__name__)


class MCPServerConnection:
    """Manages a connection to a single MCP server."""
    
    def __init__(self, config: MCPServerConfig):
        """Initialize with server configuration."""
        self.config = config
        self.client: Optional[MCPClient] = None
        self.connected = False
        self.available_tools: List[Tool] = []
        self.available_resources: List[Resource] = []
        self.available_prompts: List[Prompt] = []
    
    async def connect(self) -> bool:
        """Connect to the MCP server."""
        if not self.config.enabled:
            logger.info(f"Server {self.config.name} is disabled, skipping connection")
            return False
        
        try:
            # Create transport based on configuration
            transport = self._create_transport()
            
            # Create MCP client
            self.client = MCPClient(transport)
            
            # Connect to server
            await self.client.connect()
            self.connected = True
            
            # Discover server capabilities
            await self._discover_capabilities()
            
            logger.info(f"Successfully connected to MCP server: {self.config.name}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect to MCP server {self.config.name}: {str(e)}")
            self.connected = False
            return False
    
    def _create_transport(self) -> Transport:
        """Create appropriate transport based on configuration."""
        transport_type = self.config.transport_type.lower()
        
        if transport_type == "sse":
            headers = {}
            if self.config.auth_token:
                headers["Authorization"] = f"Bearer {self.config.auth_token}"
            
            return SSEClientTransport(
                url=self.config.url,
                headers=headers,
            )
        
        elif transport_type == "stdio":
            # For stdio transport, URL should be a command to execute
            return StdioClientTransport(
                command=self.config.url,
            )
        
        else:
            raise ValueError(f"Unsupported transport type: {transport_type}")
    
    async def _discover_capabilities(self) -> None:
        """Discover server capabilities (tools, resources, prompts)."""
        if not self.client or not self.connected:
            return
        
        try:
            # Discover tools
            self.available_tools = await self.client.list_tools()
            logger.debug(f"Discovered {len(self.available_tools)} tools from {self.config.name}")
            
            # Discover resources
            self.available_resources = await self.client.list_resources()
            logger.debug(f"Discovered {len(self.available_resources)} resources from {self.config.name}")
            
            # Discover prompts
            self.available_prompts = await self.client.list_prompts()
            logger.debug(f"Discovered {len(self.available_prompts)} prompts from {self.config.name}")
            
        except Exception as e:
            logger.error(f"Error discovering capabilities from {self.config.name}: {str(e)}")
    
    async def disconnect(self) -> None:
        """Disconnect from the MCP server."""
        if self.client and self.connected:
            try:
                await self.client.close()
                logger.info(f"Disconnected from MCP server: {self.config.name}")
            except Exception as e:
                logger.error(f"Error disconnecting from {self.config.name}: {str(e)}")
            finally:
                self.connected = False
                self.client = None


class MCPConnectionManager:
    """Manages connections to multiple MCP servers."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize the connection manager."""
        self.config_path = config_path
        self.servers: Dict[str, MCPServerConnection] = {}
    
    def load_config(self, config_path: Optional[str] = None) -> List[MCPServerConfig]:
        """Load server configurations from JSON file."""
        path = Path(config_path or self.config_path)
        if not path.exists():
            logger.warning(f"MCP servers config file not found: {path}")
            return []
        
        try:
            with open(path, "r") as f:
                data = json.load(f)
            
            configs = []
            for server_data in data.get("servers", []):
                configs.append(MCPServerConfig(**server_data))
            
            return configs
        
        except Exception as e:
            logger.error(f"Error loading MCP servers config: {str(e)}")
            return []
    
    async def connect_all(self, config_path: Optional[str] = None) -> None:
        """Connect to all configured MCP servers."""
        configs = self.load_config(config_path)
        
        for config in configs:
            # Skip if server is already connected
            if config.name in self.servers and self.servers[config.name].connected:
                continue
                
            # Create and connect server
            server = MCPServerConnection(config)
            connected = await server.connect()
            
            if connected:
                self.servers[config.name] = server
    
    async def disconnect_all(self) -> None:
        """Disconnect from all MCP servers."""
        for name, server in list(self.servers.items()):
            await server.disconnect()
            del self.servers[name]
    
    def get_all_tools(self) -> List[Dict[str, Any]]:
        """Get all available tools from all connected servers."""
        all_tools = []
        
        for server_name, server in self.servers.items():
            if not server.connected:
                continue
                
            for tool in server.available_tools:
                tool_info = {
                    "server_name": server_name,
                    "tool": tool,
                }
                all_tools.append(tool_info)
        
        return all_tools
    
    def get_all_resources(self) -> List[Dict[str, Any]]:
        """Get all available resources from all connected servers."""
        all_resources = []
        
        for server_name, server in self.servers.items():
            if not server.connected:
                continue
                
            for resource in server.available_resources:
                resource_info = {
                    "server_name": server_name,
                    "resource": resource,
                }
                all_resources.append(resource_info)
        
        return all_resources
    
    def get_all_prompts(self) -> List[Dict[str, Any]]:
        """Get all available prompts from all connected servers."""
        all_prompts = []
        
        for server_name, server in self.servers.items():
            if not server.connected:
                continue
                
            for prompt in server.available_prompts:
                prompt_info = {
                    "server_name": server_name,
                    "prompt": prompt,
                }
                all_prompts.append(prompt_info)
        
        return all_prompts