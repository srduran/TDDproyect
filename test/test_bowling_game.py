"""
test bowling_game.py
"""

import unittest

from program import bowling_game

class GameTest(unittest.TestCase):

    def test_get_score__knocked_down_4_pins__return_80(self):
        # arrange
        bowling_game_class = bowling_game.Game()

        # act
        for turns in range(20):
            bowling_game_class.record_roll(num_pins_knocked=4)
        get_score = bowling_game_class.get_score()

        # assert
        self.assertEqual(80, get_score)

    # def test_get_score__strike_first_roll_4_second_roll_3_third_roll_2_others_rolls__return_56(self):
    #     # arrange
    #     bowling_game_class = bowling_game.Game()
    #
    #     # act
    #     bowling_game_class.record_roll(num_pins_knocked=10)
    #     bowling_game_class.record_roll(num_pins_knocked=4)
    #     bowling_game_class.record_roll(num_pins_knocked=3)
    #     for turns in range(8):
    #         bowling_game_class.record_roll(num_pins_knocked=2)
    #         bowling_game_class.record_roll(num_pins_knocked=2)
    #     get_score = bowling_game_class.get_score()
    #
    #     # assert
    #     self.assertEqual(56, get_score)
