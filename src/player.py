from src.hand import Hand
import time

class Player():
    
    def __init__(self, start_ammount=100.00):
        self.hand1 = Hand()
        self.hand2 = Hand()
        self.bank = None

        # Convert to float if it isn't
        if not isinstance(start_ammount, float):
            self.bank = float(start_ammount)
        else:
            self.bank = start_ammount

        
        self.__is_hand_split__ = False


    # Play Game
    def play(self, canSplit=False, canInsure=False):

        can_split_status = self.__can_split__()


        # Get printable play options
        options = self.get_play_options(canSplit=canSplit, canInsure=canInsure)
        print(options)

        # Get decision
        decision = self.get_decision()
            
        # Check decision is valid
        decision_valid = self.check_if_decision_valid(decision, canSplit=can_split_status, canInsure=False)

        if decision_valid:
            return decision
        else:
            print(" !!! Invalid Option !!!")
            time.sleep(0.5)
            raise ValueError("Invalid Input option") 

    def get_play_options(self, canSplit=False, canInsure=False):
        output = "Pick an option:\n"
        output = output + "[1] Hit\n"
        output = output + "[2] Stand\n"

        if canSplit:
            output = output + "[3] Split\n"

        if canInsure:
            output = output + "[4] Insure\n"

        return output

    def check_if_decision_valid(self, decision, canSplit=False, canInsure=False):
        # Check valid
        if decision > 0 and decision < 5:

            if decision == 1 or decision == 2:
                return True


            # Check if user was given the option to split
            elif decision == 3 or decision == 4:
                if canSplit and decision == 3:
                    return True
                elif canInsure and decision == 4:
                    return True
                else:
                    return False

            else:
                return False
        else:
            return False


    def get_decision(self):

        decision = input("Please select a number from the options above: ")
        return int(decision)


    # Bank Status
    def get_bank(self):
        return self.bank

    def bank_deposit(self, ammount):
        self.bank = self.bank + ammount


    # Add Cards
    def add_card(self, card1, card2=None):
        if self.__get_split_status__():
            # Reject if 2nd card is not given when in split
            if card2:
                if not self.hand1.is_bust():
                    self.hand1.add_card(card1)
                
                if not self.hand2.is_bust():
                    self.hand2.add_card(card2)

        else:
            self.hand1.add_card(card1)


    # Printable Outputs for hand

    def get_hand_output(self):

        if self.__get_split_status__():
            return self.__get_hand_printable_output_in_split__()
        else:
            return self.__get_hand_printable_output__()

    def __get_hand_printable_output_in_split__(self):
        hand1_output = self.__get_hand1_printable_output__(showHandNumber=True)
        hand2_output = self.__get_hand2_printable_output__(showHandNumber=True)
        
        output = hand1_output + hand2_output

        return output

    def __get_hand_printable_output__(self):
        hand1_output = self.__get_hand1_printable_output__(showHandNumber=False)
        
        output = hand1_output

        return output

    def __get_hand1_printable_output__(self, showHandNumber=False):
        hand_value = self.hand1.get_hand_value()
        hand_output = self.hand1.get_printable_hand_output()

        if showHandNumber:
            return self.__compose_printable_output__(hand_output, hand_value, 1)
        else:
            return self.__compose_printable_output__(hand_output, hand_value)

    def __get_hand2_printable_output__(self, showHandNumber=False):
        hand_value = self.hand2.get_hand_value()
        hand_output = self.hand2.get_printable_hand_output()

        if showHandNumber:
            return self.__compose_printable_output__(hand_output, hand_value, 2)
        else:
            return self.__compose_printable_output__(hand_output, hand_value)

    def __compose_printable_output__(self, hand_output, hand_value, handNumber=0):
        hand_value_str = str(hand_value)
        output = "\t"

        if handNumber == 0:
            output = output + "Hand: "

        else:
            output = output + "Hand_" + str(handNumber) + ": "

        output = output + hand_output + " (Value: " + hand_value_str + ") \n"

        return output


    # Get The hand Objects
    def __get_hand_obj__(self):
        return [self.hand1.hand, self.hand2.hand]

    # Hand Values

    def get_hand_value(self):
        if self.__get_split_status__():
            return self.__get_hand_value_in_split__()

        else:
            return self.__get_hand1_value__()

    def __get_hand1_value__(self):

        return self.hand1.get_hand_value()

    def __get_hand_value_in_split__(self):
        value_hand_1 = self.hand1.get_hand_value()
        value_hand_2 = self.hand2.get_hand_value()

        return [value_hand_1, value_hand_2]


    # Split Functions

    def split(self):
        self.__set_split__()

        split1 = self.hand1.hand[0]
        split2 = self.hand1.hand[1]

        self.__clear_hand__()

        # self.hand.add_card(split1)
        # self.hand2.add_card(split2)
        self.add_card(card1=split1, card2=split2)
    
    def __get_split_status__(self):
        return self.__is_hand_split__

    def __set_split__(self):
        self.__is_hand_split__ = True

    def __unset_split__(self):
        self.__is_hand_split__ = False

    def __can_split__(self):
        can_split = False

        # make sure we're not already in a split
        if not self.__get_split_status__():
            # Check hand only has two cards
            if self.hand1.get_number_of_cards() == 2:
                # Check if first two cards are identical
                if self.hand1.first_two_cards_identical():
                    can_split = True
        
        return can_split



    # Check if hand is busted (over 21)

    def check_if_bust(self):
        bust = False
        # Bust in Split?
        if self.__get_split_status__():
            if self.__check_hand1_bust__() and self.__check_hand2_bust__():
                bust = True

        #Bust in normal
        else:
            if self.__check_hand1_bust__():
                bust = True

        return bust

    def __check_hand1_bust__(self):
        return self.hand1.is_bust()

    def __check_hand2_bust__(self):
        return self.hand2.is_bust()
    # Reset Functions

    def reset(self):
        self.__clear_hand__()
        self.__unset_split__()

    def __clear_hand__(self):
        self.hand1.clear_hand()
        self.hand2.clear_hand()
