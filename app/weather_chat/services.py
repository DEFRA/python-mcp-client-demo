from logging import getLogger

import boto3
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

from app.config import config
from app.weather_chat.agents import WeatherAgent

logger = getLogger(__name__)


async def process_weather_message(message: str):
    async with streamablehttp_client(config.mcp_url) as (r, w, _), ClientSession(r, w) as mcp_session:
        await mcp_session.initialize()

        client = boto3.client(
            "bedrock-runtime",
            region_name=config.aws_region
        )

        weather_agent = WeatherAgent(client, mcp_session)

        return await weather_agent.run(message)

