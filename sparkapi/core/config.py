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
