import random
import copy

from src.card import Card


class Deck():

    def __init__(self, generate=True):

        self.__faceCards__ = ['A', 'J', 'Q', 'K']

        self.__deck__ = []

        if generate:
            self.__generate_deck__()



    def __generate_deck__(self):
        self.__generate_numeric_cards__()
        self.__generate_face_cards__()

    def __generate_numeric_cards__(self):
        for card_value in range(2,11):
            self.__add_card_to_deck__(value=card_value, face=str(card_value))

    def __generate_face_cards__(self):

        for face_card in self.__faceCards__:
            if 'a' in face_card.lower():
                value = 11
                self.__add_card_to_deck__(value=value, face=face_card, isAce=True)
            else:
                value = 10
                self.__add_card_to_deck__(value=value, face=face_card, isAce=False)
                


    def __add_card_to_deck__(self, value, face, isAce=False):
        newCard = Card(value=value, face=face, ace=isAce)
        self.__deck__.append(newCard)
    

    def get_card(self):
        
        poppedCard = random.choice(self.__deck__)

        return poppedCard

    def get_hidden_card(self):
        poppedCard = copy.deepcopy(self.get_card())

        # Set hidden
        poppedCard.hide()

        return poppedCard

    

    
