from logging import getLogger

import boto3

from app.config import config

logger = getLogger(__name__)


def process_weather_message(message: str):
    client = boto3.client(
        service_name="bedrock-runtime",
        region_name=config.aws_region
    )

    model_id = "anthropic.claude-3-haiku-20240307-v1:0"

    messages = [
        {
            "role": "user",
            "content": [{"text": message}]
        }
    ]

    return client.converse(
        modelId=model_id,
        messages=messages,
    )

