from src.player import Player
from src.dealer import Dealer
from src.deck   import Deck
import subprocess, platform
import time

import os

class Game():

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()


    def run(self):
        # Deal cards
        self.new_run()

        # Print board
        self.print_board()

        # Player 1 goes first
        self.players_turn()

        self.print_board()

        # dealers turn
        self.dealer_turn()

        # check who won
        winner = self.check_winner()

        print(winner)

    def new_run(self):

        # Deal cards to player
        self.__deal_to_plyr__()


        # deal cards to dealer
        self.__deal_to_dealer__()

    def __deal_to_plyr__(self):
        for i in range(0,2):
            self.player.add_card(self.deck.get_card(), None)

    def __deal_to_dealer__(self):
        self.dealer.add_card(self.deck.get_card(), None)
        self.dealer.add_card(self.deck.get_hidden_card(), None)

    def players_turn(self):

        while True:
            #  Get players's decision 
            decision = self.player.play()

            # If stand then break the loop
            if decision == 2:
                break

            elif decision == 1: #IF the player hits
                self.hit_player()
                self.print_board()

            elif decision == 3: # Split for the player 
                self.split_player()
                self.print_board()

            elif decision == 4: # Insurer the player
                pass
        
            # Check if bust
            if self.player.check_if_bust():
                break

    def hit_player(self):
        # If player is in a split
        if self.player.__get_split_status__():
            self.player.add_card(card1=self.deck.get_card(), card2=self.deck.get_card())
        else:
            self.player.add_card(card1=self.deck.get_card(), card2=None)


    def split_player(self):
        self.player.split()
        self.hit_player()


    def insure_player(self):
        pass

    
    def hit_dealer(self):
        self.dealer.add_card(card1=self.deck.get_card(), card2=None)
        
    def dealer_reveal(self, inTest=False):
        # Reveal hidden card
        self.dealer.unhide_card()

        if not inTest:
            # Print board
            self.print_board()
            print("Dealer revealed hidden card")
            time.sleep(2)

    def dealer_turn(self):

        # Reveal hidden card
        self.dealer_reveal()

        
        while True:

            #  Get players's decision 
            decision = self.dealer.play()

            # If stand then break the loop
            if decision == 2:
                break

            elif decision == 1: #IF the dealer hits
                self.hit_dealer()

                self.print_board()
                print("Dealer chose to hit")
                time.sleep(1)

    # CHECK WINNER BY BUST
    def __check_tie_by_both_bust__(self, player_bust_status, dealer_bust_status):

        if (player_bust_status and dealer_bust_status):
            return True
        else:
            return False
    
    def __check_player_bust_and_dealer_hasnt__(self, player_bust_status, dealer_bust_status):
        if (player_bust_status and not dealer_bust_status):
            return True
        else:
            return False

    def __check_dealer_bust_and_player_hasnt__(self, player_bust_status, dealer_bust_status):
        if (not player_bust_status and dealer_bust_status):
            return True
        else:
            return False

    def __winner_by_bust__(self, player_bust_status, dealer_bust_status):
        # Tie if both bust
        if self.__check_tie_by_both_bust__(player_bust_status, dealer_bust_status):
            return self.tie()

        # If player bust and dealer hasn't
        if self.__check_player_bust_and_dealer_hasnt__(player_bust_status, dealer_bust_status):
            return self.bust()

        # If dealer bust and player hasn't
        if self.__check_dealer_bust_and_player_hasnt__(player_bust_status, dealer_bust_status):
            return self.winner()

        return None


    # CHECK WINNER BY VALUE
    def __check_plyr_hand_value_larger_than_dealer__(self, plyrHandValue, dealerHandValue):
        
        if plyrHandValue > dealerHandValue:
            return True
        else:
            return False

    def __check_player_and_dealer_hands_are_equal__(self, plyrHandValue, dealerHandValue):
        if plyrHandValue == dealerHandValue:
            return True
            
        else:
            return False

    def __winner_by_value__(self, plyrHand1Value, plyrHand2Value, dealerHandValue, playerSplit=False):

        # Check hand 1 or hand2 is larger than dealers
        if self.__check_plyr_hand_value_larger_than_dealer__(plyrHand1Value, dealerHandValue) or self.__check_plyr_hand_value_larger_than_dealer__(plyrHand2Value, dealerHandValue):
            return self.winner()
        
        # # Check hand 2 is larger than dealers
        # elif self.__check_plyr_hand_value_larger_than_dealer__(plyrHand2Value, dealerHandValue) and playerSplit:
        #     return self.winner()

        # Check if hand1 or is tied with dealer
        elif self.__check_player_and_dealer_hands_are_equal__(plyrHand1Value, dealerHandValue) or self.__check_player_and_dealer_hands_are_equal__(plyrHand2Value, dealerHandValue):
            return self.tie()

        # # Check if hand2 is tied with dealer
        # elif self.__check_player_and_dealer_hands_are_equal__(plyrHand2Value, dealerHandValue) and playerSplit:
        #     return self.tie()

        # Otherwise player lost
        else:
            return self.loose()




    def check_winner(self):
        player_bust_status = self.player.check_if_bust()
        dealer_bust_status = self.dealer.check_if_bust()
        
        dealer_hand_value = self.dealer.get_hand_value()
        # hand_values = self.player.get_hand_value()
        hand1_value = self.player.hand1.get_hand_value()
        hand2_value = self.player.hand2.get_hand_value()

        player_in_split = self.player.__get_split_status__()


        # Check winner by bust
        winnerByBustOutcome = self.__winner_by_bust__(player_bust_status, dealer_bust_status)

        if winnerByBustOutcome:
            return winnerByBustOutcome

        # Check Winner By Value

        winnerByValueOutcome = self.__winner_by_value__(hand1_value, hand2_value, dealer_hand_value, player_in_split)

        if winnerByValueOutcome:
            return winnerByValueOutcome

        return "UNKNOWN OUTCOME"

    def winner(self):
        return "You Win"
    
    def tie(self):
        return "Game Tied"

    def loose(self):
        return "You Lose"

    def bust(self):
        return "BUST - " + self.loose()


    def print_board(self):
        # Clear screen
        self.clear_screen()

        # print Dealer
        print("Dealer")
        print(self.dealer.get_hand_output())


        # print("\n\n")

        # print Player
        print("Player 1")
        print(self.player.get_hand_output())

        print("")

    def clear_screen(self):
        if platform.system()=="Windows":
            subprocess.Popen("cls", shell=True).communicate()
        else: #Linux and Mac
            print("\033c", end="")

        # pass



