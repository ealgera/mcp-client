"""
Application settings module.
"""
import os
from pathlib import Path
from typing import Dict, List, Optional, Any

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = BASE_DIR / "mcp_client_config"


class LLMSettings(BaseModel):
    """Settings for an LLM provider."""

    name: str
    api_key_env: str
    default_model: str
    available_models: List[str]


class DatabaseSettings(BaseModel):
    """Database connection settings."""

    url: str = Field(default="sqlite:///./mcp_client.db")
    echo: bool = Field(default=False)


class MCPServerConfig(BaseModel):
    """Configuration for a single MCP server."""

    name: str
    url: str
    transport_type: str = "sse"  # or "stdio"
    auth_token: Optional[str] = None
    enabled: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Settings(BaseSettings):
    """Application settings."""

    # App settings
    app_name: str = "MCP Client"
    debug: bool = False
    secret_key: str = "changeme"

    # API settings
    api_prefix: str = "/api"
    api_version: str = "v1"

    # Server settings
    host: str = "127.0.0.1"
    port: int = 8000
    cors_origins: List[str] = ["*"]
    
    # Database settings
    database: DatabaseSettings = DatabaseSettings()

    # LLM settings
    llm_providers: List[LLMSettings] = [
        LLMSettings(
            name="anthropic",
            api_key_env="ANTHROPIC_API_KEY",
            default_model="claude-3-sonnet-20240229",
            available_models=[
                "claude-3-opus-20240229",
                "claude-3-sonnet-20240229",
                "claude-3-haiku-20240307",
                "claude-2.1",
            ],
        ),
        LLMSettings(
            name="openai",
            api_key_env="OPENAI_API_KEY",
            default_model="gpt-4-turbo",
            available_models=[
                "gpt-4-turbo",
                "gpt-4",
                "gpt-3.5-turbo",
            ],
        ),
    ]

    # MCP server configs
    mcp_servers_config_path: str = str(CONFIG_DIR / "servers.json")
    mcp_servers: List[MCPServerConfig] = []

    # Frontend settings
    static_dir: str = str(BASE_DIR / "frontend" / "dist")
    templates_dir: str = str(BASE_DIR / "frontend" / "dist")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


# Create global settings instance
settings = Settings()