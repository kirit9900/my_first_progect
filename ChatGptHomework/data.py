import logging
import os
import sqlite3
from config import DB_NAME,DB_TABLE_USERS_NAME


def create_db(database_name=DB_NAME):
    db_path=f'{database_name}'
    connection = sqlite3.connect(db_path)
    connection.close()
    logging.info(f'Database {db_path} created')
def execute_query(sql_query,data=None,db_path=f'{DB_NAME}'):
    logging.info(f'DATABASE:EXECUTE query:{sql_query}')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    if data:
        cursor.execute(sql_query,data)
    else:
        cursor.execute(sql_query)
    connection.commit()
    connection.close()
def execute_selection_query(sql_query,data=None,db_path=f'{DB_NAME}'):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    if data:
        cursor.execute(sql_query,data)
    else:
        cursor.execute(sql_query)
    rows = cursor.fetchall()
    connection.close()
    return rows
def create_table(table_name):
    sql_query = f'CREATE TABLE IF NOT EXISTS {table_name} ' \
                f'(id INTEGER PRIMARY KEY, ' \
                f'user_id INTEGER' \
                f'subject TEXT' \
                f'levels INTEGER' \
                f'task TEXT' \
                f'answer TEXT'\
                f'prompt_active INTEGER DEFAULT 0);'
    execute_query(sql_query)
def get_all_rows(table_name):
    rows = execute_selection_query(f'SELECT * FROM {table_name}')
    for row in rows:
        print(row)
def insert_row(values):
    columns='(user_id,subject,level,task,answer)'
    sql_query = f"INSERT INTO {DB_TABLE_USERS_NAME} {columns} VALUES (?,?,?,?,?)"
    execute_query(sql_query,values)
def is_value_in_table(table_name,column_name,value):
    sql_query = f'SELECT ? FROM ? WHERE ? = ? LIMIT1'
    rows = execute_selection_query(sql_query,[value])
    return any(rows) > 0
def update_row_values(user_id,column_name,new_value):
    if is_value_in_table(DB_TABLE_USERS_NAME,'user_id',user_id):
        sql_query = f'UPDATE {DB_TABLE_USERS_NAME} SET {column_name} = ? WHERE user_id = {user_id}'
        execute_query(sql_query,[new_value])
    else:
        logging.error(f'User with id {user_id} not found')
        print(f'User with id {user_id} not found')
def get_data_from_user(user_id):
    if is_value_in_table(DB_TABLE_USERS_NAME,'user_id',user_id):
        sql_query = f'SELECT user_id,subject,level,task,answer'\
                    f'FROM {DB_TABLE_USERS_NAME} WHERE user_id = LIMIT1'
        row = execute_selection_query(sql_query,[user_id][0])
        return {
            'subject':row[1],
            'levels':row[2],
            'task':row[3],
            'answer':row[4],
            "prompt_active": row[5]
        }
    else:
        logging.error(f'User with id={user_id} not found')
        print(f'User with id {user_id} not found')
        return {
            'user_id':'',
            'subject':'',
            'levels':'',
            'task':'',
            'answer':'',
            "prompt_active": 0
        }
def prepare_db(clean_if_exists=False):
    create_db()
    create_table(DB_TABLE_USERS_NAME)
    if clean_if_exists:
        execute_query({DB_TABLE_USERS_NAME})
def user_exists(self, user_id):
        if not self.is_value_in_table('user_id', user_id):
            logging.info(f"DATABASE: Пользователь с id = {user_id} не найден")
            insert_row(user_id)
            return True
        return False


    # обновление столбца в таблице users
def update_gpt(self, user_id, answer):
        data = get_data_from_user(user_id)
        answer2 = data["answer"] + answer
        update_row_values(user_id, "answer", answer2)
        logging.info(f"DATABASE: Answer updated")


    # очистка таблицы users
def clean_table(self):
        execute_query(f'DELETE FROM {DB_TABLE_USERS_NAME}')
        logging.info(f"DATABASE: Table cleaned")

if __name__ == '__main__':
    prepare_db(True)
    get_all_rows(DB_TABLE_USERS_NAME)



