from pyrogram import Client, filters


@Client.on_message(filters.command("start"))
async def welcome(client, message):
    await message.reply_text("Welcome to Better Butter Bot.")
