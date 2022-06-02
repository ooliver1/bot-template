# bot-template

A bot template for nextcord bots https://github.com/nextcord/nextcord

## Features

- Uses [my botbase](https://github.com/ooliver1/botbase) to reduce boilerplate
- Uses [docker](https://www.docker.com) for consistent environments
- Creates the `logs` structure for the botbase for you
- Creates the bot structure inside of a module to remove bot source from getting lost in the top level
- Uses poetry for less painful dependency management
- Uses uvloop and [speed] for a faster aiohttp client and faster asyncio event loop
- Uses a Bot subclass to reduce the need for refactoring
- Only sets the required intents for the majority of bots
