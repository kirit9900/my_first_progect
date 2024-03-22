import io
from gptraya import *
from config import DB_NAME, DB_TABLE_USERS_NAME,TOKEN
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
import telebot
import gptraya
from data import *

# тестилось на модельке openchat_3.5-16k-Mistral-7B-Instruct-v0.2-slerp.Q5_K_S.gguf
# @ChatickGPTIXAbot-чат бот

bot = telebot.TeleBot(TOKEN)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logi.txt",
    filemode="w",
)
bot.set_my_commands([
    telebot.types.BotCommand('start', 'start'),
    telebot.types.BotCommand('help', 'help'),
    telebot.types.BotCommand('chatgpt', 'gpt'),
])


def create_keyboard(buttons_list):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*buttons_list)
    return keyboard
def user_check(message):
    user_id = message.chat.id
    (user_id, message.from_user.first_name)
    data = get_data_from_user(user_id)
    return data






@bot.message_handler(commands=['start', 'help'])
def start(message):
    logging.info("Отправка приветственного сообщения")
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Привет,{user_name}"
                                      f"Я твой бот психолог!"
                                      f"Ты можешь написать любую проблему и я помогу тебе разобраться"
                                      f"Если тебе и этого не хватит,то появится кнопка продолжить!"
                                      f"Если хочешь начать напиши  команду /chatgpt")
    user_exists(user_id=message.from_user.id)


@bot.message_handler(commands=['debug'])
def log(message):
    logging.getLogger().setLevel(logging.DEBUG)
    bot.send_message(message.chat.id, 'Режим отладки включен')
    try:
        with open('logi.txt', 'r') as file:
            logs = file.read()
    except FileNotFoundError:
        bot.reply_to(message, 'Файл не найден')
        return

    bot.send_document(message.chat.id, io.BytesIO(logs.encode()))

    if message.text != "log" or message.text != "start" or message.text != "chatgpt":
        bot.send_message(message.chat.id, text="Такой команды не существует.")

@bot.message_handler(commands=['chatgpt'])
def chatgpt(message):
    keyboard = create_keyboard(["Сложный ответ","Просто ответ"])
    bot.send_message(message.chat.id,"Выбери сложный ответ или просто ответ", reply_markup=keyboard)
    bot.register_next_step_handler(message, get_answer)
def get_answer(message):
    while message.text != "Сложный ответ" and message.text!= "Просто ответ":
        bot.send_message(message.chat.id, text="Введи ответ")
        bot.register_next_step_handler(message, chatgpt)
    if message.text == "Сложный ответ":
        update_row_values(message.user_id,'levels', 'сложный ответ')
        bot.register_next_step_handler(message, get_answer_object)
    elif message.text == "Просто ответ":
        update_row_values(message.chat.id,'levels', "просто ответ")
        bot.send_message(message.chat.id, "Введи предмет")
        bot.register_next_step_handler(message, get_answer_object)
def get_answer_object(message):
    keyboard = create_keyboard(["Математика", "Психология","Русский язык"])
    bot.send_message("Выбери математику или психологию или русский язык", reply_markup=keyboard)
    bot.register_next_step_handler(message, get_answer_object_2)
def get_answer_object_2(message):
    while message.text != "Математика" and message.text!= "Психология" and message.text!= "Русский язык":
        bot.send_message(message.chat.id, text="Введи предмет")
        bot.register_next_step_handler(message, get_answer_object)
    if message.text == "Математика":
        update_row_values(message.user_id,'subject', "math")
        bot.register_next_step_handler(message,problem)
    elif message.text == "Психология":
        update_row_values(message.user_id,'subject', "psychology")
        bot.register_next_step_handler(message, problem)
    elif message.text == "Русский язык":
        update_row_values(message.user_id,'subject', "russian")
        bot.register_next_step_handler(message, problem)
def problem(message):
    bot.send_message(message.chat.id, "Напиши твою проблему")
    logging.info("Отправка примера или задачи")


@bot.message_handler(content_types=["text"])
def dialog(message):
    gpt_dialog(message)


gpt = GPT(system_content="")


def gpt_dialog(message):
    keyboard = create_keyboard(["конец", "продолжи"])
    json = gpt.make_promt(message.text)
    resp = gpt.send_request(json)
    response = gpt.process_resp(resp)
    bot.send_message(message.chat.id, response[1], reply_markup=keyboard)
    answer=response[1]
    update_gpt(message.user_id,answer)
    bot.register_next_step_handler(message, vubor)
    logging.info("Отправка ответа")


def vubor(message):
    user_id = message.chat.id
    data = user_check(message)
    if data["prompt_active"] == 1:
        if message.text == "конец":
            update_row_values(message.user_id,"prompt_active", 0)
            bot.send_message(message.chat.id, "Пока!")
            bot.send_message(message.chat.id, "Текущее решение завершено")
            bot.register_next_step_handler(message, start)
            logging.info("Конец")
            return
        while gpt.MAX_TOKENS < len(message.text):
            msg = bot.send_message(message.chat.id, "Ваш запрос слишком длинный!")
            bot.register_next_step_handler(msg, chatgpt)
        if message.text == "продолжи":
            json = gpt.make_promt(message.text)
            resp = gpt.send_request(json)
            response = gpt.process_resp(resp)
            bot.send_message(message.chat.id, response[1])
            bot.register_next_step_handler(message, vubor)
            logging.info("Продолжение")
    if not response[0]:
        bot.send_message(message.chat.id, text="Не удалось выполнить запрос...")
        logging.info(f"Ошибка: {response.status_code}")
    else:
        bot.send_message(message.chat.id, "Я тебя не понял!")

    def clear_log_file():
        with open("log_file.txt", "w") as file:
            file.write("")


bot.polling()
