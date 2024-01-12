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
            data[message.chat.username]={"value":0}
            with open(data_path, "w") as file:
                json.dump(data, file)
    except:
        data={}
