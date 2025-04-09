"""
SQLAlchemy models for the database.
"""
import uuid
from datetime import datetime
from typing import List, Optional

from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean, Text, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import JSON, BLOB

from mcp_client.database.base import Base


class ChatSession(Base):
    """Chat session SQLAlchemy model."""
    __tablename__ = "chat_sessions"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(255), nullable=False)
    model = Column(String(100), nullable=True)
    provider_name = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    # Relationships
    messages = relationship("Message", back_populates="session", cascade="all, delete-orphan")


class Message(Base):
    """Message SQLAlchemy model."""
    __tablename__ = "messages"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String(36), ForeignKey("chat_sessions.id"), nullable=False)
    role = Column(String(20), nullable=False)  # user, assistant, system
    created_at = Column(DateTime, default=datetime.now)
    
    # For simple text content, store directly
    # For complex content, use the content relationship
    simple_content = Column(Text, nullable=True)
    
    # Relationships
    session = relationship("ChatSession", back_populates="messages")
    content_items = relationship("MessageContent", back_populates="message", cascade="all, delete-orphan")


class MessageContent(Base):
    """Message content SQLAlchemy model."""
    __tablename__ = "message_contents"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    message_id = Column(String(36), ForeignKey("messages.id"), nullable=False)
    type = Column(String(50), nullable=False)  # text, image, resource, tool_call, tool_result
    order = Column(Integer, nullable=False, default=0)  # Order in the content list
    content = Column(JSON, nullable=False)  # Store the content as JSON
    blob_content = Column(BLOB, nullable=True)  # For binary data like images
    
    # Relationships
    message = relationship("Message", back_populates="content_items")