"""
Base classes for LLM providers.
"""
from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, Dict, List, Optional, Union

from pydantic import BaseModel


class Message(BaseModel):
    """A message in a conversation."""
    
    role: str  # "user", "assistant", "system"
    content: Union[str, List[Dict[str, Any]]]


class LLMOptions(BaseModel):
    """Options for LLM generation."""
    
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    stop_sequences: List[str] = []
    top_p: float = 1.0
    stream: bool = True


class LLMProvider(ABC):
    """Base class for LLM providers."""
    
    @abstractmethod
    async def generate(
        self, 
        messages: List[Message], 
        model: Optional[str] = None,
        options: Optional[LLMOptions] = None
    ) -> str:
        """Generate a completion for the given messages."""
        pass
    
    @abstractmethod
    async def generate_stream(
        self, 
        messages: List[Message], 
        model: Optional[str] = None,
        options: Optional[LLMOptions] = None
    ) -> AsyncIterator[str]:
        """Generate a streaming completion for the given messages."""
        pass
    
    @abstractmethod
    def get_available_models(self) -> List[str]:
        """Get the list of available models."""
        pass
    
    @property
    @abstractmethod
    def default_model(self) -> str:
        """Get the default model for this provider."""
        pass


class LLMProviderRegistry:
    """Registry for LLM providers."""
    
    def __init__(self):
        self.providers: Dict[str, LLMProvider] = {}
        self.default_provider: Optional[str] = None
    
    def register(self, name: str, provider: LLMProvider, default: bool = False) -> None:
        """Register a provider."""
        self.providers[name] = provider
        if default or self.default_provider is None:
            self.default_provider = name
    
    def get_provider(self, name: Optional[str] = None) -> LLMProvider:
        """Get a provider by name, or the default if no name is provided."""
        if name is None:
            if self.default_provider is None:
                raise ValueError("No default provider registered")
            name = self.default_provider
            
        if name not in self.providers:
            raise ValueError(f"Provider not found: {name}")
            
        return self.providers[name]
    
    def get_available_providers(self) -> List[str]:
        """Get a list of available provider names."""
        return list(self.providers.keys())


# Global provider registry
provider_registry = LLMProviderRegistry()