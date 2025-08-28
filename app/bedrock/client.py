import boto3

from app.config import config

client = boto3.client(
    "bedrock-runtime",
    region_name=config.aws_region,
    endpoint_url=config.bedrock_endpoint_url,
)
