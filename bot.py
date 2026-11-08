import telebot

TOKEN = "9138929656:AAFahQL-pljfmqWDryd90LlOcoTyBxeSd0M"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("📖 Q&A")
    item2 = telebot.types.KeyboardButton("📢 Official News")
    item3 = telebot.types.KeyboardButton("👤 Support")
    markup.add(item1, item2, item3)

    bot.reply_to(message, "🚀 ¡Bienvenido a la plataforma!\nHaz clic en los botones de abajo:", reply_markup=markup)

print("¡Bot ligero iniciado!")
bot.infinity_polling()
