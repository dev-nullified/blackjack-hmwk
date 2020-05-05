from src.player import Player

class Dealer(Player):

    def play(self):

        # if value is 17 or greater then stand (i.e. option 2)
        if self.get_hand_value() >= 17:
            return 2

        else:
            # Otherwise hit
            return 1


    def unhide_card(self):
        self.hand1.unhide_card()

