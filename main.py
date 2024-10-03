from finder import *
from adding import *
from users import *
from FSMCards import *
from FSMAdmins import *
from config import *
from menu.menu import *

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text


#TODO: Возможность добавления админов

@dp.message_handler(commands=['start'])
async def start(message:types.Message) -> None:
    id = (message.text.split()[-1])

    try:
        counter = 1
        while True:
            await bot.delete_message(message.chat.id, message.message_id - counter)
            counter += 1

    except Exception as ex:
        pass



    await bot.delete_message(message.chat.id, message.message_id)
    await findItem(id, message)


async def findItem(request, message) -> None:

    need_card = Requests(request).card

    if not isinstance(need_card, EmptyCard):

        message_text = f'<b>{need_card.data.get("name")}</b>\n{need_card.data.get("description")}\n\nДля заказа пишите\n@Fish_shop_NN\n\nViber, WhatsApp, позвонить \n8 (986) 766-99-31'

        keyboard_contacts = InlineKeyboardMarkup(row_width=1)

        buttons = [
            InlineKeyboardButton('Заказать📦', url='https://t.me/Fish_shop_NN?start=privet'),
            #InlineKeyboardButton('Наш Viber', url='viber://chat?number=%2B79867669931'),
            InlineKeyboardButton('Наш WhatsApp📱', url='https://wa.me/79867669931'),
            InlineKeyboardButton('Наше меню📖', url='https://t.me/more_and_morebot?start=menu')
        ]

        keyboard_contacts.add(*buttons)

        picture_list_str = need_card.data.get("picpath")
        video_list_str = need_card.data.get("videopath")
        album = types.MediaGroup()


        for index, picture in enumerate(picture_list_str):
            try:

                file = picture
                album.attach_photo(photo=file, caption=message_text if index == 0 else '')

            except Exception as ex:
                pass

        for index, video in enumerate(video_list_str):
            try:

                file = video
                album.attach_video(video=file, caption=message_text if index == 0 else '')

            except Exception as ex:
                pass

        '''для админов get_keyboard() if Admin().check_admin(message.chat.id) else None '''
        if len(picture_list_str) + len(video_list_str) > 1:
            await message.answer_media_group(album)
            await message.answer('Связаться с нами:', reply_markup=keyboard_contacts)

        elif len(picture_list_str) == 1:
            await message.answer_photo(picture_list_str[0], caption=message_text, reply_markup=keyboard_contacts)

        elif len(video_list_str) == 1:
            await message.answer_video(video_list_str[0], caption=message_text, reply_markup=keyboard_contacts)

        else:
            await message.answer(message_text, reply_markup=keyboard_contacts)

    else:
        await message.answer("Такого товара нет в наличии", reply_markup=get_keyboard() if Admin().check_admin(message.chat.id) else get_user_keyboard())

    return message

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
