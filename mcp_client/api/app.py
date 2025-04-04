"""
FastAPI application setup.
"""
import logging
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from mcp_client.config.settings import settings
from mcp_client.api.routes import api_router
from mcp_client.core.mcp.client import MCPConnectionManager
from mcp_client.llm.anthropic import register_provider as register_anthropic
from mcp_client.llm.openai import register_provider as register_openai


logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    # Create FastAPI app
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="MCP Client Application",
        debug=settings.debug,
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include API routes
    app.include_router(api_router, prefix=f"{settings.api_prefix}/{settings.api_version}")
    
    # Mount static files
    static_dir = Path(__file__).parent.parent / "static"
    if static_dir.exists() and static_dir.is_dir():
        app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
    else:
        logger.warning(f"Static directory not found: {static_dir}")
        static_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created static directory: {static_dir}")
    
    # Register startup and shutdown events
    @app.on_event("startup")
    async def startup_event():
        """Initialize services on startup."""
        # Set up logging
        logging.basicConfig(
            level=logging.DEBUG if settings.debug else logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        
        logger.info(f"Starting {settings.app_name}")
        
        # Register LLM providers
        for llm_config in settings.llm_providers:
            api_key_env = llm_config.api_key_env
            api_key = None
            if api_key_env in globals():
                api_key = globals()[api_key_env]
            
            if llm_config.name == "anthropic":
                try:
                    register_anthropic(api_key, llm_config.default_model)
                    logger.info("Registered Anthropic provider")
                except Exception as e:
                    logger.error(f"Failed to register Anthropic provider: {str(e)}")
            
            elif llm_config.name == "openai":
                try:
                    register_openai(api_key, llm_config.default_model)
                    logger.info("Registered OpenAI provider")
                except Exception as e:
                    logger.error(f"Failed to register OpenAI provider: {str(e)}")
        
        # Connect to MCP servers
        try:
            mcp_manager = MCPConnectionManager(settings.mcp_servers_config_path)
            app.state.mcp_manager = mcp_manager
            await mcp_manager.connect_all()
            logger.info("Connected to MCP servers")
        except Exception as e:
            logger.error(f"Failed to connect to MCP servers: {str(e)}")
    
    @app.on_event("shutdown")
    async def shutdown_event():
        """Clean up resources on shutdown."""
        logger.info(f"Shutting down {settings.app_name}")
        
        # Disconnect from MCP servers
        if hasattr(app.state, "mcp_manager"):
            await app.state.mcp_manager.disconnect_all()
            logger.info("Disconnected from MCP servers")
    
    return app


app = create_app()