import asyncio
import discord

async def safe_api_call(coro, max_retries=3):
    for attempt in range(max_retries):
        try:
            return await coro
        except discord.HTTPException as e:
            if e.status == 429:
                retry_after = e.retry_after if hasattr(e, 'retry_after') else 5
                print(f"Rate limit hit, retry after {retry_after}s (attempt {attempt + 1}/{max_retries})")
                await asyncio.sleep(retry_after)
            else:
                raise
    raise Exception("Max retries exceeded for rate limit")
