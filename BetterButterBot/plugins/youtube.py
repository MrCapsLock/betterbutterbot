import os
import asyncio
from functools import partial, wraps
from typing import Any, Awaitable, Callable, Union
import logging
import youtube_dl

from pyrogram import Client, filters

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


logging.getLogger("pyrogram").setLevel(logging.WARNING)


def run_sync(func: Callable[..., Any]) -> Awaitable[Any]:
    """Runs the given sync function (optionally with arguments) on a separate thread."""

    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any):
        return await asyncio.get_running_loop().run_in_executor(
            None, partial(func, *args, **kwargs)
        )

    return wrapper


@run_sync
def ytdownloader(url: str) -> Union[int, str]:
    try:
        with youtube_dl.YoutubeDL() as ytdl:
            info = ytdl.extract_info(url, download=True)
            filename = ytdl.prepare_filename(info)
            return filename
    except Exception as e:
        print("Something Went Wrong")
        print(e)


@Client.on_message(filters.regex("youtu.be") | filters.regex("youtube.com"))
async def download_youtube(client, message):
    command = message.text.split(maxsplit=1)
    if len(command) > 1:
        command = command[1]
    else:
        command = command[0]
    filename = await ytdownloader(command)
    await message.reply_video(filename)
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        print("Error: %s file not found" % filename)
