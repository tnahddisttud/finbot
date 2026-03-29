from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ── Azure OpenAI (Foundry v1 endpoint) ───────────────
    azure_openai_endpoint: str = ""
    azure_openai_api_key: str = ""
    azure_openai_deployment: str = "gpt-oss-120b"

    # ── SerpAPI ───────────────────────────────────────────
    serpapi_api_key: str = ""

    # ── SQLite ────────────────────────────────────────────
    sqlite_db_path: str = ".data/finance_agent.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )


settings = Settings()