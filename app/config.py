from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict()
    python_env: str = "development"
    host: str | None = None
    port: int | None = None
    log_config: str | None = None
    mongo_uri: str | None = None
    mongo_database: str = "python-mcp-client-demo"
    mongo_truststore: str = "TRUSTSTORE_CDP_ROOT_CA"
    aws_endpoint_url: str | None = None
    http_proxy: HttpUrl | None = None
    enable_metrics: bool = False
    tracing_header: str = "x-cdp-request-id"
    bedrock_api_key: str | None = None
    aws_region: str | None = None
    mcp_url: HttpUrl | None = None


config = AppConfig()
