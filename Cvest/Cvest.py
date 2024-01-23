import json
import random
from Date import save_user_data, load_user_data, save_data
from telebot import types
import Consid
import telebot

bot = telebot.TeleBot(Consid.Token)
data_path = "data.json"
user_data = load_user_data(data_path)


@bot.message_handler(commands=["start"])
def handler(message):
    data = load_user_data(data_path)
    data[message.chat.username] = {"WinorFalse": ""}
    save_data(data, data_path)
    bot.send_message(message.chat.id, """Привет мой друг,ты попал на мой квест хоррор по смешарикам!
    Ты можешь посмотреть информацию в 
    """)
    cvestick(message)


def cvestick(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("К нюше")
    btn2 = types.KeyboardButton("К лосяшу")
    btn3 = types.KeyboardButton("К ежику")
    markup.add(btn1, btn2, btn3)
    msg = bot.send_message(message.chat.id, """
    Был темный вечер.Тихо ехал поезд.Я посмотрел в окно и увидел густой туман"
    Эх...Надеюсь меня встретят и засел дальше воткнул наушники в уши где играла музыка!
    Он не заметил как пролетел час и я приехали!
    Я с радостью выбегаю и сразу впадаю вступор.
    -Когда я садился в поезд Крош ему сказал что встретит меня...Но его нету!
    Оставалось самому идти!Но куда?""", reply_markup=markup)
    bot.register_next_step_handler(msg, opredel)


def opredel(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("К нюше")
    btn2 = types.KeyboardButton("К лосяшу")
    btn3 = types.KeyboardButton("К ежику")
    markup.add(btn1, btn2, btn3)
    if message.text == "К нюше":
        nusha(message)
    elif message.text=="К лосяшу":
        Loshay(message)
    elif message.text=="К ежику":
        eshik(message)
def eshik(message):
    bot.send_message(message.caht.id,"""
    Я подошел к дому Ежика,но свет не был включен!
    Или его нету дома или он спит-додумав решил покричать
    ЕЖИК Это Я КИСАРИК 
    Ты дома?
    тишина...
    Я постучался в дверь и попытался ее открыть и она с легкостью открылась...
    Заходя домой я увидел что все стены были разорваны цветы лежали на полу...
    Ежик....ты где...
    Тут же на тумбочке я нашел его дневник...
    Я решил чуть чуть прочитать его""")

def Loshay(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ждать")
    btn2 = types.KeyboardButton("Открыть")
    btn3 = types.KeyboardButton("Или через окно")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,"""
    Прийдя к лосяшу ты стучишься и кричишь:ЛОСЯШ ЭТО Я КИСАРИК ОТКРОЙ дверь
    Через пару минут минут тебя хватают в охапку и быстро заталкивают пыльную комнату
    Ты кашляешь примерно 10 минут пока не слышишь голос лосяша:
    -Это ты Кисарик?-недоверчиво спросил Лосяш
    ДА это я-зло ответил Лосяшу
    А кто еще?
    Что тут ВОБЩЕ ПРОИСХОДИТ ВОБЩЕ?
    Давай попозже у совуньи расскажу!
    Куда мы идем....
    Тут же не успев это сказал прозвучал громкий звук в дверь
    Открой Лосяш это я КОПАТЫЧ
    Тихо...-сказал мне Лосяш
    Давай откроем это же копатыч
    НЕ надо чуть ли не закричал Лосяш
    Давай подождем и тихо через окно уйдем только я винтовку возьму!
    Что делать тебе?
    """)
def Losh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ждать")
    btn2 = types.KeyboardButton("Открыть")
    btn3 = types.KeyboardButton("Через окно")
    markup.add(btn1, btn2, btn3)
    if message.text=="Ждать":
        msg=bot.send_message("""Мы ждем 20 минут и стуки стихают!"
                    Мы выходим и бежим со всех ног к совунье""")
        bot.register_next_step_handler(msg, sovunia2)
    elif message.text=="Открыть":
        bot.send_message("""Ты окрываешь дверь и на тебя налетает монстр ежик и кусает тебя"
                         Через 10 минут становишься таким же зомби!
                                        <Game Over>""")
    elif message.text=="Через окно":
        msg = bot.send_message("""Мы решили через окно!
        Мы тихо его открываем и вылезаем тихо тихо
        Отходим пару метров и бежим со всех ног к совунье!""")
        bot.register_next_step_handler(msg, sovunia2)
def sovunia2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, """Ты пришел к дому совуньи вместе с лосяшем""", reply_markup=markup)
    bot.send_message(message.chat.id, Consid.sovushkalosh1)
    bot.send_message(message.chat.id, Consid.sovushkalosh2)
    bot.send_message(message.chat.id, Consid.sovushka2)
    bot.send_message(message.chat.id, Consid.sovuskaeshik)
    bot.send_message(message.chat.id, Consid.sovuska3)
    msg = bot.send_message(message.chat.id, Consid.sovuskaotvar, reply_markup=markup)
    bot.register_next_step_handler(msg, handle_buttons)





def nusha(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("К нюше")
    btn2 = types.KeyboardButton("К лосяшу")
    btn3 = types.KeyboardButton("К ежику")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, """
    Ты подошел к домику.Света не было...
    Ты стучишься в дверь и кричишь:"Нюша,это я Кисарик"
    Ответа нету....
    Ты дергаешь ручку и дверь сама собой открывается!
    -Нюша....ты где?-кричищь на весь дом
    Тишина....
    Ты заходишь и видишь записку на столе:
    "Я не знаю что происходит но ко мне прибежал бараж и говорит что общий сбор у совуньи.Если ты мой друг идти к совунье если нет уходи!"
    -Ту ту ту что же делать...Надо идти к совунье!-прочитав записку решаешь ты""", reply_markup=markup)
    sovunia(message)


def sovunia(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, """Ты пришел к дому совуньи""", reply_markup=markup)
    bot.send_message(message.chat.id, Consid.sovushka)
    bot.send_message(message.chat.id, Consid.sovushka1)
    bot.send_message(message.chat.id, Consid.sovushka2)
    bot.send_message(message.chat.id, Consid.sovuskaeshik)
    bot.send_message(message.chat.id, Consid.sovuska3)
    msg = bot.send_message(message.chat.id, Consid.sovuskaotvar, reply_markup=markup)
    bot.register_next_step_handler(msg, handle_buttons)


def handle_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    markup.add(btn1, btn2)
    if message.text == "1":
        pin2(message)
    elif message.text == "2":
        gameover(message)


def pin2(message):
    bot.send_message(message.chat.id,
                     """Давайте на счет три:
                     Раз
                     Два
                     Три
                     Все выпили...
                     -Фу какая гадасть-сказал я
                     Но вдруг дверь упала и в дом вломились Огромные Ежик и Крош!\n
                     У них были красные глаза!
                     -Я заметил что лосяш сзади достает оружие
                     -Ребят,что делать?-шопотом спрашиваю я
                     -ВАЛИМ-кричит бараж.
                     -Тут началась неразбериха!
                     Прозвучали звуки стрельбу,крики,куськи в шею и звук разбитого окна!
                     Я смог каким то чудом вылететь на улицу и я со всех ног бегу к пину!""")
    pin(message)


def gameover(message):
    bot.send_message(message.chat.id, """
    Но вдруг дверь упала и в дом вломили Огромные Ежик и Крош!
    У них были красные глаза.\n
    -Я заметил что лосяш сзади достает оружие\n
    Ребят,что делать?-шопотом спрашиваю я\n
    ВАЛИМ-кричит бараж.\n
    Тут началась неразбериха!
    Прозвучали звуки стрельбу,крики,куськи в шею и звук разбитого окна!
    Тут я вылетаю на улицу и понимаю что на руке у меня укус\n
    Через 10 минут я ничего не понимаю и тут я бросаюсь на других...!""")
    bot.send_message(message.chat.id, "Game over")


def pin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("В красную")
    btn2 = types.KeyboardButton("В белую")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, """Ты бежишь со всех ног не оборачиваясь назад.\n
    В далеке я вижу его дом и пляж и самого пина смотревшего в окно.
    Напрягая последнии силы я добигаю и кричу ему:"Опусти лифт быстее"
    Он опусти но я не поднимаюсь,я жду.
    Сначала подбегает нюша с лосяшем и барашем!
    Потом Совунье и Кар-Карыч.
    Они кричат:"ПОДНИМАЙ"
    Я не мемлю,Поднимаю и вижу в далеке Ежика и Кроша разряренных!
    Мы залетаем к пину и закрывая дверь совунья говорит"Звони в правительство!Пускай спасают нас!"
    Он не мемлит подходит к компу и звонит куда то !
    Мы слышим звуки чего то бьющего.
    Через 30 минут он говорит:Ребят ктото должен поговорить просто я ничего не понимаю!
    Я подхожу и говорю:"Здравствуйте с кем имею честь говорить?
    -Александр Пупкин,представитесь тоже!
    -Томских Кисичь Вадимов!
    -Обьясните что у вас происходит!
    -У нас зомби,можете нас забрать отсюда-справшиваю я!
    -Да мы видим ваши кординаты,приготовстесь к эвакуации!Сколько и вас и есть зараженные?
    -Нас девять и нету зараженных!
    -Хорошо через 20 минут к вам прибудут!Будьте рядом с пляжем!
    Конец связи!""")
    bot.send_message(message.chat.id, """
    Я посмотрел на других и сказал:быстро руки ноги и собирите любые вещи которые тут есть!""")
    bot.send_message(message.chat.id, """
    Мы выглянули в окно.Никого не было ни слышно не видно!
    Прошло 20 минут...
    Мы все вышли из дома пина со всеми вещами которые бригодятся!""")
    bot.send_message(message.chat.id, """
    В далеке мы увидели две лодки одна красная другая синяя,но лосяш заподозрил чтото не ладное!
    Он сказал нам всем:Ребят а одна из лодок это походу какие то бандиты!
    И правда,у двоих не было одобначений и у двоих были маски!
    И что же нам делать?
    Надо решать 
    Я предлагаю самую тупую вещь выстрелить в одну из лодок и что будет то будет!""")
    msg = bot.send_message(message.chat.id, "В какую лодку будите стрелять?В красную или белую?", reply_markup=markup)
    bot.register_next_step_handler(msg, lodka)


def lodka(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("В красную")
    btn2 = types.KeyboardButton("В белую")
    markup.add(btn1, btn2)
    if message.text == "В белую":
        bad(message)
    elif message.text == "В красную":
        Good(message)


def Good(message):
    bot.send_message(message.chat.id, """
    Прицелься и бабах!Надеюсь я в правильную лодку попал...
    Через 5 минут к ним подплыла лодка и забрала всех!
    Хороший конец но дальше больше интересного но это будет другая история!
    """)
    exit()


def bad(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Через дом кроша")
    btn2 = types.KeyboardButton("Через дом совуньи")
    btn3 = types.KeyboardButton("Остаться")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, """
    Прицелься и бабах!Надеюсь я в правильную лодку попал...
    Через 5 минут к ним подплыла лодка и забрала все припасы
    Да это окозались воры подслушающие нас!
    Когда мы уплыли мы конечно попытались связаться еще раз с правительством но у нас не получилось!
    Мы остались на острове с этими монстрами....
    Подождите ребят у нас же есть поезд!
    Но он наверное ухал-сказал Кар Карыч!
    А вот этого я не знаю...
    Но мы можем попробывать!
    Но нам нужен план действия!
    Есть два пути:
    Через Дом ежика-кроша-дом браша
    Или через дом совуньи!
    А есть третий вариант просто попробывать еще раз связаться с правительством и все им обьяснить!""")
    msg=bot.send_message(message.chat.id,"""Что мы решаем?""", reply_markup=markup)
    bot.register_next_step_handler(msg, puti)



def puti(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Через дом кроша")
    btn2 = types.KeyboardButton("Через дом совуньи")
    btn3 = types.KeyboardButton("Остаться")
    markup.add(btn1, btn2, btn3)
    if message.text == "Через дом кроша":
        Crosh(message)
    elif message.text == "Через дом Совуньи":
        Sovusha(message)
    else:
        bot.send_message(message.chat.id, """
        Мы пошли к пину и проседели там 5 часов
        Потом мы услышали что очень близко были шаги очень громкие!
        Мы решили закрыться и подумали что они скоро уйдут
        Да не тут это было!
        Нас дерзжали в заперти примерно 5 суток без еды!
        Так что мы умерли!
        """)
        bot.send_message(message.chat.id, """
                                <GAME OVER>""")


def Crosh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("По стелсу")
    btn2 = types.KeyboardButton("Отвлечь")
    btn3 = types.KeyboardButton("Пролом")
    btn4 = types.KeyboardButton("Убить")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, """
    Ну так что пошли только окуратно!
    Прошло 20 минут....
    Мы прошли уже Дом Ежика и подходим к дому Кроша!-кричу громким шопотом!""")
    bot.send_message(message.chat.id, """
    Осталось чуть чуть хотел сказать я но замолчал
    Ребят...что нам делать...-очень очень тихо сказал я
    в 20 метрах передо мной стояли эти два монстра и кричали друг на друга...
    У нас есть выбор пройти по стелсу или отвечь их чем нибудь
    или просто на пролом!
    или зайти каркарычу за оружием прошлых лет и убить их!""", reply_markup=markup)
    msg=bot.send_message(message.chat.id,"Что ты решил?")
    bot.register_next_step_handler(msg, Boss)


def Boss(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("По тселсу")
    btn2 = types.KeyboardButton("Отвлечь")
    btn3 = types.KeyboardButton("Пролом")
    btn4 = types.KeyboardButton("Убить")
    markup.add(btn1, btn2, btn3, btn4)
    if message.text == "По тселсу":
        stelc(message)
    elif message.text == "Отвлечь":
        Otvlech(message)
    elif message.text == "prolom":
        Prolom(message)
    elif message.text=="Убить":
        Bay(message)
def stelc(message):
    a = random.randint(10, 100)
    b = random.randint(1, 8)
    if a >= 60:
        bot.send_message(message.chat.id, """Вы прекрасно тихонечко прошли сквозь них не потеряв никого!
                             Вы молодцы!
                             Прибавив темп мы увидели поезд зашли в нутрь и он оказался самоуправляемым
                             Кар-Карыч быстро разобрался с управлением и запусти его!
                             Мы уехали,но дальше будет еще интерестнее!
                              Ждите обнов!
                                Конец!\n""")
    elif a < 60:
        bot.send_message(message.chat.id, f"""
            Я и несколько товарищей смогли пройти сквозь монстров,но {b} товарищей не смогли пройти,
            Нас осталось {9 - b}
            Остальные и я прибавили темп и увидели поезд зашли в нутрь и он оказался самоуправляемым
            Кар-Карыч быстро разобрался с управлением и запусти его!
            Мы уехали,но дальше будет еще интерестнее!
            Ждите обнов
                    Конец!\n""")
def Otvlech(message):
    a = random.randint(10, 100)
    b = random.randint(1, 8)
    c = random.randint(4, 9)
    d = random.randint(5, 9)
    if a >= 40:
        bot.send_message(message.chat.id, """Мы прекрасно тихонечко отвлекли их не потеряв никого!
                             Мы молодцы!
                             Прибавив темп мы увидели поезд зашли в нутрь и он оказался самоуправляемым
                             Кар-Карыч быстро разобрался с управлением и запусти его!
                             Мы уехали,но дальше будет еще интерестнее!
                              Ждите обнов!
                              Конец!\n""")
    elif a < 40:
            bot.send_message(message.chat.id, f"""
            Я и несколько товарищей смогли отвлечь,но {b} товарищей не смогли пройти,
            Нас осталось {9 - b}
            Остальные и я прибавили темп и увидели поезд зашли в нутрь и он оказался самоуправляемым
            Кар-Карыч быстро разобрался с управлением и запусти его!
            Мы уехали,но дальше будет еще интерестнее!
            Ждите обнов,написано на главном экране поезда!
                                Конец\n""")
def Prolom(message):
    a = random.randint(10, 100)
    b = random.randint(1, 8)
    c = random.randint(4, 9)
    d = random.randint(5, 9)
    if a >= 40:
        bot.send_message(message.chat.id, """Мы прекрасно тихонечко отвлекли их не потеряв никого!
                             Мы молодцы!
                             Прибавив темп мы увидели поезд зашли в нутрь и он оказался самоуправляемым
                             Кар-Карыч быстро разобрался с управлением и запусти его!
                             Мы уехали,но дальше будет еще интерестнее!
                              Ждите обнов!
                              Конец\n""")
    elif a < 40 and 9-c!=0 and 9-c!=1:
            bot.send_message(message.chat.id, f"""
            Я и несколько товарищей смогли отвлечь сквозь монстров,но {c} товарищей не смогли пройти,
            Нас осталось {9 - c}
            Остальные и я прибавили темп и увидели поезд 
            Когда зашли в нутрь и он оказался самоуправляемым
            Кар-Карыч быстро разобрался с управлением и запусти его!
            Мы уехали,но дальше будет еще интерестнее!
            Ждите обнов,написано на главном экране поезда!""")
    elif a < 40 and 9-c==0:
            bot.send_message(message.chat.id, f"""
            Мы не смогли пройти на пролом нас всех сьели!
                            <GAME OVER>""")
    elif a < 40 and 9-c==1:
            bot.send_message(message.chat.id, """
            Я остался один
            Я со всех ног бегу на поезд
            Мой андруналин помог мне разобраться с поездом и я уехал от сюда!
            Ждите обнов""")
def Bay(message):
    a = random.randint(10, 100)
    b = random.randint(1, 8)
    c = random.randint(4, 9)
    d = random.randint(5, 9)
    if a >= 40:
        bot.send_message(message.chat.id, """Мы со всеми дошли до дома Кар-Карыча,взяли оружие и я лосяш,бараш и копатыч пошли их убивать!
            Мы убили их не потеряв никого!
            Мы молодцы!
            Прибавив темп мы зашли домой быстро забрали всех остальных и пошли на станцию!
            Мы увидели поезд зашли в нутрь и он оказался самоуправляемым
            Кар-Карыч быстро разобрался с управлением и запусти его!
                             Мы уехали,но дальше будет еще интерестнее!
                              Ждите обнов!
                              Конец\n""")
    elif a < 40 and 4-d!=0 and 4-d!=1:
            bot.send_message(message.chat.id, f"""
            Мы со всеми дошли до дома Кар-Карыча,взяли оружие и я лосяш,бараш и копатыч пошли их убивать!,но {d} товарищей не смогли пройти,
            Нас осталось {9 - d}
            Остальные и я прибавили темп и увидели поезд зашли в нутрь и он оказался самоуправляемым
            Кар-Карыч быстро разобрался с управлением и запусти его!
            Мы уехали,но дальше будет еще интерестнее!
            Ждите обнов,написано на главном экране поезда!
                            Конец\n""")
    elif a < 40 and 4-d==1:
            bot.send_message(message.chat.id, """
            Я остался один,убив кроша я бегу в дом и Кричу Быстро к поезду!
            Я и остальные со всех ног бежым на поезд
            Мой андруналин помог мне разобраться с поездом и мы уехали от сюда!
            Ждите обнов""")
    elif a < 40 and 4-d==0:
            bot.send_message(message.chat.id, f"""
            Мы не смогли убить их
            Нас всех сьели!
                            <GAME OVER>\n""")


def Sovusha(message):
    bot.send_message("""
    Мы тихо идем и видим в далеке монстров!
    Мы не сговариваясь ускоряемся и через 20 минут видим станцию и ...ПОЕЗД
    Мы бежим как наруто 
    Когда зашли в нутрь и он оказался самоуправляемым
    Кар-Карыч быстро разобрался с управлением и запусти его!
    Мы уехали,но дальше будет еще интерестнее!
    Ждите обнов,написано на главном экране поезда!
                            Конец\n""")


bot.polling()
