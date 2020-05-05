import unittest

import sys

# sys.path.append('../')

class TestDeckInit(unittest.TestCase):

    def test_face_cards_are_correct(self):
        from src.deck import Deck

        testDeck = Deck()

        faceCards = ['A', 'J', 'Q', 'K']

        self.assertListEqual(testDeck.__faceCards__, faceCards)

    def test_deck_generates_deck_of_13_cards(self):
        from src.deck import Deck

        testDeck = Deck()

        self.assertEqual(len(testDeck.__deck__), 13)


    def test_deck_only_contains_cards_type(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck()
        # testDeck.__deck__.append(2319)

        isCardType = True

        for card in testDeck.__deck__:
            if not isinstance(card, Card):
                isCardType = False
                break

        self.assertTrue(isCardType)

class TestCardGeneration(unittest.TestCase):

    # def test_fcn_face_cards_generated(self):
    #     from src.deck import Deck
    #     from src.deck import Card

    #     testDeck = Deck(generate=False)
        
    #     testDeck.__generate_face_cards__()

    def test_fcn_generate_face_cards_generates_4_cards(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=False)
        
        testDeck.__generate_face_cards__()

        self.assertEqual(len(testDeck.__deck__), 4)

    def test_fcn_generate_numeric_cards_generates_9_cards(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=False)
        
        testDeck.__generate_numeric_cards__()

        self.assertEqual(len(testDeck.__deck__), 9)



    def test_card_faces_are_all_str(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=True)

        faceIsStr = True

        for card in testDeck.__deck__:
            if not isinstance(card.__face__, str):
                faceIsStr = False

        self.assertTrue(faceIsStr)

    def test_card_faces_of_face_cards_are_all_str(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=False)

        testDeck.__generate_face_cards__()

        faceIsStr = True

        for card in testDeck.__deck__:
            if not isinstance(card.__face__, str):
                faceIsStr = False

        self.assertTrue(faceIsStr)

    def test_card_faces_of_numeric_cards_are_all_str(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=False)

        testDeck.__generate_numeric_cards__()

        faceIsStr = True

        for card in testDeck.__deck__:
            if not isinstance(card.__face__, str):
                faceIsStr = False

        self.assertTrue(faceIsStr)

    def test_fcn_face_cards_are_of_value_10(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=False)

        faceCardValueIs10 = True

        for card in testDeck.__deck__:
            # Skip the Ace
            if not card.__is_ace__:
                if not (card.__value__ == 10):
                    faceCardValueIs10 = False
                    break

        self.assertTrue(faceCardValueIs10)


    def test_ace_generated(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=True)


        aceInDeck = False

        for card in testDeck.__deck__:
            if card.__is_ace__:
                aceInDeck = True

        self.assertTrue(aceInDeck)

    def test_ace_value_is_11(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=True)

        valueOfAce = 0

        for card in testDeck.__deck__:
            if card.__is_ace__:
                valueOfAce = card.__value__

        self.assertEqual(valueOfAce, 11)

    def test_only_one_ace_card_is_generated(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=True)

        numberOfAcesInDeck = 0

        for card in testDeck.__deck__:
            if card.__is_ace__:
                numberOfAcesInDeck = numberOfAcesInDeck + 1

        self.assertEqual(numberOfAcesInDeck, 1)

class TestCardGetterAndSetter(unittest.TestCase):

    def test_get_card_returns_a_card(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=True)

        cardFromDeck = testDeck.get_card()

        self.assertIsInstance(cardFromDeck, Card)

    def test_get_card_returns_a_card_from_deck(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=True)

        cardFromDeck = testDeck.get_card()

        self.assertIn(cardFromDeck, testDeck.__deck__)

    def test_get_card_returns_a_card(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=True)

        cardFromDeck = testDeck.get_hidden_card()

        self.assertIsInstance(cardFromDeck, Card)

    def test_get_hidden_card_returns_a_hidden_card(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=True)

        cardFromDeck = testDeck.get_hidden_card()

        self.assertTrue(cardFromDeck.__is_hidden__)


    def test_get_hidden_card_returns_copy_of_a_card_from_deck(self):
        from src.deck import Deck
        from src.deck import Card

        testDeck = Deck(generate=True)

        cardFromDeck = testDeck.get_hidden_card()

        self.assertNotIn(cardFromDeck, testDeck.__deck__)

if __name__ == "__main__":
    unittest.main()