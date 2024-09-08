from telebot.types import Message
import httpx

from src.bot import bot


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message: Message):
    await bot.send_message(message.chat.id, "Здравствуйте, пожалуйста отправьте любой вопрос и я перешлю ео AI асситенту")

@bot.message_handler()
async def assist(message: Message):
    responce = httpx.post(
       "http://localhost:8000/assist",
           data={"query": message.text}
    )
    await bot.send_message(message.chat.id, responce.text)

