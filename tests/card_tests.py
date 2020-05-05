import unittest
import sys

sys.path.append('../')

from src.card import Card


class TestCardCreation(unittest.TestCase):

    # cardVal = 3
    # cardFace = str(3)
    # cardAce = False
    # testCard = Card(value=cardVal, face=cardFace, ace=cardAce)

    def test_card_creation_cardValue(self):
        cardVal = 3
        cardFace = str(3)
        cardAce = False
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)

        self.assertEqual(testCard.__value__, cardVal)

    def test_card_creation_cardFace(self):
        cardVal = 3
        cardFace = str(3)
        cardAce = False
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)

        self.assertEqual(testCard.__face__, cardFace)

    def test_card_creation_cardAce_when_false(self):
        cardVal = 3
        cardFace = str(3)
        cardAce = False
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)

        self.assertFalse(testCard.__is_ace__)

    def test_card_creation_cardAce_when_True(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)

        self.assertTrue(testCard.__is_ace__)

    def test_card_creation_cardAce_when_false(self):
        cardVal = 3
        cardFace = str(3)
        cardAce = False
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)

        self.assertFalse(testCard.__is_ace__)

    def test_card_creation_cardAce_is_false_by_default(self):
        cardVal = 3
        cardFace = str(3)
        cardAce = False
        testCard = Card(value=cardVal, face=cardFace)

        self.assertFalse(testCard.__is_ace__)

    def test_card_creation_hidden(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        cardHidden = True
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)
        testCard.__is_hidden__ = cardHidden
        self.assertTrue(testCard.__is_hidden__)

    def test_card_creation_not_hidden(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        cardHidden = False
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)
        testCard.__is_hidden__ = cardHidden

        self.assertFalse(testCard.__is_hidden__)

    def test_card_creation_not_hidden_by_default(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)

        self.assertFalse(testCard.__is_hidden__)

    
class TestCardHiddenFunction(unittest.TestCase):
   
    def test_unhide_when_hidden(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        cardHidden = True
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)
        testCard.__is_hidden__ = cardHidden

        testCard.unhide()

        self.assertFalse(testCard.__is_hidden__)

    def test_unhide_when_not_hidden(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        cardHidden = False
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)
        testCard.__is_hidden__ = cardHidden

        testCard.unhide()

        self.assertFalse(testCard.__is_hidden__)

    def test_hide_when_not_hidden(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        cardHidden = True
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)
        testCard.__is_hidden__ = cardHidden

        testCard.hide()

        self.assertTrue(testCard.__is_hidden__)

    def test_hide_when_hidden(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        cardHidden = True
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)
        testCard.__is_hidden__ = cardHidden

        testCard.hide()

        self.assertTrue(testCard.__is_hidden__)


    def test_is_hidden_when_hidden(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        cardHidden = True
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)
        testCard.__is_hidden__ = cardHidden

        self.assertTrue(testCard.is_hidden())

    def test_is_hidden_when_not_hidden(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        cardHidden = False
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)
        testCard.__is_hidden__ = cardHidden

        self.assertFalse(testCard.is_hidden())

class TestCardFaceAndValueFunction(unittest.TestCase):
    def test_card_face(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        cardHidden = False
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)

        self.assertEqual(testCard.getFace(), cardFace)

    def test_card_value(self):
        cardVal = 9
        cardFace = str(9)
        cardAce = False
        cardHidden = True
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)

        self.assertEqual(testCard.getValue(), cardVal)

    def test_card_is_ace(self):
        cardVal = 11
        cardFace = 'A'
        cardAce = True
        cardHidden = False
        testCard = Card(value=cardVal, face=cardFace, ace=cardAce)

        self.assertEqual(testCard.is_ace(), cardAce)


if __name__ == "__main__":
    unittest.main()