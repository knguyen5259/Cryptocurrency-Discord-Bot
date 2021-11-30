from lightbulb import Plugin, command
from lightbulb.context import Context
from hikari.embeds import Embed
from hikari import Color


class Crypto(Plugin):
    def __init__(self) -> None:
        super().__init__("Crypto")

    @command("price", "Gets the price of a cryptocurrency")
    async def price(self, ctx: Context, coin: str) -> None:
        coin_price = await self.bot.markets.get_coin(coin)

        if coin_price is not None:
            await ctx.respond(embed=Embed(title="Price", description=f"${coin_price}", color=Color.from_rgb(0, 0, 200)))
        else:
            await ctx.respond(embed=Embed(title="Error", description=f"Coin not found", color=Color.from_rgb(200, 0, 0)))

    @command("change", "Gets the 24 hour change of a cryptocurrency")
    async def change(self, ctx: Context, coin: str) -> None:
        coin_change = await self.bot.markets.get_day_change(coin)

        if coin_change is not None:
            await ctx.respond(embed=Embed(title="Change", description=f"${coin_change}", color=Color.from_rgb(0, 0, 200)))
        else:
            await ctx.respond(embed=Embed(title="Error", description=f"Coin not found", color=Color.from_rgb(200, 0, 0)))
