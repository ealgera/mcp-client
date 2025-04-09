"""
Mock LLM provider for testing.
"""
import random
import asyncio
import logging
from typing import AsyncIterator, List, Optional

from mcp_client.llm.base import LLMProvider, LLMOptions, Message, provider_registry


logger = logging.getLogger(__name__)


class MockProvider(LLMProvider):
    """Mock LLM provider for testing without API keys."""
    
    def __init__(self, default_model: str = "mock-model"):
        """Initialize the mock provider."""
        self._default_model = default_model
        self._available_models = [default_model, "mock-model-large", "mock-model-small"]
        logger.info(f"MockProvider initialized with model {default_model}")
        
    async def generate(
        self, 
        messages: List[Message], 
        model: Optional[str] = None,
        options: Optional[LLMOptions] = None
    ) -> str:
        """Generate a mock completion."""
        logger.info(f"MockProvider.generate called with model={model}")
        
        # Get the last user message
        user_message = None
        for message in reversed(messages):
            if message.role == "user":
                user_message = message.content
                break
        
        # Generate a mock response
        if not user_message:
            return "I don't have a message to respond to."
        
        # Simple responses based on common questions
        response = self._get_mock_response(user_message)
        
        # Wait to simulate API call
        await asyncio.sleep(0.5)
        
        logger.info(f"MockProvider returning response of length {len(response)}")
        return response
    
    async def generate_stream(
        self, 
        messages: List[Message], 
        model: Optional[str] = None,
        options: Optional[LLMOptions] = None
    ) -> AsyncIterator[str]:
        """Generate a streaming mock completion."""
        logger.info(f"MockProvider.generate_stream called with model={model}")
        
        # Get the last user message
        user_message = None
        for message in reversed(messages):
            if message.role == "user":
                user_message = message.content
                break
        
        # Generate a mock response
        if not user_message:
            yield "I don't have a message to respond to."
            return
            
        # Get the full response
        full_response = self._get_mock_response(user_message)
        
        # Split into words and stream word by word
        words = full_response.split()
        
        for i, word in enumerate(words):
            # Add space except for first word
            prefix = " " if i > 0 else ""
            yield f"{prefix}{word}"
            
            # Random delay between 50-200ms
            await asyncio.sleep(random.uniform(0.05, 0.2))
        
        logger.info(f"MockProvider finished streaming response of {len(words)} words")
    
    def get_available_models(self) -> List[str]:
        """Get the list of available models."""
        return self._available_models
    
    @property
    def default_model(self) -> str:
        """Get the default model for this provider."""
        return self._default_model
        
    def _get_mock_response(self, query: str) -> str:
        """Generate a mock response based on the query."""
        query = query.lower()
        
        if "hello" in query or "hi" in query or "hey" in query:
            return "Hello! I'm a mock AI assistant. I'm here to help you test the chat interface. How can I assist you today?"
            
        elif "weather" in query:
            return "I don't have access to real-time weather data, but I can tell you that in a mock world, it's always sunny with a chance of AI!"
            
        elif "name" in query:
            return "I'm MockGPT, a simulated AI assistant used for testing the chat interface. I don't have access to real AI models, but I can provide predefined responses to help test functionality."
            
        elif "time" in query or "date" in query:
            return "As a mock AI, I don't have access to the current time or date. My responses are predefined for testing purposes."
            
        elif "pythagoras" in query or "stelling van pythagoras" in query:
            return "De stelling van Pythagoras stelt dat in een rechthoekige driehoek het kwadraat van de lengte van de hypotenusa (de zijde tegenover de rechte hoek) gelijk is aan de som van de kwadraten van de lengtes van de andere twee zijden. In wiskundige notatie: a² + b² = c², waarbij c de lengte van de hypotenusa is, en a en b de lengtes van de andere twee zijden zijn."
            
        elif "joke" in query or "grap" in query:
            return "Waarom programmeren programmeurs altijd in het donker? Omdat licht bugs aantrekt!"
            
        elif "thanks" in query or "thank you" in query or "dank" in query or "bedankt" in query:
            return "Je bent welkom! Ik ben blij dat ik kon helpen bij het testen van de chat-interface."
            
        else:
            return "Dit is een geautomatiseerd antwoord van de mock provider. De echte LLM functionaliteit werkt alleen als je API sleutels hebt geconfigureerd in het .env bestand. Voor nu simuleer ik responsies om de interface te testen. Je vraag was: \"" + query + "\""


# Flag to track if we've already registered
_mock_registered = False

# Register the provider
def register_provider(api_key: Optional[str] = None, default_model: Optional[str] = None, default: bool = False) -> None:
    """Register the mock provider."""
    global _mock_registered
    
    # Only register once
    if _mock_registered:
        logger.info("Mock provider already registered, skipping")
        return
        
    provider = MockProvider(default_model or "mock-model")
    provider_registry.register("mock", provider, default)
    _mock_registered = True
    logger.info(f"Mock provider registered with default={default}")