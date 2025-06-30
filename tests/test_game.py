import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from game import TicTacToe
class TestCheckWinner(unittest.TestCase):
    def testRowWin(self):
        game=TicTacToe()
        game.board = ['X', 'X', 'X',
                 ' ', 'O', ' ',
                 'O', ' ', ' ']
        self.assertEqual(game.checkWinner(),True)

    def testColWin(self):
        game=TicTacToe()
        game.board = ['O', 'X', ' ',
                 'O', 'X', ' ',
                 'O', ' ', 'X']
        self.assertEqual(game.checkWinner(),True)

    def testDiagWin(self):
        game=TicTacToe()
        game.board = ['O', 'X', 'X',
                 ' ', 'O', ' ',
                 ' ', ' ', 'O']
        self.assertEqual(game.checkWinner(),True)

    def testNoWin(self):
        game=TicTacToe()
        game.board = ['X', 'O', 'X',
                 'X', 'X', 'O',
                 'O', 'X', 'O']
        self.assertEqual(game.checkWinner(), False)

if __name__ == '__main__':
    unittest.main()