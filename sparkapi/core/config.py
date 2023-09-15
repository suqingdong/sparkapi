from pydantic_settings import BaseSettings, SettingsConfigDict


class SparkConfig(BaseSettings):
    app_id: str
    api_key: str
    api_secret: str
    api_model: str = 'v1.5'

    model_config = SettingsConfigDict(
        env_file='~/.sparkapi.env',
        env_prefix='SPARK_',
        case_sensitive=False,
    )


class ChatConfig(BaseSettings):
    temperature: float = 0.5
    max_tokens: int = 2048
    top_k: int = 4

    model_config = SettingsConfigDict(
        env_file='~/.sparkapi.env',
        env_prefix='SPARK_CHAT_',
        case_sensitive=False,
    )


if __name__ == '__main__':
    print(1, SparkConfig(_env_file='.env'))
    print(2, ChatConfig(_env_file='.env'))
