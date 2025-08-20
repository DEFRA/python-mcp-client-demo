from logging import getLogger

from fastapi import APIRouter

from app.weather_chat.models import WeatherChatRequest
from app.weather_chat.services import process_weather_message

logger = getLogger(__name__)

router = APIRouter()


@router.post("/weather-chat")
async def weather_chat(chat_request: WeatherChatRequest):
    logger.info("Received weather chat request")

    response = process_weather_message(chat_request.message)

    logger.info("Weather chat response processed successfully")

    return response
