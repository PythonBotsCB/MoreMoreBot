from aiogram.types import *
from aiogram.dispatcher.filters import Command
import json
from users import Admin
from adding import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import *
from constants import *

@dp.message_handler(commands=['newcard'], state=None)
async def addcard(message: Message) -> None:
    if Admin().check_admin(message.chat.id):
        await message.answer('Название товара: ')
        await AddCardState.name.set()
    else:
        await message.answer('У вас нет прав!')
        return

@dp.message_handler(content_types=['photo', 'video', 'text'], state=AddCardState.photo)
async def load_photo(message: Message, state: FSMContext) -> None:

    if message.text is not None and message.text.lower() == 'без медиа':
        await state.update_data(picpath=[])
        await state.update_data(videopath=[])

        state_data = await state.get_data()
        await message.answer('Товар добавлен!')

        with open(f'{DB_PATH}data.json', 'r', encoding=ENCODING) as file:
            data = json.load(file)

        state_data['id'] = data[-1].get('id') + 1

        data.append(state_data)

        with open(f'{DB_PATH}data.json', 'w', encoding=ENCODING) as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        await message.answer(f"ссылка на товар - https://t.me/more_and_morebot?start={state_data['id']}")

        await state.finish()
        return

    elif message.text == None:
        message_photo = [file.file_id for file in message.photo]

        try:
            message_video = message.video.file_id
        except:
            pass

        photos = []
        for photo_index in range(0, len(message_photo), 4):
            photos.append(message_photo[photo_index])

        try:
            photos.append(message.video.file_id)
        except Exception as ex:
            pass

        await state.update_data(picpath=photos)

        try:
            await state.update_data(videopath=[message_video])
        except Exception as ex:
            await state.update_data(videopath=[])

        state_data = await state.get_data()

        await message.answer('Товар добавлен!')

        with open(f'{DB_PATH}data.json', 'r', encoding=ENCODING) as file:
            data = json.load(file)

        state_data['id'] = data[-1].get('id') + 1 if len(data) >= 1 else 1

        data.append(state_data)

        if len(data) > 1:
            name_card = ''
            for card in data:

                '''Проверка на повторяемые карточки'''
                if card.get('name') == name_card:
                    current_index = data.index(card)
                    photo = card.get('picpath')
                    video = card.get('videopath')
                    if len(video) > 0:
                        data[current_index - 1]['videopath'] += video
                        photo = []
                    data[current_index - 1]['picpath'] += photo

                    data.remove(card)

                if len(card.get('videopath')) > 0:
                    try:
                        card['picpath'].remove(card.get('videopath')[0])
                    except Exception as ex:
                        pass

                name_card = card['name']

        await message.answer(f"Ссылка на товар - https://t.me/more_and_morebot?start={state_data['id']}")


        with open(f'{DB_PATH}data.json', 'w', encoding=ENCODING) as file:

            json.dump(data, file, indent=4, ensure_ascii=False)

        await state.finish()


@dp.message_handler(state=AddCardState.name)
async def load_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=u'{0}'.format(message.text))

    await message.answer('Описание товара: ')
    await AddCardState.next()


@dp.message_handler(state=AddCardState.description)
async def load_desc(message: Message, state: FSMContext) -> None:
    await state.update_data(description=u'{0}'.format(message.text))

    await message.reply('Изображения и видео товара:\nЕсли нет видео и картинок напишите "без медиа"')
    await AddCardState.next()
