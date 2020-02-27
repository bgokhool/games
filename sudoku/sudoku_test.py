"""
Unit Tests for the Sudoku class
"""
from sudoku import *
import unittest as u

class SudokuTest(u.TestCase):

    def setUp(self):
        board = [[0 for j in range(9)] for i in range(9)]
        self.test_game = Sudoku(board)

    def tearDown(self):
        self.test_game = None

    def test_resetboard(self):
        self.test_game.resetBoard()
        actual_board = self.test_game.board
        expected_board = [[0 for j in range(9)] for i in range(9)]
        self.assertEqual(actual_board, expected_board, "Testing reseting board to zeros")

    def test_updateEntry(self):
        self.test_game.updateEntry(8,8,9)
        actual_board = self.test_game.board
        expected_board = [[0,0,0,0,0,0,0,0,0] for i in range(8)]
        expected_board.append([0,0,0,0,0,0,0,0,9])
        self.assertEqual(actual_board, expected_board, "Testing updating last\
         entry (row 9, col 9) of board to 9")

    def test_toString(self):
        expected = "0,0,0|0,0,0|0,0,0\n0,0,0|0,0,0|0,0,0\n" +\
                    "0,0,0|0,0,0|0,0,0\n-----------------\n" +\
                    "0,0,0|0,0,0|0,0,0\n0,0,0|0,0,0|0,0,0\n" +\
                    "0,0,0|0,0,0|0,0,0\n-----------------\n" +\
                    "0,0,0|0,0,0|0,0,0\n0,0,0|0,0,0|0,0,0\n" +\
                    "0,0,0|0,0,0|0,0,0\n"
        actual = str(self.test_game)
        self.assertEqual(actual, expected, "Testing to string method")

    def test_dictkey(self):
        expected = "0,0,0|0,0,0|0,0,0\n0,0,0|0,0,0|0,0,0\n" +\
                    "0,0,0|0,0,0|0,0,0\n-----------------\n" +\
                    "0,0,0|0,0,0|0,0,0\n0,0,0|0,0,0|0,0,0\n" +\
                    "0,0,0|0,0,0|0,0,0\n-----------------\n" +\
                    "0,0,0|0,0,0|0,0,0\n0,0,0|0,0,0|0,0,0\n" +\
                    "0,0,0|0,0,0|0,0,0\n"
        actual = self.test_game.dictkey()
        self.assertEqual(actual, expected, "Testing dictkey method")

    def test_equals_correct(self):
        otherBoard = [[0 for j in range(9)] for i in range(9)]
        otherGame = Sudoku(otherBoard)
        self.assertTrue(self.test_game.equals(otherGame),\
         "Testing equals method with correct data")

    def test_equals_incorrect(self):
        otherBoard = [[1 for j in range(9)] for i in range(9)]
        otherGame = Sudoku(otherBoard)
        self.assertFalse(self.test_game.equals(otherGame),\
         "Testing equals method with incorrect data")

    def test_newBoard(self):
        board = [[0 for j in range(9)] for i in range(9)]
        game = Sudoku(board)
        new_board = game.newBoard(4, 4, 9)
        expected = new_board

        self.test_game.updateEntry(4, 4, 9)
        actual = self.test_game.board

        self.assertEqual(expected, actual, "Testing new board method")

    def test_isValid_correct_row(self):
        self.assertTrue(self.test_game.isValid(0,3,1), "Testing isValid with correct\
         data on first row at entry 0,3")

    def test_isValid_incorrect_row(self):
        self.test_game.updateEntry(8,8,5)
        self.test_game.updateEntry(8,1,6)
        self.assertFalse(self.test_game.isValid(8,2,5), "Testing isValid with\
        incorrect data in last row at entry 8,2")

    def test_isValid_correct_col(self):
        self.assertTrue(self.test_game.isValid(4,0,6), "Testing isValid with correct\
         data on first col at entry 4,0")

    def test_isValid_incorrect_col(self):
        self.test_game.updateEntry(1,4,9)
        self.test_game.updateEntry(4,4,2)
        self.assertFalse(self.test_game.isValid(8,4,9), "Testing isValid with\
        incorrect data in middle col at entry 8,4")

    def test_isValid_correct_grid(self):
        self.assertTrue(self.test_game.isValid(2,8,3), "Testing isValid with correct\
         data on 3rd grid (counting horizontally) at entry 2,8")

    def test_isValid_incorrect_grid(self):
        self.test_game.updateEntry(7,0,5)
        self.assertFalse(self.test_game.isValid(6,2,5), "Testing isValid with\
        incorrect data in 7th grid (counting horizontally) at entry 6,2")

    def test_getFirstBlank1(self):
        self.assertEqual(self.test_game.getFirstBlankEntry(), (0,0),\
        "Testing first blank entry")

    def test_getFirstBlank2(self):
        self.test_game.updateEntry(0,0,5)
        self.assertEqual(self.test_game.getFirstBlankEntry(), (0,1),\
        "Testing first blank entry to be second entry")

    def test_getFirstBlank3(self):
        for i in range(9):
            self.test_game.updateEntry(0,i,i+1)
        self.assertEqual(self.test_game.getFirstBlankEntry(), (1,0),\
        "Testing first blank entry on second row")

    def test_getFirstBlank4(self):
        for i in range(9):
            self.test_game.updateEntry(0,i,i+1)
            self.test_game.updateEntry(1,8-i,i+1)
        self.assertEqual(self.test_game.getFirstBlankEntry(), (2,0),\
        "Testing first blank entry on third row")

    def test_getFirstBlank5(self):
        for i in range(9):
            for j in range(9):
                self.test_game.updateEntry(i,j,j+1)
        self.assertEqual(self.test_game.getFirstBlankEntry(), None,\
        "Testing first blank entry does not exist")

    def test_successors(self):
        board = [[0 for j in range(9)] for i in range(9)]
        expected = []
        for i in range(9):
            board[0][0] = i+1
            new_board =copy.deepcopy(board)
            expected.append(Sudoku(new_board))
            
        actual = self.test_game.successors()
        values = map(lambda x,y: x.equals(y), expected, actual)
        values = list(values)
        result = True
        for value in values:
            result = result and value
        self.assertTrue(result, "Testing successors method")


if __name__ == "__main__":
    u.main()
