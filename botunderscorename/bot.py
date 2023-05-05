from __future__ import annotations

from botbase import BotBase
from nextcord import Intents, MemberCacheFlags

__all__ = ("BotName",)


class BotName(BotBase):
    def __init__(self) -> None:
        super().__init__(
            name="botname",
            intents=Intents(guilds=True),
            member_cache_flags=MemberCacheFlags.none(),
        )
