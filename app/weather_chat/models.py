from pydantic import BaseModel, Field


class WeatherChatRequest(BaseModel):
    message: str = Field(description="The message to send in the chat request", json_schema_extra={
        "example": "What's the weather like in New York?"
    })

