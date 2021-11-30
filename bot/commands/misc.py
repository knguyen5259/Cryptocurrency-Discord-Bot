from time import time

from lightbulb import Plugin, command
from lightbulb.context import Context


class Misc(Plugin):
    def __init__(self) -> None:
        super().__init__("Misc")

    @command("ping", "Checks the latency of the bot")
    async def ping(self, ctx: Context) -> None:
        send = time()
        message = await ctx.respond("Pong!")
        milliseconds = int((time() - send) * 1000)
        await message.edit(f"Pong! `{milliseconds} ms`")

    @command("echo", "Repeats what you say")
    async def echo(self, ctx: Context, *args) -> None:
        await ctx.respond(" ".join(args))
