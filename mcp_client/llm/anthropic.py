"""
Anthropic Claude integration.
"""
import os
from typing import Any, AsyncIterator, Dict, List, Optional, Union

try:
    import anthropic
except ImportError:
    # Mock classes for development without the SDK
    class anthropic:
        class Anthropic:
            def __init__(self, api_key=None):
                self.api_key = api_key or "mock-key"
                
            async def messages(self, *args, **kwargs):
                class Response:
                    content = [{'text': 'This is a mock response'}]
                return Response()
            
            async def messages_stream(self, *args, **kwargs):
                class Delta:
                    def __init__(self, text):
                        self.text = text
                        self.type = "text_delta"
                        
                class Block:
                    type = "content_block_delta"
                    content_block = {"type": "text"}
                    delta = None
                    
                class Message:
                    type = "message_start"
                    
                class ContentBlockStart:
                    type = "content_block_start"
                    content_block = {"type": "text"}
                
                yield {"type": "message_start", "message": Message()}
                yield {"type": "content_block_start", "content_block": ContentBlockStart()}
                
                for part in ["This ", "is ", "a ", "mock ", "streaming ", "response"]:
                    block = Block()
                    block.delta = Delta(part)
                    yield {"type": "content_block_delta", "delta": block}

from mcp_client.llm.base import LLMProvider, LLMOptions, Message, provider_registry


class AnthropicProvider(LLMProvider):
    """Anthropic Claude provider."""
    
    def __init__(self, api_key: Optional[str] = None, default_model: Optional[str] = None):
        """Initialize with API key."""
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self._has_valid_key = bool(self.api_key)
        
        # Initialize client if key is available
        self.client = anthropic.Anthropic(api_key=self.api_key or "dummy_key")
        self._default_model = default_model or "claude-3-sonnet-20240229"
        self._available_models = [
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
            "claude-2.1",
        ]
        
    async def generate(
        self, 
        messages: List[Message], 
        model: Optional[str] = None,
        options: Optional[LLMOptions] = None
    ) -> str:
        """Generate a completion with Anthropic Claude."""
        import logging
        logger = logging.getLogger(__name__)
        
        # Check if API key is available
        if not self._has_valid_key:
            logger.error("Anthropic API key not provided and not found in environment")
            raise ValueError("Anthropic API key not provided and not found in environment")
        
        options = options or LLMOptions()
        model_name = model or self._default_model
        
        # Convert our message format to Anthropic's
        anthropic_messages = [
            {
                "role": msg.role,
                "content": msg.content
            }
            for msg in messages
        ]
        
        logger.info(f"Calling Anthropic API with model {model_name}")
        
        # Make the API call
        response = await self.client.messages.create(
            model=model_name,
            messages=anthropic_messages,
            temperature=options.temperature,
            max_tokens=options.max_tokens or 4000,
            stream=False,
            stop_sequences=options.stop_sequences or None,
            top_p=options.top_p,
        )
        
        # Extract and return the response text
        return response.content[0].text
        
    async def generate_stream(
        self, 
        messages: List[Message], 
        model: Optional[str] = None,
        options: Optional[LLMOptions] = None
    ) -> AsyncIterator[str]:
        """Generate a streaming completion with Anthropic Claude."""
        import logging
        import asyncio
        from anthropic import Anthropic
        
        logger = logging.getLogger(__name__)
        
        # Check if API key is available
        if not self._has_valid_key:
            logger.error("Anthropic API key not provided and not found in environment")
            raise ValueError("Anthropic API key not provided and not found in environment")
        
        options = options or LLMOptions(stream=True)
        model_name = model or self._default_model
        
        # Convert our message format to Anthropic's
        anthropic_messages = [
            {
                "role": msg.role,
                "content": msg.content
            }
            for msg in messages
        ]
        
        logger.info(f"Calling Anthropic streaming API with model {model_name}")
        
        # Direct implementation for Anthropic v0.49.0
        try:
            # Direct approach using anthropic.Anthropic for specific version
            # This avoids the async iteration issues
            stream_response = self.client.messages.create(
                model=model_name,
                messages=anthropic_messages,
                temperature=options.temperature,
                max_tokens=options.max_tokens or 4000,
                stream=True,
                stop_sequences=options.stop_sequences or None,
                top_p=options.top_p,
            )
            
            # Process the stream synchronously
            for chunk in stream_response:
                if chunk.type == "content_block_delta" and chunk.delta.type == "text_delta":
                    text = chunk.delta.text
                    if text:
                        # Small delay to allow for async behavior
                        await asyncio.sleep(0.001)
                        yield text
                        
        except Exception as e:
            logger.error(f"Error in Anthropic streaming: {str(e)}")
            error_msg = f"Anthropic streaming error: {str(e)}"
            logger.error(error_msg)
            raise ValueError(error_msg)
    
    def get_available_models(self) -> List[str]:
        """Get the list of available models."""
        return self._available_models
    
    @property
    def default_model(self) -> str:
        """Get the default model for this provider."""
        return self._default_model


# Register the provider
def register_provider(api_key: Optional[str] = None, default_model: Optional[str] = None) -> None:
    """Register the Anthropic provider."""
    provider = AnthropicProvider(api_key, default_model)
    provider_registry.register("anthropic", provider)