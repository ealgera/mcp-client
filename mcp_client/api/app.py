"""
FastAPI application setup.
"""
import logging
import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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
        
        # Setting log levels for noisy loggers
        logging.getLogger("uvicorn").setLevel(logging.WARNING)
        logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
        
        logger.info(f"Starting {settings.app_name}")
        
        # Register LLM providers
        registration_success = False
        
        # Log environment variables for debugging (masking the actual keys)
        logger.info("Environment variables loaded:")
        for env_var in ["OPENAI_API_KEY", "ANTHROPIC_API_KEY"]:
            key_value = os.environ.get(env_var)
            if key_value:
                masked_key = f"{key_value[:4]}...{key_value[-4:]}" if len(key_value) > 8 else "****"
                logger.info(f"  {env_var}: {masked_key} (length: {len(key_value)})")
            else:
                logger.warning(f"  {env_var}: Not found or empty")
        
        for llm_config in settings.llm_providers:
            api_key_env = llm_config.api_key_env
            api_key = None
            
            # Get API key from environment
            api_key = os.environ.get(api_key_env)
            
            # Log key information
            if api_key:
                logger.info(f"API key for {llm_config.name} found with length {len(api_key)}")
            else:
                logger.warning(f"API key for {llm_config.name} not found")
            
            if llm_config.name == "anthropic":
                try:
                    register_anthropic(api_key, llm_config.default_model)
                    logger.info("Registered Anthropic provider")
                    if api_key:
                        registration_success = True
                        logger.info("Anthropic provider registered as active provider with valid API key")
                except Exception as e:
                    logger.error(f"Failed to register Anthropic provider: {str(e)}")
            
            elif llm_config.name == "openai":
                try:
                    register_openai(api_key, llm_config.default_model)
                    logger.info("Registered OpenAI provider")
                    if api_key:
                        registration_success = True
                        logger.info("OpenAI provider registered as active provider with valid API key")
                except Exception as e:
                    logger.error(f"Failed to register OpenAI provider: {str(e)}")
                    
        # Register mock provider as fallback
        from mcp_client.llm.base import provider_registry
        from mcp_client.llm.mock import register_provider as register_mock
        
        # Always register mock provider, but only as default if no other provider was successfully registered
        register_mock(default=not registration_success)
        if not registration_success:
            logger.warning("No LLM providers with API keys registered, using mock provider as default")
        
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