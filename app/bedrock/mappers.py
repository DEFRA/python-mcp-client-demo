def mcp_tool_to_bedrock(tool):
    return {
        "toolSpec": {
            "name": tool.name,
            "description": tool.description,
            "inputSchema": {
                "json": {
                    **tool.inputSchema
                }
            },
        },
    }

def mcp_tool_result_to_bedrock(toolUseId, result):
    response = {
        "toolUseId": toolUseId
    }

    response["content"] = {
        "json": {
            "content": [result.structuredContent]
        }
    }

    if result.isError == True:
        response["status"] = "error"

    return response
