from aiogram.types import *
import json
from users import *
from adding import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import *
from constants import *

@dp.message_handler(commands=['newadmin'], state=None)
async def addadmin(message: Message) -> None:
    if Admin().check_admin(message.chat.id):
        await message.answer('Введите айди пользователя\nЧтобы узнать айди пользователя воспользуйтесь ботом https://t.me/UserBotInfoBot')
        await AddAdminState.new_user.set()

    else:
        await message.answer('У вас нет прав!')


@dp.message_handler(state=AddAdminState.new_user)
async def creating_admin(message: Message, state: FSMContext) -> None:

    with open(f'{DB_PATH}admins.json', 'r', encoding=ENCODING) as file:
        admins = json.load(file)

    admins.append(int(message.text))

    with open(f'{DB_PATH}admins.json', 'w') as file:
        json.dump(admins, file, indent=4, ensure_ascii=False)

    await message.answer('Новый админ добавлен')
    await state.finish()