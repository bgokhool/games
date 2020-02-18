"""
Unit Tests for the Sudoku class
"""
from sudoku_abstract import *
import unittest as u

class Sudoku(u.TestCase):

    def setUp(self):
        self.test_game = Sudoku()

    def tearDown(self):
        self.test_game = None

    def test_resetboard(self):
        actual_board = self.test_game.board
        expected_board = [[0,0,0,0,0,0,0,0,0] for i in range(9)]
        self.assertEqual(actual_board, expected_board, "Testing reseting board to zeros")

    def test_updateEntry(self):
        self.test_game.updateEntry(9,9,9)
        actual_board = self.test_game.board
        expected_board = [[0,0,0,0,0,0,0,0,0] for i in range(8)]
        expected_board.append([0,0,0,0,0,0,0,0,9])
        self.assertEqual(actual_board, expected_board, "Testing updating last entry of board to 9")

    def test_isValid_correct(self):
        self.assertTrue(self.test_game.isValid(1,1,1), "Testing isValid with correct\
         data on first row first entry")

    def test_isValid_incorrect(self):
        self.test_game.updateEntry(9,9,9)
        self.assertFalse(self.test_game.isValid(9,1,9), "Testing isValid with\
        incorrect data in last row last entry")


if __name__ == "__main__":
    u.main()
