from fastapi import APIRouter

from app.chat.services import process_weather_message
from app.chat.models import WeatherChatRequest

from logging import getLogger

logger = getLogger(__name__)

router = APIRouter()


@router.post("/weather-chat")
async def weather_chat(chat_request: WeatherChatRequest):
    logger.info(f"Received weather chat request: {chat_request.message}")

    response = process_weather_message(chat_request.message)

    logger.info(f"Weather chat response: {response}")

    return response
