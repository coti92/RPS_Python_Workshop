from pkg.modules.victorychecker import VictoryChecker
from unittest.mock import patch, PropertyMock
import unittest
from io import StringIO

class PlayerTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_victory(self, mock_stdout):
        
        test = VictoryChecker('rock', 'paper', 'A', 'B')
        test.check_victory()
        
        assert mock_stdout.getvalue() == 'A has lost. B has won. Long live B!\n'