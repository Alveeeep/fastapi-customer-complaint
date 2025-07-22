from openai import DefaultAioHttpClient
from openai import AsyncOpenAI
from app.config import Settings


async def get_chatgpt_response(text: str) -> str:
    async with AsyncOpenAI(
            api_key=Settings.OPENAI_TOKEN.get_secret_value(),
            http_client=DefaultAioHttpClient(proxy=Settings.PROXY_URL.get_secret_value()),
    ) as client:
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content
