from pydantic import BaseModel, Field


class WeatherChatRequest(BaseModel):
    message: str = Field(description="The message to send in the chat request", example="Hello, how are you?")

