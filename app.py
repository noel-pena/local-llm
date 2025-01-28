import chainlit as cl
import ollama

@cl.on_chat_start
async def start_chat():
    cl.user_session.set(
        "interaction",
        [
            {
                "role": "system",
                "content": "You are a helpful assistant"
            }
        ],
    )

    msg = cl.Message(content="")

    start_message = """Hello, I am your local AI assistant running on DeepSeek-R1. How can I help you today?"""

    for token in start_message:
        await msg.stream_token(token)

    await msg.send()
