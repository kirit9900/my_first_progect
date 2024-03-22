import telebot
import logging

TOKEN = "7008281820:AAFNrYB1m_OuuJs8qYJx4H0OYvM47vgNfic"
bot = telebot.TeleBot(TOKEN)

URL = 'http://localhost:1234/v1/chat/completions'
HEADERS = {"Content-Type": "application/json"}
MAX_LETTERS = 150
DB_NAME = 'db'
DB_TABLE_USERS_NAME = 'users'



