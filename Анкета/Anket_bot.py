import telebot
from Data import *
from telebot import types
from PIL import Image, ImageDraw, ImageFont
import sys

question1 = "Ты любишь свободу или безопастность?"
question2 = "Ты готов платить за технологии?"
question3 = "Тебе важна экосистема?"
question4 = "Готов ли ты защищать компанию?"
question5 = "Готов каждый год покупать новое устройство?"
question = {question1: ["Да", "Нет", "Незнаю"], question2: ["Да", "Нет", "Незнаю"], question3: ["Да", "Нет", "Незнаю"],question4: ["Да", "Нет", "Незнаю"],question5: ["Да", "Нет", "Незнаю"]}
score = [3, 1, 2]

TOKEN = "6908420457:AAFfoqmNGmNiup4JBCWixvZ179U_gwd4r7A"
bot = telebot.TeleBot(TOKEN)
data_path = "users.json"
user_data = load_user_data(data_path)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,"""
    Привет пользователь\n
    Это моя анкета :андроид против айфон"\n
    Если хочешь начать нажми (/start)""")
@bot.message_handler(commands=["start"])
def one(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    btn3 = types.KeyboardButton("Незнаю")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Ты попал на тестирование ты за айфон или за андроид!", reply_markup=markup)
    start(message, data_path)
    msg = bot.reply_to(message, question1)
    bot.register_next_step_handler(msg, next)


def next(message):
    data = load_user_data(data_path)
    if message.text in question[question1]:
        data[message.chat.username]["value"] += score[question[question1].index(message.text)]
        save_user_data(data, data_path)
    else:
        bot.send_message(message.chat.id, "Ты ввел не верный ответ")
    msg = bot.reply_to(message, question2)
    bot.register_next_step_handler(msg, next2)


def next2(message):
    data = load_user_data(data_path)
    if message.text in question[question2]:
        data[message.chat.username]["value"] += score[question[question2].index(message.text)]
        save_user_data(data, data_path)
    else:
        bot.send_message(message.chat.id, "Ты ввел не верный ответ")
    msg = bot.reply_to(message, question3)
    bot.register_next_step_handler(msg, next3)


def next3(message):
    data = load_user_data(data_path)
    if message.text in question[question1]:
        data[message.chat.username]["value"] += score[question[question1].index(message.text)]
        save_user_data(data, data_path)
    else:
        bot.send_message(message.chat.id, "Ты ввел не верный ответ")
    msg = bot.reply_to(message, question4)
    bot.register_next_step_handler(msg, next4)
def next4(message):
    data = load_user_data(data_path)
    if message.text in question[question1]:
        data[message.chat.username]["value"] += score[question[question1].index(message.text)]
        save_user_data(data, data_path)
    else:
        bot.send_message(message.chat.id, "Ты ввел не верный ответ")
    msg = bot.reply_to(message, question5)
    bot.register_next_step_handler(msg, next5)
def next5(message):
    data = load_user_data(data_path)
    if message.text in question[question1]:
        data[message.chat.username]["value"] += score[question[question1].index(message.text)]
        save_user_data(data, data_path)
    else:
        bot.send_message(message.chat.id, "Ты ввел не верный ответ")
    ex(message)
def ex(message):
    data = load_user_data(data_path)
    bot.send_message(message.chat.id, f"{data[message.chat.username]['value']} очков")
    if 7<= data[message.chat.username]["value"] <= 15:
        bot.send_message(message.chat.id, "Ты за айфон,дружище!")
        img = Image.open('-cons6.jpg')
        d1 = ImageDraw.Draw(img)
        MyFont = ImageFont.truetype('verdana.ttf', 100)
        d1.text((255, 100), f"{data[message.chat.username]['value']} очков\n Ты за айфон", fill = (255, 0, 0), font = MyFont)
        bot.send_photo(message.chat.id,img)

    if data[message.chat.username]["value"] < 7:
        bot.send_message(message.chat.id, "Ты за андроид")
        img = Image.open('-cons6.jpg')
        d1 = ImageDraw.Draw(img)
        MyFont = ImageFont.truetype('verdana.ttf', 100)
        d1.text((255, 100), f"{data[message.chat.username]['value']} очков\n Ты за андроид", fill=(255, 0, 0),font=MyFont)
        bot.send_photo(message.chat.id, img)







bot.polling()