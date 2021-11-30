from abc import ABC

from lightbulb import BotApp

from bot.markets import Markets


class CryptoBot(BotApp, ABC):
    def __init__(self, token: str, prefix: str, markets: Markets) -> None:
        super().__init__(token, prefix)
        self.markets = markets
