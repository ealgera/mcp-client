"""
Main application entry point.
"""
import os
import uvicorn

from mcp_client.config.settings import settings


def main() -> None:
    """Run the application."""
    uvicorn.run(
        "mcp_client.api.app:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )


if __name__ == "__main__":
    main()