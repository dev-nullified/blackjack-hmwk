import unittest
import sys
import io
import unittest.mock

sys.path.append('../')


class TestPlayerInit(unittest.TestCase):

    def test_hand_is_of_type_Hand(self):
        from src.player import Player
        from src.player import Hand
        testPlayer = Player()

        self.assertIsInstance(testPlayer.hand1, Hand)

    def test_hand2_is_of_type_Hand(self):
        from src.player import Player
        from src.player import Hand
        testPlayer = Player()

        self.assertIsInstance(testPlayer.hand2, Hand)

    def test_bank_is_of_type_float(self):
        from src.player import Player
        testPlayer = Player()

        self.assertIsInstance(testPlayer.bank, float)

    def test_bank_value_is_100_by_default(self):
        from src.player import Player
        testPlayer = Player()

        self.assertEqual(testPlayer.bank, 100.00)

    def test_bank_value_can_be_set_on_init(self):
        from src.player import Player

        bankValue = 39.50

        testPlayer = Player(start_ammount=bankValue)

        self.assertEqual(testPlayer.bank, bankValue)

    def test_bank_value_can_convert_int_to_float(self):
        from src.player import Player

        bankValue = 39

        testPlayer = Player(start_ammount=bankValue)

        self.assertIsInstance(testPlayer.bank, float)
        

    def test_split_status_is_of_type_bool(self):
        from src.player import Player
        testPlayer = Player()

        self.assertIsInstance(testPlayer.__is_hand_split__, bool)

    def test_split_status_is_false_by_default(self):
        from src.player import Player
        testPlayer = Player()

        self.assertFalse(testPlayer.__is_hand_split__)


# class TestPlay(unittest.TestCase):


class TestPlayOptions(unittest.TestCase):

    def test_play_option_returns_str(self):
        from src.player import Player

        testPlayer = Player()

        self.assertIsInstance(testPlayer.get_play_options(), str)

    def test_play_option_has_hit(self):
        from src.player import Player

        testPlayer = Player()
        testCanSplit = True
        testCanInsure = False

        self.assertIn('hit', testPlayer.get_play_options(canSplit=testCanSplit, canInsure=testCanInsure).lower())


    def test_play_option_has_stand(self):
        from src.player import Player

        testPlayer = Player()
        testCanSplit = True
        testCanInsure = False

        self.assertIn('stand', testPlayer.get_play_options(canSplit=testCanSplit, canInsure=testCanInsure).lower())


    def test_play_option_can_split_when_avalible(self):
        from src.player import Player

        testPlayer = Player()
        testCanSplit = True
        testCanInsure = False

        self.assertIn('split', testPlayer.get_play_options(canSplit=testCanSplit, canInsure=testCanInsure).lower())


    def test_play_option_can_insure_when_avalible(self):
        from src.player import Player

        testPlayer = Player()
        testCanSplit = True
        testCanInsure = True

        self.assertIn('insure', testPlayer.get_play_options(canSplit=testCanSplit, canInsure=testCanInsure).lower())


    def test_play_option_cant_split_when_unavalible(self):
        from src.player import Player

        testPlayer = Player()
        testCanSplit = False
        testCanInsure = False

        self.assertNotIn('split', testPlayer.get_play_options(canSplit=testCanSplit, canInsure=testCanInsure).lower())


    def test_play_option_cant_insure_when_unavalible(self):
        from src.player import Player

        testPlayer = Player()
        testCanSplit = False
        testCanInsure = False

        self.assertNotIn('insure', testPlayer.get_play_options(canSplit=testCanSplit, canInsure=testCanInsure).lower())


class TestValidDecision(unittest.TestCase):

    def test_fail_on_number_less_than_1(self):
        from src.player import Player
        testPlayer = Player()

        inputDecision = -1
        testCanSplit = False
        testCanInsure = False

        decisionValid = testPlayer.check_if_decision_valid(inputDecision, testCanSplit, testCanInsure)

        self.assertFalse(decisionValid)

    def test_fail_on_number_greater_than_4(self):
        from src.player import Player
        testPlayer = Player()

        inputDecision = 5
        testCanSplit = False
        testCanInsure = False

        decisionValid = testPlayer.check_if_decision_valid(inputDecision, testCanSplit, testCanInsure)

        self.assertFalse(decisionValid)

    def test_fail_on_split_when_not_able(self):
        from src.player import Player
        testPlayer = Player()

        inputDecision = 3
        testCanSplit = False
        testCanInsure = False

        decisionValid = testPlayer.check_if_decision_valid(inputDecision, testCanSplit, testCanInsure)

        self.assertFalse(decisionValid)

    def test_fail_on_insure_when_not_able(self):
        from src.player import Player
        testPlayer = Player()

        inputDecision = 4
        testCanSplit = False
        testCanInsure = False

        decisionValid = testPlayer.check_if_decision_valid(inputDecision, testCanSplit, testCanInsure)

        self.assertFalse(decisionValid)

    def test_true_on_decision_of_1(self):
        from src.player import Player
        testPlayer = Player()

        inputDecision = 1
        testCanSplit = False
        testCanInsure = False

        decisionValid = testPlayer.check_if_decision_valid(inputDecision, testCanSplit, testCanInsure)

        self.assertTrue(decisionValid)

    def test_true_on_decision_of_2(self):
        from src.player import Player
        testPlayer = Player()

        inputDecision = 2
        testCanSplit = False
        testCanInsure = False

        decisionValid = testPlayer.check_if_decision_valid(inputDecision, testCanSplit, testCanInsure)

        self.assertTrue(decisionValid)

    def test_true_on_decision_of_3_when_can_split(self):
        from src.player import Player
        testPlayer = Player()

        inputDecision = 3
        testCanSplit = True
        testCanInsure = False

        decisionValid = testPlayer.check_if_decision_valid(inputDecision, testCanSplit, testCanInsure)

        self.assertTrue(decisionValid)


    def test_true_on_decision_of_4_when_can_insure(self):
        from src.player import Player
        testPlayer = Player()

        inputDecision = 4
        testCanSplit = False
        testCanInsure = True

        decisionValid = testPlayer.check_if_decision_valid(inputDecision, testCanSplit, testCanInsure)

        self.assertTrue(decisionValid)


class TestPlayerHand(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    def test_add_card_to_player(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False))

        plyrHand1 = testPlayer.hand1
        plyrHand2 = testPlayer.hand2

        numberOfCardsInHand = plyrHand1.get_number_of_cards()

        #number of cards in hand should be 2
        self.assertEqual(numberOfCardsInHand, 2)

    def test_hand_value(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False))

        handValue = testPlayer.get_hand_value()

        # Hand value should be 6
        self.assertEqual(handValue, 6)

    def test_clear_hand(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False))

        # Clear the hand
        testPlayer.__clear_hand__()
        handValue = testPlayer.get_hand_value()

        # Hand value should be 0
        self.assertEqual(handValue, 0)

    def test_hand_output_returns_string(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False))

        handOutput = testPlayer.get_hand_output()

        # Hand value should be 0
        self.assertIsInstance(handOutput, str)



class TestPlayerReset(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    def test_reset_unsets_split_status(self):
        from src.player import Player

        testPlayer = Player()

        testPlayer.__set_split__()

        testPlayer.reset()

        self.assertFalse(testPlayer.__is_hand_split__)

    def test_reset_clears_hand(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False), self.generateCard(value=3, face=str(3), is_ace=False))


        testPlayer.reset()

        numberOfCardsInHand = testPlayer.hand1.get_number_of_cards()

        #number of cards in hand should be 0
        self.assertEqual(numberOfCardsInHand, 0)

    def test_reset_clears_hand2(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for card in range(0, 2):
            testPlayer.add_card(self.generateCard(value=3, face=str(3), is_ace=False), self.generateCard(value=3, face=str(3), is_ace=False))


        testPlayer.reset()

        numberOfCardsInHand = testPlayer.hand1.get_number_of_cards()

        #number of cards in hand2 should be 0
        self.assertEqual(numberOfCardsInHand, 0)


class TestBust(unittest.TestCase):
    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)


    def test_bust__hand1(self):
        from src.player import Player

        testPlayer = Player()

        # Create two cards
        # Generate Two "3" cards and add them to hand
        for I in range(0, 3):
            card1 = self.generateCard(value=10, face=str(10), is_ace=False)
            card2 = self.generateCard(value=10, face=str(10), is_ace=False)
            testPlayer.add_card(card1, card2)

        self.assertTrue(testPlayer.check_if_bust())

    


if __name__ == "__main__":
    unittest.main()