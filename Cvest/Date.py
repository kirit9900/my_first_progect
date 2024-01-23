import json
def load_user_data(data_path):
    try:
        with open(data_path,"r") as f:
            data=json.load(f)
    except:
        data={}
    return data


def save_user_data(user_data, data_path):
    with open(data_path,"w") as f:
        json.dump(user_data,f)

def start(message,data_path):
    try:
        with open(data_path,"r") as f:
            data=json.load(f)
            data[message.chat.username]={"WinorFalse":""}
            with open(data_path, "w") as file:
                json.dump(data, file)
    except:
        data={}
def save_data(data: dict, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, fp=f, ensure_ascii=False)