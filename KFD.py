name=input("Введите свое имя")
artef=""
win=False
is_start=True
print("""Привет пользователь.Ты попал на квест,напиши:
1.начать
0.Выйти
""")
count=input()
while True:
    if count=="1":
        break
    elif count=="0":
        print("Ждем тебя в будущем....")
        exit()
is_start=True
print(f"""Привет {name}
      Ты попал в глухой лес
      у тебя есть выбор куда пойти
      или в горы или попросить помощи в домике на опушке леса!
      выбирай
      1)Горы
      2)В домик""")
count=input()
if count==1:
        print("""Ты прошел огромный путь по горам и впереди увидел замок
        Но уже ночь и у тебя выбор
        и есть две дороги(Хорошая,но долгая и небезопастная,но быстрая
        1)Остаться на ночь и подождать до утра и спокойно дойти по безопастной дороге
        2)Пойти ночью 
        3)Остаться на ночь,но пойти по второй дороге """)
        count=input()
        if count==1:
                win=True
                print("""Молодец,Ты дошел до замка """)
        elif count==2:
                print("Прости путник,но ты упал")
        elif count==3:
                print("Прости путник,но ты не успел уйти от оползня ")
        else:
                print("Нету такого варианта или ты ввел чтото ни то!")
elif count==2:
        print("""Ты пришел к домику и постучался
        тебе ответили милым голоском
        ты зашел и увидел красивую девушку
        она варила супчик
        она предложила тебе отведать его
        1)Сьешь его
        2)Нет,только спать
        """)
        count=input()
        if count==1:
                print("Этой девушкой была ведьма и в суп она положила зелье и ты не проснулся,когда она точила ножики :)")
        elif count==2:
                win=True
                print("""Ты спокойно уснул,но услышал как девушка точит ножи
                 посмотрев на нее ты не увидел белых волос,а увидел темные грязные волосы
                 окончательно проснувшкись ты нашел ножик и медленно подошел к ведьме и зарезал ее
                 после того как она умерла ты пошел дальше спать.....""")
        else:
                print("Нету такого варианта или что то ни то ввел!")
if win==True:
        print("Ты победил")
elif win==False:
        print("Ты проиграл")
print("Продолжение следует......")



