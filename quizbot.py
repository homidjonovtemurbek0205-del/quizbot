import os
import telebot

# Tokenni Environment Variables dan olish
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom! Men quiz botman. Savol berish uchun /quiz ni bosing."
    )

# Quiz komandasi
@bot.message_handler(commands=['quiz'])
def quiz(message):
    question = "O‘zbekiston poytaxti qaysi?"
    options = ["Toshkent", "Samarqand", "Buxoro"]

    bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type="quiz",
        correct_option_id=0,  # 0 -> Toshkent
        is_anonymous=False
    )

print("Bot ishga tushdi...")
bot.infinity_polling()
