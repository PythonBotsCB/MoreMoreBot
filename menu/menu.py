from config import *
from constants import *
from users import *

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.dispatcher.filters import Text

@dp.message_handler(lambda message: message.text.split()[-1] == 'menu')
async def show_menu(message:types.Message) -> None:
    try:
        counter = 1
        while True:
            await bot.delete_message(message.chat.id, message.message_id - counter)
            counter += 1

    except Exception as ex:
        pass
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("Икра и крабы🔥", callback_data='1'),
        InlineKeyboardButton("Морепродукты🔥", callback_data='2'),
        InlineKeyboardButton("Консервы🔥", callback_data='3'),
        InlineKeyboardButton("Рыбка слабосоленая и копченая🔥", callback_data='4'),
        InlineKeyboardButton("Филе и стейки🔥", callback_data='5'),
        InlineKeyboardButton("Рыба свежемороженная и охлажденная🔥", callback_data='6'),
        InlineKeyboardButton("Рыбка вяленая🔥", callback_data='7'),
        InlineKeyboardButton("Полуфабрикаты🔥", callback_data='8'),
        InlineKeyboardButton("Бады и Витамины🔥", callback_data='9'),
    ]
    keyboard.add(*buttons)
    await bot.delete_message(message.chat.id, message.message_id)
    await message.answer_photo("AgACAgIAAxkBAAIdi2V102HVeNqE9zIWneJKvbkQWUTCAAKO1zEbKbmoSxmAe5MDhD7SAQADAgADcwADMwQ", reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: True)
async def check(callback_query: types.CallbackQuery) -> None:
    if callback_query.data == '1':
        await crabs(callback_query)
    elif callback_query.data == '2':
        await seaproducts(callback_query)
    elif callback_query.data == '3':
        await canned_food(callback_query)
    elif callback_query.data == '4':
        await salt_fish(callback_query)
    elif callback_query.data == '5':
        await steaks(callback_query)
    elif callback_query.data == '6':
        await sm_fish(callback_query)
    elif callback_query.data == '7':
        await dried_fish(callback_query)
    elif callback_query.data == '8':
        await semi_fished_products(callback_query)
    elif callback_query.data == '9':
        await vitamins(callback_query)
    elif callback_query.data == 'back':
        await goback(callback_query)
    print(callback_query.data)
async def delete_previous_message(message:Message) -> None:
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except Exception as ex:
        pass

@dp.callback_query_handler(lambda callback_query: callback_query.data == '1')
async def crabs(callback_query: types.CallbackQuery) -> None:
    ''' меню из икры и крабов '''


    message = callback_query.message
    await delete_previous_message(message)
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🐟Икра красная (5000₽)', url='https://t.me/more_and_morebot?start=22'),
        InlineKeyboardButton('🐟Икра Восточный берег (750₽)', url='https://t.me/more_and_morebot?start=24'),
        InlineKeyboardButton('🦀Краб камчатский (фаланги) (3500₽)', url='https://t.me/more_and_morebot?start=16'),
        InlineKeyboardButton('🦀Краб стригун опилио (1200₽)', url='https://t.me/more_and_morebot?start=23'),
        InlineKeyboardButton('🦀Мясо камчатского краба (3100₽)', url='https://t.me/more_and_morebot?start=6'),
        InlineKeyboardButton('🦀Краб Камчатский, коленца (2000₽)', url='https://t.me/more_and_morebot?start=26'),
        InlineKeyboardButton('◀️Вернуться в меню', callback_data='back'),
    ]
    keyboard.add(*buttons)
    await message.answer("Икра и крабы🔥", reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '2')
async def seaproducts(callback_query: types.CallbackQuery) -> None:
    ''' меню из морепродуктов '''
    message = callback_query.message
    await delete_previous_message(message)
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🦐Креветка Аргентинская (550₽)', url='https://t.me/more_and_morebot?start=9'),
        InlineKeyboardButton('🦐Креветка Аргентинская очищенная (1200₽)', url='https://t.me/more_and_morebot?start=27'),
        InlineKeyboardButton('🦐Лангустин Аргентина (850₽)', url='https://t.me/more_and_morebot?start=28'),
        InlineKeyboardButton('🐟Клемы Вонголе (300₽)', url='https://t.me/more_and_morebot?start=52'),
        InlineKeyboardButton('🐟Морской коктейль (300₽)', url='https://t.me/more_and_morebot?start=53'),
        InlineKeyboardButton('🐟Гребешок северокурильский (1900₽)', url='https://t.me/more_and_morebot?start=15'),
        InlineKeyboardButton('🐟Гребешок крупный медальон (600₽)', url='https://t.me/more_and_morebot?start=54'),
        InlineKeyboardButton('🐟Мясо мидии (540₽)', url='https://t.me/more_and_morebot?start=18'),
        InlineKeyboardButton('🐟Мидии в створках (420₽)', url='https://t.me/more_and_morebot?start=7'),
        InlineKeyboardButton('◀️Вернуться в меню', callback_data='back'),
    ]
    keyboard.add(*buttons)
    await message.answer("Морепродукты🔥", reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '3')
async def canned_food(callback_query: types.CallbackQuery) -> None:
    ''' меню из консерв '''

    message = callback_query.message
    await delete_previous_message(message)
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🐟Барабулька-султанка (210₽)', url='https://t.me/more_and_morebot?start=55'),
        InlineKeyboardButton('🐟Печень трески (300₽)', url='https://t.me/more_and_morebot?start=10'),
        InlineKeyboardButton('◀️Вернуться в меню', callback_data='back'),
    ]
    keyboard.add(*buttons)
    await message.answer("Консервы🔥", reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '4')
async def salt_fish(callback_query: types.CallbackQuery) -> None:
    ''' меню из соленой и копченой рыбы '''

    message = callback_query.message
    await delete_previous_message(message)
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🐟Сёмга слабосоленая (2500₽)', url='https://t.me/more_and_morebot?start=56'),
        InlineKeyboardButton('🐟Сёмга слабосоленая нарезка (2500₽)', url='https://t.me/more_and_morebot?start=57'),
        InlineKeyboardButton('🐟Форель слабосоленая филе пласт (1600₽)', url='https://t.me/more_and_morebot?start=58'),
        InlineKeyboardButton('🐟Форель слабосоленая филе на подложке (590₽)',
                             url='https://t.me/more_and_morebot?start=59'),
        InlineKeyboardButton('🐟Форель слабосоленая нарезка (300₽)', url='https://t.me/more_and_morebot?start=60'),
        InlineKeyboardButton('🐟Форель тушка холодного копчения (990₽)', url='https://t.me/more_and_morebot?start=61'),
        InlineKeyboardButton('🐟Селёдочка слабосоленая (195₽)', url='https://t.me/more_and_morebot?start=62'),
        InlineKeyboardButton('🐟Филе сельди слабосоленной (85₽)', url='https://t.me/more_and_morebot?start=63'),
        InlineKeyboardButton('🐟Скумбрия холодного копчения (400₽)', url='https://t.me/more_and_morebot?start=64'),
        InlineKeyboardButton('🐟Кипперс из Скумбрии холодного копчения в чесночном соусе (650₽)',
                             url='https://t.me/more_and_morebot?start=65'),
        InlineKeyboardButton('🐟Сельдь холодного копчения (220₽)', url='https://t.me/more_and_morebot?start=66'),
        InlineKeyboardButton('🐟 Тёша форели холодного копчения (1100₽)', url='https://t.me/more_and_morebot?start=67'),
        InlineKeyboardButton('◀️Вернуться в меню', callback_data='back'),

    ]
    keyboard.add(*buttons)
    await message.answer("Рыбка слабосоленая и копченая🔥", reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '5')
async def steaks(callback_query: types.CallbackQuery) -> None:
    ''' меню из филе и стейов '''

    message = callback_query.message
    await delete_previous_message(message)
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🐟Стейк лосося (1500₽)', url='https://t.me/more_and_morebot?start=14'),
        InlineKeyboardButton('🐟Стейк чилийской форели (1200₽)', url='https://t.me/more_and_morebot?start=29'),
        InlineKeyboardButton('🐟Стейк тунца (880₽)', url='https://t.me/more_and_morebot?start=17'),
        InlineKeyboardButton('🐟Филе лосося (1800₽)', url='https://t.me/more_and_morebot?start=21'),
        InlineKeyboardButton('🐟Филе лосося Чили (1990₽)', url='https://t.me/more_and_morebot?start=30'),
        InlineKeyboardButton('🐟Филе форели Чили (1440₽)', url='https://t.me/more_and_morebot?start=31'),
        InlineKeyboardButton('🐟Филе форели Турция (1230₽)', url='https://t.me/more_and_morebot?start=68'),
        InlineKeyboardButton('🐟Филе горбуши (490₽)', url='https://t.me/more_and_morebot?start=20'),
        InlineKeyboardButton('🐟Филе атлантической трески (700₽)', url='https://t.me/more_and_morebot?start=32'),
        InlineKeyboardButton('🐟Филе судака (770₽)', url='https://t.me/more_and_morebot?start=33'),
        InlineKeyboardButton('🐟Филе минтая (270₽)', url='https://t.me/more_and_morebot?start=11'),
        InlineKeyboardButton('🐟Филе морского языка (325₽)', url='https://t.me/more_and_morebot?start=34'),
        InlineKeyboardButton('🐟Филе тилапии (450₽)', url='https://t.me/more_and_morebot?start=35'),
        InlineKeyboardButton('◀️Вернуться в меню', callback_data='back'),
    ]
    keyboard.add(*buttons)
    await message.answer("Филе и стейки🔥", reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '6')
async def sm_fish(callback_query: types.CallbackQuery) -> None:
    ''' меню из рыбы свежемороженной и охлажденной '''

    message = callback_query.message
    await delete_previous_message(message)
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🐟Лосось потрошенный (тушка) (1600₽)', url='https://t.me/more_and_morebot?start=19'),
        InlineKeyboardButton('🐟Лосось Чилийский (1500₽)', url='https://t.me/more_and_morebot?start=36'),
        InlineKeyboardButton('🐟Форель Чилийская (1100₽)', url='https://t.me/more_and_morebot?start=37'),
        InlineKeyboardButton('🐟Горбуша (250₽)', url='https://t.me/more_and_morebot?start=38'),
        InlineKeyboardButton('🐟Сибас (650₽)', url='https://t.me/more_and_morebot?start=39'),
        InlineKeyboardButton('🐟Дорадо (590₽)', url='https://t.me/more_and_morebot?start=40'),
        InlineKeyboardButton('🐟Камбала Атлантическая (350₽)', url='https://t.me/more_and_morebot?start=41'),
        InlineKeyboardButton('🐟Окунь морской (600₽)', url='https://t.me/more_and_morebot?start=42'),
        InlineKeyboardButton('🐟Скумбрия (320₽)', url='https://t.me/more_and_morebot?start=43'),
        InlineKeyboardButton('🦑Кальмар Командорский (400₽)', url='https://t.me/more_and_morebot?start=69'),
        InlineKeyboardButton('◀️Вернуться в меню', callback_data='back'),
    ]
    keyboard.add(*buttons)
    await message.answer("Рыба свежемороженная и охлажденная🔥", reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '7')
async def dried_fish(callback_query: types.CallbackQuery) -> None:
    ''' меню из рыбы свежемороженной и охлажденной '''

    message = callback_query.message
    await delete_previous_message(message)
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🐟Корюшка вяленая (750₽)', url='https://t.me/more_and_morebot?start=4'),
        InlineKeyboardButton('🐟Камбала вяленая (700₽)', url='https://t.me/more_and_morebot?start=5'),
        InlineKeyboardButton('◀️Вернуться в меню', callback_data='back'),
    ]
    keyboard.add(*buttons)
    await message.answer("Рыбка вяленая🔥", reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '8')
async def semi_fished_products(callback_query: types.CallbackQuery) -> None:
    ''' меню из полуфабрикатов '''

    message = callback_query.message
    await delete_previous_message(message)
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🐟Котлеты из щуки (240₽)', url='https://t.me/more_and_morebot?start=44'),
        InlineKeyboardButton('🐟Котлеты из трески (240₽)', url='https://t.me/more_and_morebot?start=45'),
        InlineKeyboardButton('🐟Котлеты из черной трески (300₽)', url='https://t.me/more_and_morebot?start=46'),
        InlineKeyboardButton('🐟Котлеты лососевые (250₽)', url='https://t.me/more_and_morebot?start=47'),
        InlineKeyboardButton('🐟Котлеты из Сома (240₽)', url='https://t.me/more_and_morebot?start=70'),
        InlineKeyboardButton('🐟Котлеты из Судака (240₽)', url='https://t.me/more_and_morebot?start=71'),
        InlineKeyboardButton('🐟Пельмени лососевые (310₽)', url='https://t.me/more_and_morebot?start=48'),
        InlineKeyboardButton('🐟Пельмени из трески (275₽)', url='https://t.me/more_and_morebot?start=49'),
        InlineKeyboardButton('🐟Пельмени из щуки (275₽)', url='https://t.me/more_and_morebot?start=50'),
        InlineKeyboardButton('◀️Вернуться в меню', callback_data='back'),
    ]
    keyboard.add(*buttons)
    await message.answer("Полуфабрикаты🔥", reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '9')
async def vitamins(callback_query: types.CallbackQuery) -> None:
    ''' меню из бадов и витаминов '''


    message = callback_query.message
    await delete_previous_message(message)
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('Омега 3 160кап. (1700₽)', url='https://t.me/more_and_morebot?start=12'),
        InlineKeyboardButton('Омега 3 42кап. (550₽)', url='https://t.me/more_and_morebot?start=51'),
        InlineKeyboardButton('◀️Вернуться в меню', callback_data='back'),
    ]
    keyboard.add(*buttons)
    await message.answer("Бады и Витамины🔥", reply_markup=keyboard)

@dp.callback_query_handler(lambda query: query.data == 'back')
async def goback(callback_query: types.CallbackQuery) -> None:
    message = callback_query.message
    ''' возвращает к основному меню '''
    await show_menu(message)