from time import time

from lightbulb import Plugin, command, Context


class Misc(Plugin):
    @command()
    async def ping(self, ctx: Context) -> None:
        send = time()
        message = await ctx.respond("Pong!")
        milliseconds = int((time() - send) * 1000)
        await message.edit(f"Pong! `{milliseconds} ms`")

    @command()
    async def echo(self, ctx: Context, *args) -> None:
        await ctx.respond(" ".join(args))
