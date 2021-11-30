from ujson import loads, dumps
from pathlib import Path

from bot.bot import CryptoBot
from bot.commands.crypto import Crypto
from bot.commands.misc import Misc
from bot.markets import Markets


def main() -> None:
    if not Path("config.json").exists():
        with open("config.json", "w", encoding="utf-8") as file:
            file.write(dumps({
                "token": "BOT TOKEN",
                "prefix": "BOT PREFIX",
                "rate_limit": 30  # seconds
            }))

        return

    with open("config.json", "r", encoding="utf-8") as file:
        config = loads(file.read())

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
    main()
