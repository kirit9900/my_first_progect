import telebot

token="6963749795:AAHB4g-54ZuX89PJL25vbmBapQsGTpTdgXc"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['о себе'])
def start(message):
  bot.send_message(message.chat.id,"Привет,меня зовут Кирилл и я начинающий программист в Яндексе!Развлекаййся и не скучай!")
@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id,"Привет ✌️ Можешь нажать /help чтобы узнать что это за бот!")

@bot.message_handler(commands=['help'])
def help(message):
  bot.send_message(message.chat.id,"Привет друг!Вот что я умею"
                                   "1:Ты можешь сделать визитку"
                                   "2:Записать в нее свой номер телефона"
                                   "3:Написать свое хобби а также свой возрат и год рождения!"
                                    "4:/help-помощь"
                                    "5:/о себе-что это за бот и кто я вобще!")

def filter_password(message):
    password = "привет"
    return password in message.text.lower()

def pasxalka(message):
    passwodik="2008kir1703march"
    return passwodik in message.text.lower()

def filtre_passwordpoka(message):
    password1 = "пока"
    return password1 in message.text.lower()


@bot.message_handler(content_types=['text'], func = filter_password)
def say_hello(message):
      bot.send_message(message.chat.id, f"Привет!{message.from_user.first_name}")

@bot.message_handler(content_types=['text'], func = pasxalka())
def say_pasx(message):
      bot.send_message(message.chat.id, f"Привет{message.from_user.first_name}"
                                        f"Я не знаю кто ты,но ты где то нашел пасхалочку"
                                        f"Молодец!")

@bot.message_handler(content_types=['text'], func = filtre_passwordpoka)
def say_poka(message):
      bot.send_message(message.chat.id, f"Пока{message.from_user.first_name}")


@bot.message_handler(content_types=['text'])
def povtor(message):
    bot.send_message(message.chat.id, f"Привет привет!{message.from_user.first_name}")


bot.polling()