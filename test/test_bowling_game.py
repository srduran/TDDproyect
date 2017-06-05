"""
test bowling_game.py
"""

import unittest

from program import bowling_game

class GameTest(unittest.TestCase):

    def test_record_roll__knocked_down_7_pins__return_true(self):
        # arrange
        bowling_game_class = bowling_game.Game()

        # act
        for turns in range(20):
            bowling_game_class.record_roll(num_pins_knocked=4)
        get_score = bowling_game_class.get_score()

        # assert
        self.assertEqual(80, get_score)
