import asyncio
from openai import DefaultAioHttpClient
from openai import AsyncOpenAI
from app.config import Settings


async def main() -> None:
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
