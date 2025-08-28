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

def mcp_tool_result_to_bedrock(tool_use_id, result):
    response = {
        "toolUseId": tool_use_id
    }

    response["content"] = {
        "json": {
            "content": [result.structuredContent]
        }
    }

    if result.isError:
        response["status"] = "error"

    return response
