import asyncio
from pathlib import Path

import aiofiles
from ujson import loads, dumps

from bot.bot import CryptoBot
from bot.commands.crypto import Crypto
from bot.commands.misc import Misc
from bot.markets import Markets


async def main() -> None:
    if not Path("config.json").exists():
        async with aiofiles.open("config.json", "w", encoding="utf-8") as file:
            await file.write(dumps({
                "token": "BOT TOKEN",
                "prefix": "BOT PREFIX",
                "rate_limit": 30  # seconds
            }))

        return

    async with aiofiles.open("config.json", "r", encoding="utf-8") as file:
        config = loads(await file.read())

    bot = CryptoBot(
        token=config["token"],
        prefix=config["prefix"],
        markets=Markets(
            file="markets.json",
            rate_limit=config["rate_limit"]
        )
    )

    bot.add_plugin(Crypto())
    bot.add_plugin(Misc())

    bot.run()


if __name__ == "__main__":
    asyncio.set_event_loop(asyncio.new_event_loop())
    asyncio.get_event_loop().run_until_complete(main())
