from lightbulb import Plugin, command
from lightbulb.context import Context


class Crypto(Plugin):
    def __init__(self) -> None:
        super().__init__("Crypto")

    @command("price", "Gets the price of a cryptocurrency")
    async def price(self, ctx: Context, coin: str) -> None:
        coin_price = await self.bot.markets.get_coin(coin)

        if coin_price is not None:
            await ctx.respond(f"Price: ${coin_price}")
        else:
            await ctx.respond("Sorry, coin not found.")

    @command("change", "Gets the 24 hour change of a cryptocurrency")
    async def change(self, ctx: Context, coin: str) -> None:
        coin_change = await self.bot.markets.get_day_change(coin)

        if coin_change is not None:
            await ctx.respond(f"Change: ${coin_change}")
        else:
            await ctx.respond("Sorry, coin not found.")
