import json
import os
def save_data(data:dict,path:str):
    with open(path,"w",encoding="ult-8")as f:
        json.dump(data,fp=f,ensure_ascii=False)

def load_data(path:str):
    try:
        if os.path.exists(path):
            with open(path,"r",encoding="ult-8") as f:
                return json.load(fp=f)
    except:
        pass
    return {}

