"""Core application configuration"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    # API Settings
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Reflection Agent"
    VERSION: str = "0.1.0"

    # CORS Settings
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173"]

    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # External API Keys
    TAVILY_API_KEY: str
    API_KEY: str
    BASE_URL: str = "https://openrouter.ai/api/v1"


    # Base Config
    number_of_initial_queries: int = 3
    max_research_loops: int = 2

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
