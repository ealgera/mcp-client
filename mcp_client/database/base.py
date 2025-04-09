"""
Database connection and session management.
"""
import logging
import os
from typing import Generator, Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from mcp_client.config.settings import settings

logger = logging.getLogger(__name__)

# Create SQLAlchemy base
Base = declarative_base()

# Database engine
db_url = settings.database.url
engine = create_engine(
    db_url, 
    connect_args={"check_same_thread": False},
    echo=settings.database.echo
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    """Initialize the database."""
    logger.info(f"Initializing database with URL: {db_url}")
    
    # Import models to ensure they are registered with the Base
    from mcp_client.database import models
    
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created")


def get_db_session() -> Generator[Session, None, None]:
    """Get a database session."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()