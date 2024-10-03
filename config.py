#TODO: добавить всю конфигурацию бота
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '6695031105:AAHQn5va-i_1SnuDU7s6ndYo4fTBhm9vyMQ'
storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

def get_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        KeyboardButton('/newcard'),
        KeyboardButton('/newadmin'),
        KeyboardButton('Меню'),
    ]
    keyboard.add(*buttons)

    return keyboard

def get_user_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        KeyboardButton('Меню'),
    ]
    keyboard.add(*buttons)

    return keyboard
