import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8671080123:AAEyGSUVsFoaNMY6oux9srNyvit1LNrpyjA"

bot = telebot.TeleBot(TOKEN)

# Главное меню с кнопками
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("🔪 Афалина"))
    markup.add(KeyboardButton("📐 Вектор"))
    markup.add(KeyboardButton("🐂 Таурус"))
    markup.add(KeyboardButton("⚖️ Баланс"))
    markup.add(KeyboardButton("🏛️ Рубикон"))
    markup.add(KeyboardButton("🌸 Ирис"))
    return markup

# Кнопки выбора комплектации
def variant_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("💎 Премиум"))
    markup.add(KeyboardButton("⭐ Оптимальный"))
    markup.add(KeyboardButton("✅ Базовый"))
    markup.add(KeyboardButton("🔙 Назад в меню"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 
        "👋 Добро пожаловать!\n\nВыберите модель ножа:", 
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda message: message.text == "🔪 Афалина")
def afalina(message):
    text = """🔪 **Афалина** — сила океана в твоей ладони

📏 **Характеристики:**
• Длина общая: 240 мм
• Длина клинка: 105 мм
• Длина рукоятки: 135 мм
• Ширина клинка: 36 мм
• Толщина клинка: 3.5-3.8 мм
• Вес: 144-148 г
• Производство: Россия

Выберите вариант исполнения:"""
    bot.send_message(message.chat.id, text, reply_markup=variant_menu(), parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "📐 Вектор")
def vector(message):
    text = """📐 **Вектор** — ясность цели и прорыв

📏 **Характеристики:**
• Длина общая: 235 мм
• Длина клинка: 100 мм
• Длина рукоятки: 135 мм
• Ширина клинка: 28 мм
• Толщина клинка: 3.5-3.8 мм
• Вес: 133-140 г
• Производство: Россия

Выберите вариант исполнения:"""
    bot.send_message(message.chat.id, text, reply_markup=variant_menu(), parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "🐂 Таурус")
def taurus(message):
    text = """🐂 **Таурус** — неукротимая сила в твоей руке

📏 **Характеристики:**
• Длина общая: 213 мм
• Длина клинка: 95 мм
• Длина рукоятки: 122 мм
• Ширина клинка: 34 мм
• Толщина клинка: 3.2 мм
• Вес: 124-131 г
• Производство: Россия

Выберите вариант исполнения:"""
    bot.send_message(message.chat.id, text, reply_markup=variant_menu(), parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "⚖️ Баланс")
def balance(message):
    text = """⚖️ **Баланс** — точка равновесия между формой и функцией

📏 **Характеристики:**
• Длина общая: 213 мм
• Длина клинка: 93 мм
• Длина рукоятки: 123 мм
• Ширина клинка: 26 мм
• Толщина клинка: 4 мм
• Вес: 123-140 г
• Производство: Россия

Выберите вариант исполнения:"""
    bot.send_message(message.chat.id, text, reply_markup=variant_menu(), parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "🏛️ Рубикон")
def rubicon(message):
    text = """🏛️ **Рубикон** — решимость для лидеров, меняющих правила

📏 **Характеристики:**
• Длина общая: 207 мм
• Длина клинка: 90 мм
• Длина рукоятки: 120 мм
• Ширина клинка: 30 мм
• Толщина клинка: 3.2 мм
• Вес: 101-127 г
• Производство: Россия

Выберите вариант исполнения:"""
    bot.send_message(message.chat.id, text, reply_markup=variant_menu(), parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "🌸 Ирис")
def iris(message):
    text = """🌸 **Ирис** — французское изящество и самурайская стойкость

📏 **Характеристики:**
• Длина общая: 203 мм
• Длина клинка: 89 мм
• Длина рукоятки: 114 мм
• Ширина клинка: 26 мм
• Толщина клинка: 3.2 мм
• Вес: 96-120 г
• Производство: Россия

Выберите вариант исполнения:"""
    bot.send_message(message.chat.id, text, reply_markup=variant_menu(), parse_mode="Markdown")

# Обработка выбора варианта
@bot.message_handler(func=lambda message: message.text in ["💎 Премиум", "⭐ Оптимальный", "✅ Базовый"])
def choose_variant(message):
    if message.text == "💎 Премиум":
        response = "💎 Премиум комплектация:\n• Лучшая сталь\n• Эксклюзивное покрытие\n• Подарочная упаковка\n\nСсылка для заказа: https://example.com/premium"
    elif message.text == "⭐ Оптимальный":
        response = "⭐ Оптимальный комплектация:\n• Отличная сталь\n• Классическое покрытие\n• Стандартная упаковка\n\nСсылка для заказа: https://example.com/optimal"
    else:
        response = "✅ Базовый комплектация:\n• Надежная сталь\n• Базовое покрытие\n• Простая упаковка\n\nСсылка для заказа: https://example.com/base"
    
    bot.send_message(message.chat.id, response)

@bot.message_handler(func=lambda message: message.text == "🔙 Назад в меню")
def back_to_menu(message):
    bot.send_message(message.chat.id, "Выберите модель ножа:", reply_markup=main_menu())

# Эхо для остальных сообщений
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "Используйте кнопки меню для навигации.")

print("🚀 Бот запущен...")
bot.infinity_polling()
