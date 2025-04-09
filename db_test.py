"""
Test script voor database functionaliteit.
"""
from mcp_client.database.base import init_db, Base
from mcp_client.database.models import ChatSession, Message
from sqlalchemy import create_engine
from mcp_client.config.settings import settings
from sqlalchemy.orm import sessionmaker

def main():
    """Test database functionaliteit."""
    # Initialize engine
    engine = create_engine(settings.database.url)
    
    # Create tables
    Base.metadata.create_all(engine)
    
    # Create session
    Session = sessionmaker(engine)
    session = Session()
    
    # Add a test chat session
    test_session = ChatSession(
        title='Test Direct DB',
        model='claude-3-sonnet-20240229'
    )
    session.add(test_session)
    session.commit()
    print(f'Session added with ID: {test_session.id}')
    
    # Query all sessions
    all_sessions = session.query(ChatSession).all()
    print(f'Found {len(all_sessions)} sessions:')
    for s in all_sessions:
        print(f'  - {s.id}, {s.title}, {s.model}, created: {s.created_at}')
    
    # Add a message to the session
    message = Message(
        session_id=test_session.id,
        role='user',
        simple_content='This is a test message'
    )
    session.add(message)
    session.commit()
    print(f'Message added with ID: {message.id}')
    
    # Query messages for the session
    session_with_messages = session.query(ChatSession).filter(ChatSession.id == test_session.id).first()
    print(f'Session {session_with_messages.id} has {len(session_with_messages.messages)} messages:')
    for m in session_with_messages.messages:
        print(f'  - {m.id}, {m.role}, {m.simple_content}')
    
    # Cleanup session
    session.close()

if __name__ == '__main__':
    main()