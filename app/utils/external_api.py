import aiohttp
import json
from app.config import Settings
from fastapi import HTTPException, status


async def analyze_sentiment(text: str) -> str:
    url = "https://api.apilayer.com/sentiment/analysis"
    headers = {"apikey": Settings.SENTIMENT_TOKEN.get_secret_value()}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=text.encode("utf-8")) as response:
            result = await response.text()
            try:
                result_json = json.loads(result)
                sentiment = result_json.get("sentiment", "unknown")
                return sentiment
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                     detail=f"Unexpected error: {str(e)}")
