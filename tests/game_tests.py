import unittest

import sys

# sys.path.append('../')


class TestGameInit(unittest.TestCase):
    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)


    def test_player_is_type_player(self):
        from src.game import Game
        testGame = Game()

        from src.player import Player

        self.assertIsInstance(testGame.player, Player)

    def test_dealer_is_type_dealer(self):
        from src.game import Game
        testGame = Game()

        from src.dealer import Dealer

        self.assertIsInstance(testGame.dealer, Dealer)

    def test_deck_is_type_deck(self):
        from src.game import Game
        testGame = Game()

        from src.deck import Deck

        self.assertIsInstance(testGame.deck, Deck)


class TestNewRun(unittest.TestCase):

    def test_deal_to_player(self):
        from src.game import Game
        testGame = Game()

        testGame.__deal_to_plyr__()

        # Check player has two cards in hand
        numberOfCardsInPlayersHand = testGame.player.hand1.get_number_of_cards()

        self.assertEqual(numberOfCardsInPlayersHand, 2)

    def test_deal_to_dealer(self):
        from src.game import Game
        testGame = Game()

        testGame.__deal_to_dealer__()

        # Check dealer has two cards in hand
        numberOfCardsInDealersHand = testGame.dealer.hand1.get_number_of_cards()

        self.assertEqual(numberOfCardsInDealersHand, 2)

    def test_deal_to_dealer_and_player(self):
        from src.game import Game
        testGame = Game()

        testGame.new_run()

        # Check player and dealer have two cards in hand
        numberOfCardsInPlayersHand = testGame.player.hand1.get_number_of_cards()
        numberOfCardsInDealersHand = testGame.dealer.hand1.get_number_of_cards()
        TotalNumberOfCardsDealt = numberOfCardsInPlayersHand + numberOfCardsInDealersHand
        
        self.assertEqual(TotalNumberOfCardsDealt, 4)

    def test_dealers_2nd_card_is_hidden(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()

        dealerHand = testGame.dealer.hand1
        card2Status = dealerHand.hand[1].is_hidden()

        self.assertTrue(card2Status)



class TestHitPlayer(unittest.TestCase):

    def test_hit_player(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()

        testGame.hit_player()

        playerHand1 = testGame.player.hand1.get_number_of_cards()

        self.assertEqual(playerHand1, 3)

    def test_hit_player_only_did_not_add_to_hand2(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()

        testGame.hit_player()

        playerHand2 = testGame.player.hand2.get_number_of_cards()

        self.assertEqual(playerHand2, 0)

    def test_hit_player_in_split_hand1(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()
        testGame.split_player()

        testGame.hit_player()

        playerHand1 = testGame.player.hand1.get_number_of_cards()

        self.assertEqual(playerHand1, 3)
    
    def test_hit_player_in_split_hand2(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()
        testGame.split_player()

        testGame.hit_player()

        playerHand2 = testGame.player.hand2.get_number_of_cards()

        self.assertEqual(playerHand2, 3)


class TestSplitPlayer(unittest.TestCase):

    def test_split_status_is_set(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()
        testGame.split_player()

        playerSplitStatus = testGame.player.__get_split_status__()

    def test_player_is_delt_card_after_split_hand1(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()

        numberOfCardsHand1_beforeSplit = testGame.player.hand1.get_number_of_cards()
        numberOfCardsHand2_beforeSplit = testGame.player.hand2.get_number_of_cards()

        testGame.split_player()

        numberOfCardsHand1_afterSplit = testGame.player.hand1.get_number_of_cards()
        numberOfCardsHand2_afterSplit = testGame.player.hand2.get_number_of_cards()

        self.assertEqual(numberOfCardsHand1_beforeSplit, numberOfCardsHand1_afterSplit)

    def test_player_is_delt_card_after_split_hand2(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()

        numberOfCardsHand1_beforeSplit = testGame.player.hand1.get_number_of_cards()
        numberOfCardsHand2_beforeSplit = testGame.player.hand2.get_number_of_cards()

        testGame.split_player()

        numberOfCardsHand1_afterSplit = testGame.player.hand1.get_number_of_cards()
        numberOfCardsHand2_afterSplit = testGame.player.hand2.get_number_of_cards()

        self.assertNotEqual(numberOfCardsHand2_beforeSplit, numberOfCardsHand2_afterSplit)


class TestHitDealer(unittest.TestCase):

    def test_hit_dealer(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()

        testGame.hit_dealer()

        dealerHand1 = testGame.dealer.hand1.get_number_of_cards()

        self.assertEqual(dealerHand1, 3)

    def test_hit_dealer_did_not_add_to_hand2(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()

        testGame.hit_dealer()

        dealerHand2 = testGame.dealer.hand2.get_number_of_cards()

        self.assertEqual(dealerHand2, 0)


class TestDealerReveal(unittest.TestCase):

    def test_dealer_reveal(self):
        from src.game import Game
        testGame = Game()
        testGame.new_run()

        testGame.dealer_reveal(inTest=True)

        dealerHand = testGame.dealer.hand1
        card2Status = dealerHand.hand[1].is_hidden()

        self.assertFalse(card2Status)


class TestWinnerByBust(unittest.TestCase):

    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)



    def mock_game(self, hand1Value, hand2Value, dealerHandValue, inSplit):
        from src.game import Game
        testGame = Game()

        # Generate Dealer hand value
        for card in range(0, dealerHandValue):
            testGame.dealer.hand1.add_card(self.generateCard(value=1, face=str(1), is_ace=False))
        

        # Generate Hand1 Value
        for card in range(0, hand1Value): 
            testGame.player.hand1.add_card(self.generateCard(value=1, face=str(1), is_ace=False))

        # Generate Hand2 value
        for card in range(0, hand2Value): 
            testGame.player.hand2.add_card(self.generateCard(value=1, face=str(1), is_ace=False))


        if inSplit:
            # Set split status
            testGame.player.__set_split__()


        return testGame
    

    def test_dealer_bust_normal_master_fcn(self):
        testGame = self.mock_game(hand1Value=20, hand2Value=0, dealerHandValue=30, inSplit=False)

        player_bust_status = testGame.player.check_if_bust()
        dealer_bust_status = testGame.dealer.check_if_bust()
        
        outcome = testGame.__winner_by_bust__(player_bust_status, dealer_bust_status)

        self.assertEqual(outcome, testGame.winner())

    def test_plyr_bust_normal_master_fcn(self):
        testGame = self.mock_game(hand1Value=30, hand2Value=0, dealerHandValue=20, inSplit=False)

        player_bust_status = testGame.player.check_if_bust()
        dealer_bust_status = testGame.dealer.check_if_bust()
        
        outcome = testGame.__winner_by_bust__(player_bust_status, dealer_bust_status)


        self.assertEqual(outcome, testGame.bust())

    def test_plyr_both_tie_by_bust_normal_master_fcn(self):
        testGame = self.mock_game(hand1Value=30, hand2Value=29, dealerHandValue=28, inSplit=False)

        player_bust_status = testGame.player.check_if_bust()
        dealer_bust_status = testGame.dealer.check_if_bust()
        
        outcome = testGame.__winner_by_bust__(player_bust_status, dealer_bust_status)

        self.assertEqual(outcome, testGame.tie())



class TestWinnerByValue(unittest.TestCase):
    def generateCard(self, value=5, face=str(5), is_ace=False):
        from src.card import Card

        return Card(value=value, face=face, ace=is_ace)

    def mock_game(self, hand1Value, hand2Value, dealerHandValue, inSplit):
        from src.game import Game
        testGame = Game()

        # Generate Dealer hand value
        for card in range(0, dealerHandValue):
            testGame.dealer.hand1.add_card(self.generateCard(value=1, face=str(1), is_ace=False))
        

        # Generate Hand1 Value
        for card in range(0, hand1Value): 
            testGame.player.hand1.add_card(self.generateCard(value=1, face=str(1), is_ace=False))

        # Generate Hand2 value
        for card in range(0, hand2Value): 
            testGame.player.hand2.add_card(self.generateCard(value=1, face=str(1), is_ace=False))


        if inSplit:
            # Set split status
            testGame.player.__set_split__()


        return testGame
    
    def test_plyr_winner_hand1(self):
        testGame = self.mock_game(hand1Value=20, hand2Value=0, dealerHandValue=18, inSplit=False)

        dealer_hand_value = testGame.dealer.get_hand_value()
        hand_values = testGame.player.get_hand_value()
        hand1_value = testGame.player.hand1.get_hand_value()
        hand2_value = testGame.player.hand2.get_hand_value()
        player_in_split = testGame.player.__get_split_status__()

        outcome = testGame.__winner_by_value__(hand1_value, hand2_value, dealer_hand_value, player_in_split)

        self.assertEqual(outcome, testGame.winner())

    def test_plyr_winner_hand2(self):
        testGame = self.mock_game(hand1Value=17, hand2Value=20, dealerHandValue=18, inSplit=True)

        dealer_hand_value = testGame.dealer.get_hand_value()
        hand_values = testGame.player.get_hand_value()
        hand1_value = hand_values[0]
        hand2_value = hand_values[1]
        player_in_split = testGame.player.__get_split_status__()

        outcome = testGame.__winner_by_value__(hand1_value, hand2_value, dealer_hand_value, player_in_split)

        self.assertEqual(outcome, testGame.winner())

    def test_plyr_tie_hand1(self):
        testGame = self.mock_game(hand1Value=18, hand2Value=17, dealerHandValue=18, inSplit=False)

        dealer_hand_value = testGame.dealer.get_hand_value()
        hand_values = testGame.player.get_hand_value()
        hand1_value = testGame.player.hand1.get_hand_value()
        hand2_value = testGame.player.hand2.get_hand_value()
        player_in_split = testGame.player.__get_split_status__()

        outcome = testGame.__winner_by_value__(hand1_value, hand2_value, dealer_hand_value, player_in_split)

        self.assertEqual(outcome, testGame.tie())

    def test_plyr_tie_hand2(self):
        testGame = self.mock_game(hand1Value=17, hand2Value=18, dealerHandValue=18, inSplit=True)

        dealer_hand_value = testGame.dealer.get_hand_value()
        hand_values = testGame.player.get_hand_value()
        hand1_value = testGame.player.hand1.get_hand_value()
        hand2_value = testGame.player.hand2.get_hand_value()
        player_in_split = testGame.player.__get_split_status__()

        outcome = testGame.__winner_by_value__(hand1_value, hand2_value, dealer_hand_value, player_in_split)

        self.assertEqual(outcome, testGame.tie())



    def test_winner_hand1_while_tie_hand2_and_dealer(self):
        testGame = self.mock_game(hand1Value=20, hand2Value=18, dealerHandValue=18, inSplit=True)

        dealer_hand_value = testGame.dealer.get_hand_value()
        hand_values = testGame.player.get_hand_value()
        hand1_value = testGame.player.hand1.get_hand_value()
        hand2_value = testGame.player.hand2.get_hand_value()
        player_in_split = testGame.player.__get_split_status__()

        outcome = testGame.__winner_by_value__(hand1_value, hand2_value, dealer_hand_value, player_in_split)

        self.assertEqual(outcome, testGame.winner())


    def test_winner_hand2_while_tie_hand1_and_dealer(self):
        testGame = self.mock_game(hand1Value=18, hand2Value=19, dealerHandValue=18, inSplit=True)

        dealer_hand_value = testGame.dealer.get_hand_value()
        hand_values = testGame.player.get_hand_value()
        hand1_value = testGame.player.hand1.get_hand_value()
        hand2_value = testGame.player.hand2.get_hand_value()
        player_in_split = testGame.player.__get_split_status__()

        outcome = testGame.__winner_by_value__(hand1_value, hand2_value, dealer_hand_value, player_in_split)

        self.assertEqual(outcome, testGame.winner())


    def test_plyr_lost(self):
        testGame = self.mock_game(hand1Value=19, hand2Value=0, dealerHandValue=20, inSplit=False)

        dealer_hand_value = testGame.dealer.get_hand_value()
        # hand_values = testGame.player.get_hand_value()
        hand1_value = testGame.player.hand1.get_hand_value()
        hand2_value = testGame.player.hand2.get_hand_value()
        player_in_split = testGame.player.__get_split_status__()

        outcome = testGame.__winner_by_value__(hand1_value, hand2_value, dealer_hand_value, player_in_split)

        self.assertEqual(outcome, testGame.loose())


    def test_plyr_lost_split(self):
        testGame = self.mock_game(hand1Value=18, hand2Value=19, dealerHandValue=21, inSplit=True)

        dealer_hand_value = testGame.dealer.get_hand_value()
        hand_values = testGame.player.get_hand_value()
        hand1_value = testGame.player.hand1.get_hand_value()
        hand2_value = testGame.player.hand2.get_hand_value()
        player_in_split = testGame.player.__get_split_status__()

        outcome = testGame.__winner_by_value__(hand1_value, hand2_value, dealer_hand_value, player_in_split)

        self.assertEqual(outcome, testGame.loose())


if __name__ == "__main__":
    unittest.main()