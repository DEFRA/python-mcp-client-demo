from logging import getLogger

from app.bedrock.mappers import mcp_tool_to_bedrock, mcp_tool_result_to_bedrock
import boto3
from mcp import ClientSession

logger = getLogger(__name__)

class WeatherAgent:
    def __init__(self, llm: boto3.client, mcp_session: ClientSession):
        self.llm = llm
        self.model_id = "anthropic.claude-3-haiku-20240307-v1:0"
        self.mcp_session: ClientSession = mcp_session
        self.messages = []
        self.tools = []

    async def run(self, prompt: str):
        if not self.tools:
            self.tools = [
                mcp_tool_to_bedrock(tool)
                for tool in (await self.mcp_session.list_tools()).tools
            ]

            logger.info(f"Using mpc tools: {self.tools}")

        self.messages.append({"role": "user", "content": [{"text": prompt}]})

        return await self._invoke()

    async def _invoke(self):
        response = self.llm.converse(
            modelId=self.model_id,
            messages=self.messages,
            toolConfig={
                "tools": self.tools,
            }
        )

        await self._handle_response(response)

        return self.messages


    async def _handle_response(self, response):
        self.messages.append(response["output"]["message"])

        stop_reason = response["stopReason"]

        if stop_reason == "tool_use":
            requests = response["output"]["message"]["content"]

            for request in requests:
                if "toolUse" in request:
                    tool = request["toolUse"]

                    logger.info(f"Invoking tool: {tool}")

                    tool_response = await self.mcp_session.call_tool(
                        tool["name"],
                        tool["input"]
                    )

                    self.messages.append({
                        "role": "user",
                        "content": [
                            {
                                "toolResult": {
                                    "toolUseId": tool["toolUseId"],
                                    "content": [{
                                        "json": {
                                            **tool_response.structuredContent
                                        }
                                    }]
                                }
                            }
                        ]
                    })

                    response = self.llm.converse(
                        modelId=self.model_id,
                        messages=self.messages,
                        toolConfig={
                            "tools": self.tools,
                        }
                    )

                    self.messages.append(response["output"]["message"])

