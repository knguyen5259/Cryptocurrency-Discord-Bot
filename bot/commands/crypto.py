from time import time
from typing import Optional

from aiohttp import ClientSession
from lightbulb import Plugin, command, Context


class Crypto(Plugin):
    def __init__(self, rate_limit: int) -> None:
        super().__init__()
        self.rate_limit = rate_limit  # Time to wait in between requests (in case of command spam)
        self.markets = {}  # Stores the coin prices
        self.last_request = 0  # UNIX timestamp of the last request send to the API

    @command()
    async def price(self, ctx: Context, coin: str) -> None:
        coin_price = await self.get_coin(coin)

        if coin_price is not None:
            await ctx.respond(f"Price: ${coin_price}")
        else:
            await ctx.respond("Sorry, coin not found.")

    async def update_markets(self) -> None:
        async with ClientSession() as session:
            async with session.get("https://www.cryptingup.com/api/markets") as response:
                self.markets = await response.json()
                self.last_request = int(time())
                print("Updated markets!")

    async def get_coin(self, coin: str) -> Optional[str]:
        if int(time()) - self.last_request > self.rate_limit or self.last_request == 0:
            await self.update_markets()

        for market in self.markets["markets"]:
            if market["base_asset"] == coin.upper():
                return "{:.10f}".format(market["price"])
