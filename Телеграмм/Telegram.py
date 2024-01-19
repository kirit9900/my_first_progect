import telebot
import info
token="6963749795:AAHB4g-54ZuX89PJL25vbmBapQsGTpTdgXc"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['about','инфа'])
def start(message):
  bot.send_message(message.chat.id,"Привет,меня зовут Кирилл и я начинающий программист в Яндексе!Развлекайся и не скучай!")
@bot.message_handler(commands=['start','начало'])
def start(message):
  bot.send_message(message.chat.id,"Привет ✌️ Можешь нажать /help чтобы узнать что это за бот!")

@bot.message_handler(commands=['help','помощь'])
def help(message):
    bot.send_message(message.chat.id,"""Привет друг!Вот что я умею:\n
                                   1:Тут представлены везитки песонажей\n
                                   2:Посмотреть хобби персонажей,а также их возрат и год рождения!\n
                                   3:/help-помощь\n"
                                   4:/about-что это за бот и кто я вобще!\n
                                   5:/chosh-информация про кроша\n
                                   6:/nusha-информация про нюшу\n
                                   7:/pin-информация про пина\n
                                   8:/eashik-инфа про ежика\n
                                   9:/egikmusic-музыка ежика\n
                                   10:pinmusic-музыка пина\n
                                   11:musiccrosh-музыка кроша\n
                                   12:musicnusha-музыка нюши\n
                                   10:Есть разлисные команды с музыкой,бот включит тебе песню,какого либо персонажа!:)\n
                                    "также в скором будущем добавим новых персонажей!""")

@bot.message_handler(commands=['crosh'])
def info_chosh(message):
    bot.send_message(message.chat.id,info.About_info_chrosh)
    bot.send_message(message.chat.id,info.other)
    bot.send_message(message.chat.id,info.Favorite_Phrase)
    bot.send_photo(message.chat.id,'https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fscontent-hel3-1.cdninstagram.com%2Fv%2Ft51.2885-15%2Fe35%2F49858648_750542605319633_8542686157698251756_n.jpg%3F_nc_ht%3Dscontent-hel3-1.cdninstagram.com%26_nc_cat%3D105%26_nc_ohc%3DrqKFJLw43HsAX8PYQpK%26edm%3DAABBvjUBAAAA%26ccb%3D7-4%26oh%3D79492c18d2f63c5945a64d9f7a76a5fe%26oe%3D612AB4FA%26_nc_sid%3D83d603&lr=117119&pos=14&rpt=simage&text=крош%20фото')

@bot.message_handler(commands=['nusha'])
def info_chosh(message):
    bot.send_message(message.chat.id,info.About_info_nusha)
    bot.send_message(message.chat.id,info.other_nusha)
    bot.send_message(message.chat.id,info.Favorite_Phrase_nusha)
    bot.send_photo(message.chat.id,'https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fwww.zastavki.com%2Fpictures%2F2560x1600%2F2014%2FCartoons_Nyusha_princess_in_the_cartoon_Kikoriki_085688_19.jpg&lr=117119&pos=14&rpt=simage&text=нюша%20смешарики')

@bot.message_handler(commands=['pin'])
def info_chosh(message):
    bot.send_message(message.chat.id,info.About_info_nusha)
    bot.send_message(message.chat.id,info.other_nusha)
    bot.send_message(message.chat.id,info.Favorite_Phrase_nusha)
    bot.send_photo(message.chat.id, 'https://images.iptv.rt.ru/images/c6uepfjir4ssllu00krg.jpg')

@bot.message_handler(commands=['eashik'])
def info_chosh(message):
    bot.send_message(message.chat.id,info.About_info_Egik)
    bot.send_message(message.chat.id,info.other_egik)
    bot.send_message(message.chat.id,info.Favorite_Phrase_ekig)
    bot.send_photo(message.chat.id, 'http://thumbs.dfs.ivi.ru/storage23/contents/0/7/8344711cba6ccd9199da1d7b16e8a3.jpg')


def filter_password(message):
    password = "привет"
    return password in message.text.lower()

def pasxalka(message):
    passwodik="2008kir1703march"
    return passwodik in message.text.lower()

def filtre_passwordpoka(message):
    password1 = "пока"
    return password1 in message.text.lower()
@bot.message_handler(commands=['egikmusic'])
def say_hello(message):
    audio=open(r'C:\Основные проекты\Smeshariki_-_Da_Net_74725100.mp3','rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()
    video = open('C:\Основные проекты\smesariki-kros-jik-da-net-prem-era-klipa-2022_(VIDEOMIN.NET).mp4', 'rb')
    bot.send_video(message.chat.id, video)
@bot.message_handler(commands=['pinmusic'])
def say_hello(message):
    audio=open(r'C:\Основные проекты\Smeshariki_-_PinKod_76934185.mp3','rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()
    video = open('C:\Основные проекты\882949802639.mp4', 'rb')
    bot.send_video(message.chat.id, video)

def say_hello(message):
      bot.send_message(message.chat.id, f"Привет!{message.from_user.first_name}")

@bot.message_handler(content_types=['text'], func = pasxalka)
def say_pasx(message):
      bot.send_message(message.chat.id, f"Привет{message.from_user.first_name}"
                                        f"Я не знаю кто ты,но ты где то нашел пасхалочку"
                                        f"Молодец!")

@bot.message_handler(content_types=['text'], func = filtre_passwordpoka)
def say_poka(message):
      bot.send_message(message.chat.id, f"Пока{message.from_user.first_name}")

@bot.message_handler(commands=['musiccrosh'])
def musick_ckrosh(message):
        audio = open(r'C:\Основные проекты\Противоположности (Remix) (256  kbps).mp3','rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        audio=open(r'C:\Основные проекты\Smeshariki_-_OMSK_Phonk_75371957.mp3','rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        video = open('C:\Основные проекты\cernoe-ne-beloe-pesni-smesarikov-smesariki-2d-pesenki-dlya-detey_(VIDEOMIN.NET).mp4','rb')
        bot.send_video(message.chat.id, video)

@bot.message_handler(commands = ['musicnusha'])
def musick_ckrosh(message):
        audio = open(r'C:\Основные проекты\Smeshariki_-_Plyus_7_minus_7_76934192.mp3','rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        video = open('C:\Основные проекты\multklipi-pesni-smesarikov-plyus-sem-minus-sem_(VIDEOMIN.NET).mp4','rb')
        bot.send_video(message.chat.id, video)


@bot.message_handler(content_types=['text'])
def povtor(message):
    bot.send_message(message.chat.id, f"Привет привет!{message.from_user.first_name},у тебя введено что то не верно!Попробуй команду /help.")




bot.polling()