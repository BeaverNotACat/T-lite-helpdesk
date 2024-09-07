import asyncio
from src.bot import bot
from src.handlers import *  # noqa


asyncio.run(bot.polling())
