import unittest
import sys
import io
import unittest.mock

# sys.path.append('../')


class TestAddCardInSplit(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    def test_cards_are_added_to_correct_hand_when_in_split_hand1(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        card1 = self.generateCard(value=3, face=str(3), is_ace=False)
        card2 = self.generateCard(value=4, face=str(4), is_ace=False)

        # Set split status
        testPlayer.__set_split__()

        testPlayer.add_card(card1, card2)

        handsFromPlayer = testPlayer.__get_hand_obj__()
        plyrHand1 = handsFromPlayer[0]
        plyrHand2 = handsFromPlayer[1]

        self.assertEqual(plyrHand1[0], card1)

    def test_cards_are_added_to_correct_hand_when_in_split_hand2(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        card1 = self.generateCard(value=3, face=str(3), is_ace=False)
        card2 = self.generateCard(value=4, face=str(4), is_ace=False)

        # Set split status
        testPlayer.__set_split__()

        testPlayer.add_card(card1, card2)

        handsFromPlayer = testPlayer.__get_hand_obj__()
        plyrHand1 = handsFromPlayer[0]
        plyrHand2 = handsFromPlayer[1]

        self.assertEqual(plyrHand2[0], card2)
 
    def test_add_card_in_split_when_2nd_card_not_provided(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        card1 = self.generateCard(value=3, face=str(3), is_ace=False)
        card2 = None

        # Set split status
        testPlayer.__set_split__()

        testPlayer.add_card(card1, card2)

        handsFromPlayer = testPlayer.__get_hand_obj__()
        plyrHand1 = handsFromPlayer[0]
        plyrHand2 = handsFromPlayer[1]

        self.assertEqual(len(plyrHand2), 0)
    
    def test_add_card_in_split_when_2nd_card_not_provided_hand1(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        card1 = self.generateCard(value=3, face=str(3), is_ace=False)
        card2 = None

        # Set split status
        testPlayer.__set_split__()

        testPlayer.add_card(card1, card2)

        handsFromPlayer = testPlayer.__get_hand_obj__()
        plyrHand1 = handsFromPlayer[0]
        plyrHand2 = handsFromPlayer[1]

        self.assertEqual(len(plyrHand1), 0)



class TestSplitStatus(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)


    def test_can_split_true_when_able_fcn(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False))

        canSplitStatus = testPlayer.__can_split__()

        self.assertTrue(canSplitStatus)

    def test_can_split_true_when_able_fcn(self):
        from src.player import Player

        testPlayer = Player()

        # Generate Two cards and add them to hand
        testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False))
        testPlayer.add_card(self.generateCard(value=2, face=str(2), is_ace=False))

        canSplitStatus = testPlayer.__can_split__()

        self.assertFalse(canSplitStatus)

class TestSplit(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    def test_cards_are_moved_when_split(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        card1 = self.generateCard(value=3, face=str(3), is_ace=False)
        card2 = self.generateCard(value=3, face=str(3), is_ace=False)

        testPlayer.add_card(card1)
        testPlayer.add_card(card2)

        testPlayer.split()

        # canSplitStatus = testPlayer.__can_split__()

        handsFromPlayer = testPlayer.__get_hand_obj__()
        plyrHand1 = handsFromPlayer[0]
        plyrHand2 = handsFromPlayer[1]

        self.assertEqual(plyrHand1[0], card1)

    def test_cards_are_moved_when_split_hand2(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        card1 = self.generateCard(value=3, face=str(3), is_ace=False)
        card2 = self.generateCard(value=3, face=str(3), is_ace=False)

        testPlayer.add_card(card1)
        testPlayer.add_card(card2)

        testPlayer.split()

        handsFromPlayer = testPlayer.__get_hand_obj__()
        plyrHand1 = handsFromPlayer[0]
        plyrHand2 = handsFromPlayer[1]

        self.assertEqual(plyrHand2[0], card2)

    def test_hand1_has_1_card_after_split(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        card1 = self.generateCard(value=3, face=str(3), is_ace=False)
        card2 = self.generateCard(value=3, face=str(3), is_ace=False)

        testPlayer.add_card(card1)
        testPlayer.add_card(card2)

        testPlayer.split()

        handsFromPlayer = testPlayer.__get_hand_obj__()
        plyrHand1 = handsFromPlayer[0]
        plyrHand2 = handsFromPlayer[1]


        self.assertEqual(len(plyrHand1), 1)

    def test_hand2_has_1_card_after_split(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        card1 = self.generateCard(value=3, face=str(3), is_ace=False)
        card2 = self.generateCard(value=3, face=str(3), is_ace=False)

        testPlayer.add_card(card1)
        testPlayer.add_card(card2)

        testPlayer.split()

        handsFromPlayer = testPlayer.__get_hand_obj__()
        plyrHand1 = handsFromPlayer[0]
        plyrHand2 = handsFromPlayer[1]

        self.assertEqual(len(plyrHand2), 1)


    def test_split_status_is_set_after_split(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        card1 = self.generateCard(value=3, face=str(3), is_ace=False)
        card2 = self.generateCard(value=3, face=str(3), is_ace=False)

        testPlayer.add_card(card1)
        testPlayer.add_card(card2)

        testPlayer.split()

        splitStatus = testPlayer.__get_split_status__()

        self.assertTrue(splitStatus)


class TestHandValueInSplit(unittest.TestCase):
    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    def test_hand_value_returns_list_in_split(self):
        from src.player import Player

        testPlayer = Player()
        testPlayer.__set_split__()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False))

        handValue = testPlayer.get_hand_value()

        # Hand value should be 6
        self.assertIsInstance(handValue, list)


    def test_hand1_value_in_split(self):
        from src.player import Player

        testPlayer = Player()
        testPlayer.__set_split__()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False), self.generateCard(value=4, face=str(4), is_ace=False))

        handValue = testPlayer.get_hand_value()

        # Hand value should be 6
        self.assertEqual(handValue[0], 6)

    def test_hand1_value_in_split(self):
        from src.player import Player

        testPlayer = Player()
        testPlayer.__set_split__()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False), self.generateCard(value=4, face=str(4), is_ace=False))

        handValue = testPlayer.get_hand_value()

        # Hand value should be 8
        self.assertEqual(handValue[1], 8)


class TestClearHandInSplit(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)



    def test_clear_hand1(self):
        from src.player import Player

        testPlayer = Player()
        testPlayer.__set_split__()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False))

        # Clear the hand
        testPlayer.__clear_hand__()
        handValue = testPlayer.get_hand_value()[0]

        # Hand1 value should be 0
        self.assertEqual(handValue, 0)

    def test_clear_hand2(self):
        from src.player import Player

        testPlayer = Player()
        testPlayer.__set_split__()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False))

        # Clear the hand
        testPlayer.__clear_hand__()
        handValue = testPlayer.get_hand_value()[1]

        # Hand1 value should be 0
        self.assertEqual(handValue, 0)


class TestHandOutputInSplit(unittest.TestCase):
    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)


    def test_hand_output_returns_string(self):
        from src.player import Player

        testPlayer = Player()
        testPlayer.__set_split__()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False), self.generateCard(value=3, face=str(3), is_ace=False))

        handOutput = testPlayer.get_hand_output()

        self.assertIsInstance(handOutput, str)

    def test_hand_output_returns_string(self):
        from src.player import Player

        testPlayer = Player()
        testPlayer.__set_split__()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False), self.generateCard(value=3, face=str(3), is_ace=False))

        handOutput = testPlayer.get_hand_output()

        self.assertIsInstance(handOutput, str)


class TestBustInSplit(unittest.TestCase):
    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)


    def test_bust_both_hands(self):
        from src.player import Player

        testPlayer = Player()
        testPlayer.__set_split__()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for I in range(0, 3):
            card1 = self.generateCard(value=10, face=str(10), is_ace=False)
            card2 = self.generateCard(value=10, face=str(10), is_ace=False)
            testPlayer.add_card(card1, card2)

        self.assertTrue(testPlayer.check_if_bust())

    
    def test_bust_hand1_only(self):
        from src.player import Player

        testPlayer = Player()
        testPlayer.__set_split__()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for I in range(0, 3):
            card1 = self.generateCard(value=10, face=str(10), is_ace=False)
            card2 = self.generateCard(value=2, face=str(2), is_ace=False)
            testPlayer.add_card(card1)

        self.assertFalse(testPlayer.check_if_bust())


    def test_bust_hand2_only(self):
        from src.player import Player

        testPlayer = Player()
        testPlayer.__set_split__()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for I in range(0, 3):
            card2 = self.generateCard(value=10, face=str(10), is_ace=False)
            card1 = self.generateCard(value=2, face=str(2), is_ace=False)
            testPlayer.add_card(card1)

        self.assertFalse(testPlayer.check_if_bust())

if __name__ == "__main__":
    unittest.main()
        