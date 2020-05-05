
class Card():

    def __init__(self, value, face, ace=False):
        self.__value__ = value
        self.__face__ = face
        self.__is_ace__ = ace
        self.__is_hidden__ = False

        # self.__value__ = 11
        # self.__face__ = 'A'
        # self.__is_ace__ = True


    def getValue(self):
        return self.__value__

    def getFace(self):
        return self.__face__

    def is_ace(self):
        return self.__is_ace__

    def unhide(self):
        self.__is_hidden__ = False

    def hide(self):
        self.__is_hidden__ = True

    def is_hidden(self):
        return self.__is_hidden__

        