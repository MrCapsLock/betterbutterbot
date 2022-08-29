from os import environ
from pyrogram import Client


tz = environ.get("TIMEZONE", "Asia/Tehran")
app = Client(
    "better-butter-bot",
    session_string=environ["TG_STORE"],
    plugins=dict(root="BetterButterBot/plugins"),
)

app.run()
