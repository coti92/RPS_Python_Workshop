from pkg.modules.player import Player
from unittest.mock import patch
import unittest
import builtins

class PlayerTest(unittest.TestCase):

    @patch('builtins.input', lambda *args: 'R')
    def test_player_hand(self):

        test_player = Player()

        hand = test_player.player_hand()

        assert hand == 'rock'   