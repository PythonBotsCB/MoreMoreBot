import json
from constants import *

class Card():
    def __init__(self, id:int, name:str, description:str, picpath:list, videopath:list):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__picpath = picpath
        self.__videopath = videopath
        self.data = {
            'id' : self.__id,
            'name' : self.__name,
            'description' : self.__description,
            'picpath' : self.__picpath,
            'videopath' : self.__videopath
        }

    def __str__(self) -> str:
        return f'{self.__name} {self.__id}'

class EmptyCard(Card):
    def __init__(self):
        super().__init__(0, '', '', [], [])

    def __str__(self) -> str:
        return 'Такой карты нет'


class Finder():
    def __init__(self, data):
        self.cards = data

    def Find(self, id:str) -> Card:
        try:
            '''в качетстве оптимизации можно было бы добавить бинарный поиск'''

            for card in set(self.cards):
                # O(n), сделать бинарный поиск
                if card.data.get('id') == int(id):
                    return card

            else:
                return EmptyCard()
        except Exception as ex:
            return EmptyCard()

class Requests():
    def __init__(self, request:str):
        self.__data = []
        self.request = request

        with open(f'{DB_PATH}data.json', 'r', encoding=ENCODING) as file:
            json_data = json.load(file)

            for card in json_data:
                self.__data.append(Card(
                    card.get('id'),
                    card.get('name'),
                    card.get('description'),
                    card.get('picpath'),
                    card.get('videopath')
                ))

        self.__finder = Finder(self.__data)

        self.card = self.__findItem()

    def __findItem(self):
        return self.__finder.Find(self.request)



