import telebot

# Sizning bot tokeningiz
TOKEN = "8258584354:AAGlMeGvjNnWbQu7qNF6W3ukR9vhh3vtdcc"
bot = telebot.TeleBot(TOKEN)

# Boshlash komandasi
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom! Men quiz botman. Savol berishim uchun /quiz buyrug‘ini bosing."
    )

# Quiz komandasi
@bot.message_handler(commands=['quiz'])
def quiz(message):
    question = "O‘zbekiston poytaxti qaysi?"
    options = ["Toshkent", "Samarqand", "Buxoro", "Andijon"]

    bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type="quiz",
        correct_option_id=0,  # 0 -> "Toshkent" to‘g‘ri javob
        is_anonymous=False
    )

print("Bot ishga tushdi...")
bot.infinity_polling()
