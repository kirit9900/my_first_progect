from repesidoriu import load_data,save_data
import Consider
from sys import argv
import telebot
bot=telebot.TeleBot(Consider.Token)
inlineKeyboard=telebot.types.InlineKeyboardMarkup
inlineKeyboard.row_width=2
inlineKeyboard.add(telebot.types.InlineKeyboardButton("да",callback_data="cb_yes"),
                       telebot.types.InlineKeyboardButton("нет",callback_data="cb_no"))
@bot.register_message_handler(commands=["start"])
def handler(message):
    bot.send_message(message.chat.id,Consider.message_start)
@bot.register_message_handler(commands=["answer"])
def harler_answer(message):
    data=load_data("data.json")
    user_progres=data.setdefault(message.chat.id,0)
    bot.send_message(message.chat.id,Consider.Questions[str(user_progres)],reply_markup=inlineKeyboard)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    data=load_data(Consider.Path)
    user_progres=data.setdefault(call.message.chat.id,0)
    if user_progres<len(Consider.Questions)-1:
        if call.data=="cb_yes":
            data[call.message.chat.id]+=1
            bot.answer_callback_query(call.id,"Следующий вопрос...")
        elif call.data=="cb_no":
            data[call.message.chat.id] += 1
            bot.answer_callback_query(call.id, "Следующий вопрос...")


