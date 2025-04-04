"""
OpenAI GPT integration.
"""
import os
from typing import Any, AsyncIterator, Dict, List, Optional, Union

try:
    from openai import AsyncOpenAI
except ImportError:
    # Mock classes for development without the SDK
    class AsyncOpenAI:
        def __init__(self, api_key=None):
            self.api_key = api_key or "mock-key"
            
        class ChatCompletion:
            @classmethod
            async def create(cls, *args, **kwargs):
                class Response:
                    class Choice:
                        class Message:
                            content = "This is a mock response"
                        message = Message()
                    choices = [Choice()]
                return Response()
            
            @classmethod
            async def create_stream(cls, *args, **kwargs):
                class Response:
                    class Choice:
                        class Delta:
                            content = "part"
                        delta = Delta()
                    choices = [Choice()]
                
                for part in ["This ", "is ", "a ", "mock ", "streaming ", "response"]:
                    Response.choices[0].delta.content = part
                    yield Response()
                
        chat = type('', (), {'completions': ChatCompletion})()

from mcp_client.llm.base import LLMProvider, LLMOptions, Message, provider_registry


class OpenAIProvider(LLMProvider):
    """OpenAI GPT provider."""
    
    def __init__(self, api_key: Optional[str] = None, default_model: Optional[str] = None):
        """Initialize with API key."""
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not provided and not found in environment")
            
        self.client = AsyncOpenAI(api_key=self.api_key)
        self._default_model = default_model or "gpt-4-turbo"
        self._available_models = [
            "gpt-4-turbo",
            "gpt-4",
            "gpt-3.5-turbo",
        ]
        
    async def generate(
        self, 
        messages: List[Message], 
        model: Optional[str] = None,
        options: Optional[LLMOptions] = None
    ) -> str:
        """Generate a completion with OpenAI GPT."""
        options = options or LLMOptions()
        model_name = model or self._default_model
        
        # Convert our message format to OpenAI's
        openai_messages = []
        for msg in messages:
            if isinstance(msg.content, str):
                openai_messages.append({
                    "role": msg.role,
                    "content": msg.content
                })
            else:
                # Handle content in array format (for multi-modal content)
                openai_messages.append({
                    "role": msg.role,
                    "content": msg.content
                })
        
        # Make the API call
        response = await self.client.chat.completions.create(
            model=model_name,
            messages=openai_messages,
            temperature=options.temperature,
            max_tokens=options.max_tokens,
            stream=False,
            stop=options.stop_sequences or None,
            top_p=options.top_p,
        )
        
        # Extract and return the response text
        return response.choices[0].message.content
        
    async def generate_stream(
        self, 
        messages: List[Message], 
        model: Optional[str] = None,
        options: Optional[LLMOptions] = None
    ) -> AsyncIterator[str]:
        """Generate a streaming completion with OpenAI GPT."""
        options = options or LLMOptions(stream=True)
        model_name = model or self._default_model
        
        # Convert our message format to OpenAI's
        openai_messages = []
        for msg in messages:
            if isinstance(msg.content, str):
                openai_messages.append({
                    "role": msg.role,
                    "content": msg.content
                })
            else:
                # Handle content in array format (for multi-modal content)
                openai_messages.append({
                    "role": msg.role,
                    "content": msg.content
                })
        
        # Make the streaming API call
        stream = await self.client.chat.completions.create(
            model=model_name,
            messages=openai_messages,
            temperature=options.temperature,
            max_tokens=options.max_tokens,
            stream=True,
            stop=options.stop_sequences or None,
            top_p=options.top_p,
        )
        
        async for chunk in stream:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content
    
    def get_available_models(self) -> List[str]:
        """Get the list of available models."""
        return self._available_models
    
    @property
    def default_model(self) -> str:
        """Get the default model for this provider."""
        return self._default_model


# Register the provider
def register_provider(api_key: Optional[str] = None, default_model: Optional[str] = None) -> None:
    """Register the OpenAI provider."""
    provider = OpenAIProvider(api_key, default_model)
    provider_registry.register("openai", provider)