import os
import asyncio
from datetime import datetime, timezone

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


def get_time_text():
    now = datetime.now(timezone.utc)
    return f"🕐 ساعت جهانی: {now.strftime('%H:%M')}"


async def clock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await update.message.reply_text(get_time_text())

    while True:
        await asyncio.sleep(60)
        try:
            await message.edit_text(get_time_text())
        except Exception:
            break


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise RuntimeError("BOT_TOKEN در Variables ریل‌وی تنظیم نشده است.")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("clock", clock))
    app.add_handler(CommandHandler("saat", clock))

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
