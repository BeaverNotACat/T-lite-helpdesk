from telebot.ext.ApplicationBuilder

BOT_TOKEN = '7480734220:AAGcsLr6fnGXieiInuOa_i4_U7qMR-atz04'

bot = ApplicationBuilder().builder().token(BOT_TOKEN).read_timeout(100).get_updates_read_timeout(100).build()
