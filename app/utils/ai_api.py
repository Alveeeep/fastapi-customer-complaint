from openai import DefaultAioHttpClient
from openai import AsyncOpenAI
from app.config import Settings


async def get_chatgpt_response(text: str) -> str:
    async with AsyncOpenAI(
            api_key="My API Key",
            http_client=DefaultAioHttpClient(),
    ) as client:
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-4o",
        )
        return chat_completion.choices[0].message.content
