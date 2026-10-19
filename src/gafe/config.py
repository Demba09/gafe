from pydantic import SecretStr 
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    llm_base_url: str = "https://opencode.ai/zen/go/v1"
    llm_model: str = "deepseek-v4-flash"
    database_path: str = "data/gafe.db"
    log_level: str = "INFO"
    llm_api_key: SecretStr
