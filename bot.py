import telebot

TOKEN = "9138929656:AAEXbOpKbUauCv2Uk5S7omuqphhRxv8-WpY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("📖 Q&A")
    item2 = telebot.types.KeyboardButton("📢 Official News")
    item3 = telebot.types.KeyboardButton("👤 Support")
    markup.add(item1, item2, item3)
    
    bot.reply_to(message, "🚀 ¡Bienvenido a la plataforma!\nHaz clic en los botones de abajo:", reply_markup=markup)

# Respuesta para el botón "📖 Q&A"
@bot.message_handler(func=lambda message: message.text == "📖 Q&A")
def responder_qa(message):
    texto = (
        "❓ **Preguntas Frecuentes (Q&A):**\n\n"
        "1. ¿Cómo funciona la plataforma?\n"
        "Aquí puedes explicar los detalles de tu servicio.\n\n"
        "2. ¿Cómo ingreso?\n"
        "Usa el enlace oficial de registro."
    )
    bot.reply_to(message, texto, parse_mode="Markdown")

# Respuesta para el botón "📢 Official News"
@bot.message_handler(func=lambda message: message.text == "📢 Official News")
def responder_news(message):
    texto = (
        "📢 **Noticias Oficiales:**\n\n"
        "¡Mantente al día con nuestras últimas actualizaciones, anuncios y eventos especiales!"
    )
    bot.reply_to(message, texto, parse_mode="Markdown")

# Respuesta para el botón "👤 Support"
@bot.message_handler(func=lambda message: message.text == "👤 Support")
def responder_support(message):
    texto = (
        "👤 **Soporte y Ayuda:**\n\n"
        "Si tienes algún inconveniente o duda, puedes contactar al equipo de administración directamente."
    )
    bot.reply_to(message, texto, parse_mode="Markdown")

print("¡Bot ligero iniciado!")
bot.infinity_polling()
