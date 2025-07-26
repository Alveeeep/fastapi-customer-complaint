from openai import AsyncOpenAI
from app.config import settings
from loguru import logger


async def get_chatgpt_response(text: str) -> str:
    async with AsyncOpenAI(
            api_key=settings.OPENAI_TOKEN.get_secret_value(),
            base_url="https://hubai.loe.gg/v1"
    ) as client:
        try:
            chat_completion = await client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Определи категорию жалобы: {text}."
                                   f" Варианты: техническая, оплата, другое. Ответ только одним словом без знаков препинания",
                    }
                ],
                model="gpt-3.5-turbo",
            )
            logger.info(f"Ответ от ChatGPT - {chat_completion.choices[0].message.content}")
            return chat_completion.choices[0].message.content
        except Exception as e:
            logger.error(f"ChatGPT не смог обработать: {e}")
            return 'другое'
