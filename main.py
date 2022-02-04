from __future__ import annotations

import asyncio
import os

from dotenv import load_dotenv
import nextcord
from botbase import BotBase

# REMOVE ON WINDOWS
import uvloop  # type: ignore

# REMOVE ON WINDOWS


DEFAULT_PREFIX = "."
# REMOVE ON WINDOWS
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# REMOVE ON WINDOWS
load_dotenv()


class MyBot(BotBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


intents = nextcord.Intents.none()
intents.guilds = True
intents.messages = True
bot = MyBot(
    intents=intents,
)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run(os.getenv("TOKEN"))
