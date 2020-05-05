import unittest
import sys

sys.path.append('../')


class TestDealerBasic(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    def test_dealer_inherits_from_player(self):
        from src.dealer import Dealer
        from src.player import Player

        testDealer = Dealer()

        self.assertIsInstance(testDealer, Player)

    def test_dealer_play_fcn_returns_int(self):
        from src.dealer import Dealer
        testDealer = Dealer()

        self.assertIsInstance(testDealer.play(), int)

class TestDealerStand(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)


    # STAND FCNS
    def test_dealer_stands_when_hand_value_is_17(self):
        from src.dealer import Dealer
        testDealer = Dealer()

        # Create hand with value of 17
        testDealer.add_card(self.generateCard(value=10, face=str(10), is_ace=False))
        testDealer.add_card(self.generateCard(value=7, face=str(7), is_ace=False))

        # Dealer should return a 2 (i.e. stand)
        self.assertEqual(testDealer.play(), 2)

    def test_dealer_stands_when_hand_value_is_over_17(self):
        from src.dealer import Dealer
        testDealer = Dealer()

        # Create hand with value of 20
        testDealer.add_card(self.generateCard(value=10, face=str(10), is_ace=False))
        testDealer.add_card(self.generateCard(value=10, face=str(10), is_ace=False))

        # Dealer should return a 2 (i.e. stand)
        self.assertEqual(testDealer.play(), 2)

    def test_dealer_no_stands_when_hand_value_is_under_17(self):
        from src.dealer import Dealer
        testDealer = Dealer()

        # Create hand with value of 20
        testDealer.add_card(self.generateCard(value=10, face=str(10), is_ace=False))
        testDealer.add_card(self.generateCard(value=10, face=str(10), is_ace=False))

        # Dealer should NOT return a 2 (i.e. hit)
        self.assertNotEqual(testDealer.play(), 2)


class TestDealerStand(unittest.TestCase):
    # HIT FCNS

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)


    def test_dealer_no_hit_when_hand_value_is_17(self):
        from src.dealer import Dealer
        testDealer = Dealer()

        # Create hand with value of 17
        testDealer.add_card(self.generateCard(value=10, face=str(10), is_ace=False))
        testDealer.add_card(self.generateCard(value=7, face=str(7), is_ace=False))

        # Dealer should not return a 1 (i.e. hit)
        self.assertNotEqual(testDealer.play(), 1)

    def test_dealer_no_hit_when_hand_value_is_over_17(self):
        from src.dealer import Dealer
        testDealer = Dealer()

        # Create hand with value of 19
        testDealer.add_card(self.generateCard(value=10, face=str(10), is_ace=False))
        testDealer.add_card(self.generateCard(value=9, face=str(9), is_ace=False))

        # Dealer should not return a 1 (i.e. hit)
        self.assertNotEqual(testDealer.play(), 1)
    
    def test_dealer_hits_when_hand_value_is_under_17(self):
        from src.dealer import Dealer
        testDealer = Dealer()

        # Create hand with value of 12
        testDealer.add_card(self.generateCard(value=5, face=str(5), is_ace=False))
        testDealer.add_card(self.generateCard(value=7, face=str(7), is_ace=False))

        # Dealer should return a 1 (i.e. hit)
        self.assertEqual(testDealer.play(), 1)


class TestDealerUnhideCard(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    def test_dealer_can_unhide_2nd_card_in_hand(self):
        from src.dealer import Dealer

        testDealer = Dealer()

        testCard1 = self.generateCard(value=10, face=str(10), is_ace=False)
        testCard2 = self.generateCard(value=11, face='A', is_ace=False)

        # Hide the 2nd card

        testDealer.add_card(testCard1)
        testDealer.add_card(testCard2)

        self.assertFalse(testDealer.hand1.hand[1].is_hidden())


if __name__ == "__main__":
    unittest.main()