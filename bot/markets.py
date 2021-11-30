from time import time
from typing import Optional

import aiofiles
from ujson import loads
from aiohttp import ClientSession


class Markets(object):
    def __init__(self, file: str, rate_limit: int) -> None:
        self.file = file
        self.rate_limit = rate_limit
        self.last_request = 0

    async def _update_markets(self) -> None:
        async with ClientSession() as session:
            async with session.get("https://www.cryptingup.com/api/markets") as response:
                markets = await response.text()
                self.last_request = int(time())

        async with aiofiles.open(self.file, "w", encoding="utf-8") as file:
            await file.write(markets)

    async def _get_markets(self) -> dict:
        async with aiofiles.open(self.file, "r", encoding="utf-8") as file:
            return loads(await file.read())

    async def _get_coin_market(self, coin: str) -> Optional[dict]:
        if int(time()) - self.last_request > self.rate_limit or self.last_request == 0:
            await self._update_markets()

        for market in (await self._get_markets())["markets"]:
            if market["base_asset"] == coin.upper():
                return market

    async def get_coin(self, coin: str) -> Optional[str]:
        market = await self._get_coin_market(coin)

        if market is not None:
            return "{:.20f}".format(market["price"])

    async def get_day_change(self, coin: str) -> Optional[str]:
        market = await self._get_coin_market(coin)

        if market is not None:
            return "{:.20f}".format(market["change_24h"])
