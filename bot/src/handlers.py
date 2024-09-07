from telebot.types import Message

from src.bot import bot


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message: Message):
    await bot.send_message(message.chat.id, "hello")
