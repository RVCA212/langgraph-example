import os
from dataclasses import dataclass, field, fields
from typing import Any, Optional
from langchain_core.runnables import RunnableConfig
from typing_extensions import Annotated
from dataclasses import dataclass

@dataclass(kw_only=True)
class Configuration:
    """The configurable fields for the chatbot."""
    user_id: str = "default-user"
    todo_category: str = "general"
    task_maistro_role: str = "You are a helpful task management assistant. You help create, organize, and manage the user's ToDo list."
    openai_api_key: Optional[str] = field(default_factory=lambda: os.getenv("OPENAI_API_KEY"))
    model_name: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 1000
    verbose: bool = False
    config_dict: RunnableConfig = field(default_factory=lambda: {"callbacks": None})
    
    @classmethod
    def from_env(cls) -> "Configuration":
        """Create a Configuration instance from environment variables."""
        return cls(
            user_id=os.getenv("USER_ID", "default-user"),
            todo_category=os.getenv("TODO_CATEGORY", "general"),
            task_maistro_role=os.getenv("TASK_MAISTRO_ROLE", cls.task_maistro_role),
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model_name=os.getenv("MODEL_NAME", "gpt-3.5-turbo"),
            temperature=float(os.getenv("TEMPERATURE", "0.7")),
            max_tokens=int(os.getenv("MAX_TOKENS", "1000")),
            verbose=os.getenv("VERBOSE", "False").lower() == "true"
        )
    
    def to_dict(self) -> dict[str, Any]:
        """Convert the configuration to a dictionary."""
        return {field.name: getattr(self, field.name) for field in fields(self)}
