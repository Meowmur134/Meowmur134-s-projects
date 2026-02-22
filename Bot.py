import random
import telebot
from telebot.types import ReactionTypeEmoji
import BotLogic
import os

    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("Token")
images = os.listdir('images')
ship_images = os.listdir('ship_images')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Команды: start, hello, help, gen_pass, reaction, coin, bye. Также эхо и изменения реакций")


@bot.message_handler(commands=["gen_pass"])
def send_pass(message):
    bot.reply_to(message, BotLogic.gen_pass())

# Send a reactions to all messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=["reaction"])
def send_reaction(message):
    emo = ["\U0001F525", "\U0001F917", "\U0001F60E"]  # or use ["🔥", "🤗", "😎"]
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)
@bot.message_reaction_handler(func=lambda message: True)
def get_reactions(message):
    bot.reply_to(message, f"You changed the reaction from {[r.emoji for r in message.old_reaction]} to {[r.emoji for r in message.new_reaction]}")

@bot.message_handler(commands=["coin"])
def send_coin(message):
    bot.reply_to(message, BotLogic.coin())
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=["photo"])
def send_photo(message):
    image = random.choice(images)
    with open(f'images/{image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["ship_photo"])
def send_photo(message):
    ship = random.choice(ship_images)
    with open(f'ship_images/{ship}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
     
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
print("Бот запущен")
bot.polling()
