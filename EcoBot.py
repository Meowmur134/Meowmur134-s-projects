import telebot
import os
import random

bot = telebot.TeleBot("Вставьте сюда свой токен")
eco_images = os.listdir("eco_images")

@bot.message_handler(commands=["ecoproblems"])
def send_photo(message):
    eco_image = random.choice(eco_images)
    if eco_image == "akkumulyator.jpg":
        bot.reply_to(message, "Автомобильные аккумуляторы разлагаются 500 лет")
    elif eco_image == "plastic.jpg":
        bot.reply_to(message, "Пластик разлагается от 100 до 500 лет")
    elif eco_image == "pokryshka.jpg":
        bot.reply_to(message, "Покрышки разлагаются от 100 до 150 лет")
    elif eco_image == "steklo.jpg":
        bot.reply_to(message, "Стекло разлагается дольше 1000 лет")
    elif eco_image == "zhvachka.jpg":
        bot.reply_to(message, "Жвачка разлагается от 30 до 50 лет")
    with open(f'eco_images/{eco_image}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

print("Бот запущен")

bot.polling()
