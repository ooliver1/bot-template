# SPDX-License-Identifier: MIT

from __future__ import annotations

from os import environ

import uvloop

from .bot import BotName

bot = BotName()

if __name__ == "__main__":
    uvloop.install()
    bot.run(environ["TOKEN"])
