import sys

import telebot

from uuid import UUID
from dotenv import load_dotenv
import os

from telebot import types

load_dotenv()

API_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)
from loguru import logger

# Настройка логгера
logger.remove()  # Удаляем стандартный обработчик
logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")  # Логи в консоль
logger.add("test.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB")  # Логи в файл
# Словарь для хранения состояния пользователей
user_states = {}


# Обработчик команды /start
@logger.catch
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Пожалуйста, отправьте ссылку на XML-файл.")
    # print(find_offer_by_location(71.6919271, 40.4667725))

    # Инициализируем состояние пользователя для обработки URL
    user_states[message.from_user.id] = {'awaiting_feed_url': True}


if __name__ == "__main__":
    with logger.catch():
        bot.polling()
