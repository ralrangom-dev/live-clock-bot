import os
import asyncio
from datetime import datetime, timezone

from telethon import TelegramClient, functions
from telethon.sessions import StringSession
from telethon.errors import FloodWaitError

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION_STRING = os.environ["SESSION_STRING"]


async def main():
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.start()

    me = await client.get_me()
    print(f"Logged in as: {me.first_name}")

    while True:
        clock = datetime.now(timezone.utc).strftime("%H:%M")

        try:
            await client(functions.account.UpdateProfileRequest(
                last_name=f"🕐 {clock}"
            ))
            print(f"Updated: {clock} UTC")
        except FloodWaitError as e:
            print(f"Telegram rate limit: waiting {e.seconds} seconds")
            await asyncio.sleep(e.seconds)
            continue
        except Exception as e:
            print(f"Update error: {e}")

        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())
