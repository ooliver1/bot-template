# bot-template

A bot template for [nextcord](https://github.com/nextcord/nextcord) bots.

## Features

- Uses [my botbase](https://github.com/ooliver1/botbase) to reduce boilerplate
- Uses [docker](https://www.docker.com) for consistent environments - [python 3.11 + slim Debian Bullseye](https://github.com/docker-library/python/blob/331890ef059fae05f84c652520b78c340526dc71/3.11/slim-bullseye/Dockerfile)
- Creates the `logs` structure for the botbase for you
- Creates the bot structure inside of a module to remove bot source from getting lost in the top level
- Uses poetry for less painful dependency management
- Uses [uvloop](https://github.com/MagicStack/uvloop) and `[speed]` for a faster aiohttp client and faster asyncio event loop
- Uses a Bot subclass to reduce the need for refactoring
- Only sets guilds intent to encourage granular intents selection
- Uses pre-commit for linting, specifically [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort), and [ruff](https://github.com/charliermarsh/ruff).
