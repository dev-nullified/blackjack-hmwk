
class Hand():

    def __init__(self):
        self.hand = []
        # self.bust = False

    def add_card(self, card):
        self.hand.append(card)
        
    def clear_hand(self):
        self.hand.clear()

    def get_printable_hand_output(self):
        # convert hand to printable string
        output = ""
        for card in self.hand:
            if card.is_hidden():
                output = output + '#' + ' '
            else:
                output = output + card.getFace() + ' '

        return output


    def get_hand_value(self):
        value = 0
        numberOfAces = 0
        aceInHand = False
        for card in self.hand:
            # Pass over hidden cards
            if card.is_hidden():
                continue

            if card.is_ace():
                aceInHand = True
                numberOfAces = numberOfAces + 1

            else: 
                value = value + card.getValue()

        # If an ace was in the deck check to see which value of aces wins
        if aceInHand:
            for ace_card in range(numberOfAces):
                if value >= 11: 
                    value = value + 1
                else:
                    value = value + 11
    
        return value

    def get_number_of_cards(self):
        return len(self.hand)

    def first_two_cards_identical(self):

        if self.hand[0].getFace() == self.hand[1].getFace():
            return True
        else:
            return False


    def is_bust(self):
        if self.get_hand_value() > 21:
            return True
        else:
            return False

    def unhide_card(self):
        self.hand[1].unhide()
        # for card in self.hand:
        #     card.unhide()
        