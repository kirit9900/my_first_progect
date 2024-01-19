import telebot
import About_cristnam
TOKEN = "6823842273:AAGGI5wMNe0bPqVa1iGuQgl5IvThv5Z_WKU"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Привет,всем кто зашел на мой канал\nТут собраны все материалы по новому году!\n""Нажми /help чтобы узнать побольше!")
    bot.send_photo(message.chat.id,'https://thumbs.dreamstime.com/b/%D1%81%D1%87%D0%B0%D1%81%D1%82-%D0%B8%D0%B2%D1%8B%D0%B5-%D0%BF%D0%BE%D0%B7-%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D0%B5-%D1%8C%D0%BD%D0%B0%D1%8F-%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%BA%D0%B0-%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE-%D0%B3%D0%BE-%D0%B0-%D1%82%D0%B2%D0%BE%D1%80%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F-%D0%BF%D1%80%D0%B8-83504758.jpg')
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,"""
    Привет неизвестный незнакомец!Я Дед Мороз!\n
    Если ты зашел на мой телеграмм канала,то поздравляю\n
    Тут с помощью команды /аbout ты можешь узнать все про новый год!\n
    Также с помощью волшебства(/picture) я тебе покажу главные символы нового года и покажу себя!\n
    Если стало скучно могу показать подборку новогодних фильмов!(/Films)\n
    Музыка,пхпхп не проблема тут собран плейлист из всех новогодних хитов или просто популярных песен!(/music)\n
    P.S Тут также есть новогоднее поздравления от меня!(/congratulation)\n
    P.P.S Также есть пасхальное яйцо так что дагадайся что нужно написать и я тебе покажу сюрприз!\n""")
    bot.send_photo(message.chat.id,'https://infopovod.ru/wp-content/uploads/2023/01/jhbvtyvd76ygtvrcdtyguhj-scaled.jpg')
@bot.message_handler(commands=["about"])
def abouting(message):
    bot.send_message(message.chat.id,About_cristnam.info)
    bot.send_message(message.chat.id,About_cristnam.info2)
    bot.send_photo(message.chat.id,'https: // upload.wikimedia.org / wikipedia / commons / 0 / 06 / 1998._Марка_России_0476_hi.jpg')

@bot.message_handler(commands=["picture"])
def pict(message):
    bot.send_message(message.chat.id,"А вот и главный персонаж 2024 года!")
    bot.send_photo(message.chat.id,"https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_658881c656ee56315a5320e1_658881d256ee56315a532623/scale_1200")
    bot.send_photo(message.chat.id,"https://img4.rudalle.ru/images/0f/5a/d9/0f5ad9e1ec6a472c86a9bb1d76a5c0e6_00000.jpg")
@bot.message_handler(commands=["films"])
def films(message):
    bot.send_message(message.chat.id,"""
    Хо Хо Хо Вот тебе подборка новогодних фильмов на новогоднии каникулы и на зимнии вечера""")
    bot.send_message(message.chat.id,"""
    1:Один дома:(https://hd.8lordserial.pro/3015-odin-doma.html)\n
    2:Гринч:(https://disney-movie.ru/multfilm-2018-01/)\n
    3:Ирония судьбы или с легким паром:(https://231223.lordfilm4.black/7994-film-ironija-sudby-ili-s-legkim-parom-1975.html)\n
    4:Приключения Паддиктона:(https://www.kinopoisk.ru/film/463897/)\n
    5:Карнавальная ночь:(https://www.kinopoisk.ru/film/44720/)\n
    Не понравилась подборка тогда заходи сюда!
    https://www.kinopoisk.ru/lists/movies/newyear_mood/""")
@bot.message_handler(commands=["music"])
def mus(message):
    bot.send_message(message.chat.id,"""
    Едешь в путишествие?\n
    Тогда тебе сюда!""")
    bot.send_message(message.chat.id,"https://music.yandex.ru/users/newyearplaylists/playlists/1241")
    bot.send_message(message.chat.id,"""
    А вот лично мои любимые песни 
    1:https://music.yandex.ru/album/28744175/track/120487477
    2:https://music.yandex.ru/album/20252545/track/97919421
    3:https://music.yandex.ru/album/13049093/track/74603017""")
@bot.message_handler(commands=["congratulation"])
def cong(message):
    bot.send_message(message.chat.id,"А вот и мое поздравление!:")
    video = open("C:\Основные проекты\Поздравление от Деда Мороза с Новым Годом!.mp4", 'rb')
    bot.send_video(message.chat.id,video)

def mother(message):
    password = "мама"
    return password in message.text.lower()
@bot.message_handler(content_types=['text'], func = mother)
def morhers(message):
    bot.send_message(message.chat.id,"""
    Поздравляю я тебя 
    Мою мамочку любимую
    Хочу чтобы оставалась такой же красивой как всегда!""")
    bot.send_photo(message.chat.id,"https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fsun9-73.userapi.com%2Fimpg%2FOUf6DvN9MwvilUpzJjxVTusfZ9nTz1ZoZ9oEdg%2Ff9TeTw2nfjw.jpg%3Fsize%3D719x719%26quality%3D96%26sign%3D1fd703c33870f46fd538ad2c990bc4aa%26c_uniq_tag%3DRflJspWi7WqmF5E8t5jWNI7u0SAJDgRWWN9cArQCu40%26type%3Dalbum&lr=117119&pos=2&rpt=simage&text=с%20новым%202024%20годом%20картинки")
    video = open("C:\Основные проекты\_161510.mp4", 'rb')
    bot.send_video(message.chat.id, video)
def Yandex_practicum(message):
    passwordick="Yandex"
    return passwordick in message.text.lower()
@bot.message_handler(content_types=['text'], func = Yandex_practicum)
def yand(message):
    bot.send_photo(message.chat.id,"https: // pics.ru / wp - content / uploads / 2015 / 12 / 12380327_966957120041178_1855196609_n.jpg")

def green(message):
    passwords="green dracon"
    return passwords in message.text.lower()
@bot.message_handler(content_types=['text'], func = green)
def greendr(message):
    video=open("C:\Основные проекты\_161400.mp4",'rb')
    bot.send_video(message.chat.id,video)

bot.polling()

