import requests
import config
from data import *

class GPT:
    def __init__(self, system_content=""):
        self.assistant_content = "Решаем задачи по шагам:"

    def count_token(text):
        return len(text) // 2
    def process_resp(self, response,id,message,column_name,):
        try:
            full_response = response.json()
            if response.status_code != 200:
                self.save_history()
                logging.info(f"Ошибка: {response.status_code}")
            if "error" in full_response or 'choices' not in full_response:
                self.clear_history()
                return False, f"Ошибка: {full_response}"

            result = full_response['choices'][0]['message']['content']
            update_row_values(message.user_id,'task', "result")
            if result == "" or result is None:
                self.clear_history()
                return True, "Объяснение закончено"
        except:
            logging.info("Не удалось обработать ответ")
            return ("Не удалось обработать ответ")

        self.save_history(result,id)
        return True, self.assistant_content

    def make_promt(self, user_request, data):
        json = {
            "messages": [{"role": "system", "content": promts[data['subject']][data['level']]},
                {"role": "user", "content": user_request}, {"role": "assistant", "content": self.assistant_content},

            ], "temperature": 0.7, "max_tokens": config.MAX_LETTERS, }
        return json

    def send_request(self, json):
        response = requests.post(url=config.URL, json=json, headers=config.HEADERS)
        return response

    def save_history(self, content_response,id):
        self.assistant_content += content_response

    def clear_history(self):
        # Твой код ниже
        self.assistant_content = "Cейчас подумаем над твоей проблемой:"
promts = {
    "math": {
        "сложный ответ":"Ты учитель математики в МГУ и ведящий лекции!Если тебя спросят обьясни сложно!",
        "простой ответ":"Ты учитель математики пятых классов!Если тебя спросят обьясни по простому",
    },
    "psychology": {
        "сложный ответ":"Ты профессиональный психолог который ведет лекции везде и который берет за свои услуги 5000 рублей!Если тебя спросят обьясни сложно!",
        "простой ответ":"Ты психолог в школе!Если тебя спросят обьясни по простому",
    },
    "russian": {
        "сложный ответ":"Ты профессиональный переводчик на русский язык за границей помогающим даже президентам!Если тебя спросят обьясни сложно!",
        "простой ответ":"Ты учитель в школе пятых классов!Если тебя спросят обьясни по простому",
    }
}
