from os import environ
from pyrogram import Client, filters


tz = environ.get("TIMEZONE", "Asia/Tehran")
app = Client(
    "better-butter-bot",
    api_id=environ.get("API_ID"),
    api_hash=environ.get("API_HASH"),
    bot_token=environ.get("BOT_TOKEN"),
)


@app.on_message(filters.command("start"))
async def export_session_string(client, message):
    print("here")
    session_string = await app.export_session_string()
    print(session_string)
    await message.reply_text(f"session_string: `{session_string}`", quote=True)

app.run()
