import json
from constants import *

class Admin():
    '''Возможность добавлять новых админов и новые карточки'''
    ''' Если пользователь админ, то ему доступен ряд функций '''
    def __init__(self) -> None:
        self.__admins = self.get_admins()



    def get_admins(self) -> list:
        with open(f'{DB_PATH}admins.json', 'r', encoding=ENCODING) as admins:
            self.__admins = json.load(admins)
        return self.__admins

    def check_admin(self, user_id) -> bool:
        for user in self.__admins:
            if user == user_id:
                return True

        return False


