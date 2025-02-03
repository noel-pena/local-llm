import chainlit
import ollama
from engineio.payload import Payload

# Initializes the chat session
@chainlit.on_chat_start
async def start_chat():
    chainlit.user_session.set(
        "interaction",
        [
            {
                "role": "system",
                "content": "You are a helpful assistant"
            }
        ],
    )

    msg = chainlit.Message(content="")

    start_message = """Hello, I am your local AI assistant running on DeepSeek-R1. How can I help you today?"""

    for token in start_message:
        await msg.stream_token(token)

    await msg.send()

# Processes user input using Ollama
@chainlit.step(type="tool")
async def tool(input_message):
    try:
        interaction = chainlit.user_session.get("interaction")

        interaction.append({"role": "user",
                            "content": input_message})

        response = ollama.chat(model="deepseek-r1",
                               messages=interaction)

        interaction.append({"role": "assistant",
                            "content": response.message.content})

        return response
    except ValueError as e:
        raise ValueError(f"Request processing failed. Details: {e}") from None

# Handles incoming messages in real-time
@chainlit.on_message
async def main(message: chainlit.Message):
    Payload.max_decode_packets = 500

    tool_res = await tool(message.content)

    msg = chainlit.Message(content="")

    for token in tool_res.message.content:
        await msg.stream_token(token)

    await msg.send()

