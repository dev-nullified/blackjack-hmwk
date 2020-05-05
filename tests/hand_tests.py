import unittest
import sys

# sys.path.append('../')


class TestHandInit(unittest.TestCase):

    def test_hand_var_is_type_list(self):
        from src.hand import Hand

        testHand = Hand()

        self.assertIsInstance(testHand.hand, list)

    def test_hand_var_is_empty_on_init(self):
        from src.hand import Hand

        testHand = Hand()

        self.assertEqual(len(testHand.hand), 0)

    # def test_bust_var_is_type_bool(self):
    #     from src.hand import Hand

    #     testHand = Hand()

    #     self.assertIsInstance(testHand.bust, bool)

    # def test_bust_var_is_False_on_init(self):
    #     from src.hand import Hand

    #     testHand = Hand()

    #     self.assertFalse(testHand.bust)


class TestHandCardIntegration(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    def test_fcn_add_card_adds_card_to_hand(self):
        from src.hand import Hand

        testHand = Hand()

        tempCard = self.generateCard()

        testHand.add_card(card=tempCard)

        self.assertIn(tempCard, testHand.hand)

    def test_fcn_add_card_adds_card_to_end_of_hand(self):
        from src.hand import Hand

        testHand = Hand()

        tempCard = self.generateCard()
        tempCard2 = self.generateCard(value=3, face=str(3), is_ace=False)

        testHand.add_card(card=tempCard)
        testHand.add_card(card=tempCard2)

        self.assertEqual(tempCard2, testHand.hand[-1])

    def test_fcn_unhide_only_unhides_1_card_in_hand(self):
        from src.hand import Hand

        testHand = Hand()

        tempCards = []
        tempCards.append(self.generateCard())
        tempCards.append(self.generateCard(value=3, face=str(3), is_ace=False))
        tempCards.append(self.generateCard(value=10, face='K', is_ace=False))

        # Set hidden status on all temp cards
        for card in tempCards:
            card.hide()

        # add temp cards to deck
        for card in tempCards:
            testHand.add_card(card)


        # Unhide card
        testHand.unhide_card()

        numberOfHiddenCards = 0
        # check number of hidden cards
        for card in testHand.hand:
            if card.is_hidden():
                numberOfHiddenCards = numberOfHiddenCards + 1

        self.assertEqual(numberOfHiddenCards, 2)

    def test_fcn_unhide_only_unhides_2nd_card_in_hand(self):
        from src.hand import Hand

        testHand = Hand()

        tempCards = []
        tempCards.append(self.generateCard())
        tempCards.append(self.generateCard(value=3, face=str(3), is_ace=False))
        tempCards.append(self.generateCard(value=10, face='K', is_ace=False))

        # Set hidden status of 2nd temp card
        tempCards[1].hide()


        # add temp cards to deck
        for card in tempCards:
            testHand.add_card(card)


        # Unhide card
        testHand.unhide_card()

        self.assertFalse(testHand.hand[1].is_hidden())


class TestHandUtilFcns(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    def test_clear_hand_fcn(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate 2 cards and add them to hand
        for card in range(0, 2):
            testHand.add_card(self.generateCard())

        
        # Clear hand
        testHand.clear_hand()

        # Ensure hand is empty
        self.assertEqual(len(testHand.hand), 0)

    def test_number_of_cards(self):
        from src.hand import Hand
        import random
        testHand = Hand()

        # Get a random int between 1 and 10
        numberOfCardsToGenerate = random.randint(1,10)

        # Generate random number cards and add them to hand
        for card in range(0, numberOfCardsToGenerate):
            testHand.add_card(self.generateCard())

        # Number of cards in hand should be equal to numberOfCardsToGenerate
        self.assertEqual(testHand.get_number_of_cards(), numberOfCardsToGenerate)

    def test_first_two_numerical_cards_are_identical(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate 2 cards and add them to hand
        for card in range(0, 2):
            testHand.add_card(self.generateCard(value=4, face=str(4),is_ace=False))

        # Generate 3rd alt card
        testHand.add_card(self.generateCard(value=10, face='Q',is_ace=False))

        self.assertTrue(testHand.first_two_cards_identical())

    def test_first_two_face_cards_are_identical(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate 2 cards and add them to hand
        for card in range(0, 2):
            testHand.add_card(self.generateCard(value=10, face='Q',is_ace=False))

        # Generate 3rd alt card
        testHand.add_card(self.generateCard(value=4, face=str(4),is_ace=False))
        

        self.assertTrue(testHand.first_two_cards_identical())

    def test_first_two_ace_cards_are_identical(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate 2 cards and add them to hand
        for card in range(0, 2):
            testHand.add_card(self.generateCard(value=11, face='A',is_ace=True))

        # Generate 3rd alt card
        testHand.add_card(self.generateCard(value=4, face=str(4),is_ace=False))
        
        self.assertTrue(testHand.first_two_cards_identical())

    def test_face_and_numeric_not_equal(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate Face card and add it to hand
        testHand.add_card(self.generateCard(value=10, face='J',is_ace=False))

        # Generate Numeric card and add it to hand
        testHand.add_card(self.generateCard(value=4, face=str(4),is_ace=False))
        
        self.assertFalse(testHand.first_two_cards_identical())

    def test_face_and_ace_not_equal(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate Face card and add it to hand
        testHand.add_card(self.generateCard(value=10, face='J',is_ace=False))

        # Generate Ace card and add it to hand
        testHand.add_card(self.generateCard(value=11, face='A',is_ace=True))
        
        self.assertFalse(testHand.first_two_cards_identical())

    def test_numeric_and_ace_not_equal(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate Numeric card and add it to hand
        testHand.add_card(self.generateCard(value=9, face=str(9), is_ace=False))

        # Generate Ace card and add it to hand
        testHand.add_card(self.generateCard(value=11, face='A', is_ace=True))
        
        self.assertFalse(testHand.first_two_cards_identical())


class TestBustStatus(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    
    def test_is_bust_fcn_when_hand_val_is_under_21(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testHand.add_card(self.generateCard(value=3, face=str(3), is_ace=False))


        # Value of hand is 6, so bust should be false
        self.assertFalse(testHand.is_bust())

    def test_is_bust_fcn_when_hand_is_empty(self):
        from src.hand import Hand
        testHand = Hand()

        # Value of hand is 0, so bust should be false
        self.assertFalse(testHand.is_bust())

    def test_is_bust_fcn_when_hand_val_is_21(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate a "king" and "ace" card and add them to hand
        testHand.add_card(self.generateCard(value=11, face='A', is_ace=False))
        testHand.add_card(self.generateCard(value=10, face='K', is_ace=False))

        # Value of hand is 21, so bust should be false
        self.assertFalse(testHand.is_bust())

    def test_is_bust_fcn_when_hand_val_is_over_21(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate three "king" cards and add them to hand
        for card in range(0,3):
            testHand.add_card(self.generateCard(value=10, face='K', is_ace=False))

        # Value of hand is 30, so bust should be True
        self.assertTrue(testHand.is_bust())


class TestHandValueFcn(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)


    def test_value_can_add(self):
        from src.hand import Hand
        import random
        testHand = Hand()

        # Get a random int between 1 and 10
        randomInt1 = random.randint(1,10)
        randomInt2 = random.randint(1,10)

        valueOfHand = randomInt1 + randomInt2

        testHand.add_card(self.generateCard(value=randomInt1, face=str(randomInt1), is_ace=False))
        testHand.add_card(self.generateCard(value=randomInt2, face=str(randomInt2), is_ace=False))

        self.assertEqual(testHand.get_hand_value(), valueOfHand)


    def test_value_of_three_aces_in_hand(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate three "ace" cards and add them to hand
        for card in range(0, 3):
            testHand.add_card(self.generateCard(value=11, face='A', is_ace=True))

        # Three Aces should be create a hand value of 13 (as not to bust)
        self.assertEqual(testHand.get_hand_value(), 13)

    def test_value_with_single_ace_and_a_face_card(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate Ace and King cards and add them to hand
        testHand.add_card(self.generateCard(value=11, face='A', is_ace=True))
        testHand.add_card(self.generateCard(value=10, face='K', is_ace=False))

        # One Ace and one King should be create a hand value of 21
        self.assertEqual(testHand.get_hand_value(), 21)

    def test_value_with_single_ace_and_a_numeric(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate Ace and King cards and add them to hand
        testHand.add_card(self.generateCard(value=11, face='A', is_ace=True))
        testHand.add_card(self.generateCard(value=10, face=str(10), is_ace=False))

        # One Ace and one King should be create a hand value of 21
        self.assertEqual(testHand.get_hand_value(), 21)

    def test_value_with_hidden_card(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate Ace and 10 cards and add them to hand
        card1 = self.generateCard(value=11, face='A', is_ace=True)
        card2 = self.generateCard(value=10, face=str(10), is_ace=False)

        # hide the ace
        card1.hide()
        testHand.add_card(card1)
        testHand.add_card(card2)

        # Value should be 10 when the ace card is hidden
        self.assertEqual(testHand.get_hand_value(), 10)


class TestHandOutputFcn(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)


    def test_output_when_hand_empty(self):
        from src.hand import Hand
        testHand = Hand()

        # Should be equal to empty string
        self.assertEqual(testHand.get_printable_hand_output(), "")


    def test_output_is_string(self):
        from src.hand import Hand
        testHand = Hand()

        self.assertIsInstance(testHand.get_printable_hand_output(), str)


    def test_output_is_correct(self):
        from src.hand import Hand
        testHand = Hand()

        # Add a King and a 7
        testHand.add_card(self.generateCard(value=10, face='K', is_ace=False))
        testHand.add_card(self.generateCard(value=7, face=str(7), is_ace=False))

        outputShouldBe = "K 7 "

        self.assertEqual(testHand.get_printable_hand_output(), outputShouldBe)


    def test_output_hides_cards(self):
        from src.hand import Hand
        testHand = Hand()

        # Generate Ace and 10 cards and add them to hand
        testHand.add_card(self.generateCard(value=11, face='A', is_ace=True))
        card2 = self.generateCard(value=10, face=str(10), is_ace=False)

        # hide the 10
        card2.hide()
        testHand.add_card(card2)

        outputShouldBe = "A # "

        self.assertEqual(testHand.get_printable_hand_output(), outputShouldBe)


if __name__ == "__main__":
    unittest.main()