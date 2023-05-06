from __future__ import annotations

from logging import getLogger
from traceback import format_exception

from botbase import CogBase
from nextcord import ApplicationInvokeError

from botunderscorename.bot import BotName
from botunderscorename.inter import Inter

log = getLogger(__name__)


FORMAT = """command {command} gave
```py
{tb}
```
{channel} ({name}) in {guild} by {inter.user}
""".strip()


class ErrorHandler(CogBase[BotName]):
    @CogBase.listener()
    async def on_application_command_error(self, inter: Inter, exc: Exception) -> None:
        if isinstance(exc, ApplicationInvokeError):
            exc = exc.original

        if False:  # TODO: Add specific error checks.
            ...
        else:
            log.error("Unhandled error in command.", exc_info=exc)
            if log_channel_id := self.bot.log_channel:
                log_channel = await self.bot.getch_channel(log_channel_id)

                command = (
                    inter.application_command.qualified_name
                    if inter.application_command
                    else ""
                )
                if inter.guild is None:
                    channel = "dm"
                    name = "dm"
                    guild = "dm"
                else:
                    channel = inter.channel.mention  # pyright: ignore
                    name = inter.channel.name  # pyright: ignore
                    guild = inter.guild.name

                tb = "\n".join(format_exception(exc))
                await log_channel.send_embed(
                    desc=FORMAT.format(
                        tb=tb,
                        channel=channel,
                        inter=inter,
                        name=name,
                        guild=guild,
                        command=command,
                    )
                )


def setup(bot: BotName) -> None:
    bot.add_cog(ErrorHandler(bot))
