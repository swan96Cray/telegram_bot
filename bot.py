import telebot

TOKEN = "8671080123:AAFoxiLzPJtCLyg7jMojeCEAmFhjuV0wNCM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ Бот работает на Render!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "Ты написал: " + message.text)

print("🚀 Бот запущен...")
bot.infinity_polling()
