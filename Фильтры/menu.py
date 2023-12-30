from PIL.Image import Image
import pathlib
from filtres import FiltreRepo
from PIL import Image
def filtre_defenutinion(key:str,image:Image):
    print(repo[key]["name"])
    print(repo[key]["derict"])
    promt=input("Вы уверены что хотите применить этот фильтр?")
    while promt.lower()!= "да" or "нет":
        if promt.lower()=="нет":
            print("Фильтр не применен")
            break
        elif promt.lower() == "да":
            save_path = input("Введите путь куда вы хотите сохратить новое изображение(с именем и расширением):\n")
            repo[key]["instance"].apply(image).save(save_path)
            print("Фильтр успешно применен")
            break
        else:
            promt=input("Простите но вы чтото ввели неверно...попробуйте еще раз!")

repo=FiltreRepo().repo
def main_menu():
    print("Привет пользователь ты попал в фотошоп!")
    path=input("Введите путь до изображения (с именем и расширения файла):\n")
    while not pathlib.Path(path).exists():
        print("Простите но такого файла не существует,попробуйте еще раз!")
        path=input()
    image=Image.open(path).convert("RGB")

    print("\n\nМеню фильтров:")
    for key, values in repo.items():
        print(f"{key}-{values['name']}")
    print("Введите -1 для выхода")

    choice=input("Введите пункт меню:")
    while not(choice in repo or choice=="-1"):
        print("Такого пункта не существует,введите еще раз!")
        choice=input("Введите пунтк меню:")
    if choice in repo:
        filtre_defenutinion(choice,image)
        exit_mart=input("Хотите ли вы выйти из программы?Введите да или нет").lower()
        while exit_mart.lower() not in ["да","нет"]:
            print("Что то не так...Введите да или нет")
            exit_mart = input()
        if exit_mart=="да":
            print("Спасибо за работу")
            exit()
        else:
            print("Спасибо за работу")
            return -1
            exit()
    elif choice=="-1":
        print("Спасибо за работу")
        return -1
        exit()
while True:
    main_menu()
