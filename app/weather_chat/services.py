from logging import getLogger

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

from app.config import config
from app.bedrock.client import client
from app.weather_chat.agents import WeatherAgent

logger = getLogger(__name__)


async def process_weather_message(message: str):
    async with streamablehttp_client(config.mcp_url) as (r, w, _), ClientSession(r, w) as mcp_session:
        await mcp_session.initialize()

        weather_agent = WeatherAgent(client, mcp_session)

        return await weather_agent.run(message)

