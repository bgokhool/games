"""
CLASS USED TO GENERATE RANDOM UNIQUELY SOLVABLE SUDOKU PUZZLES

I will generate possible puzzles by removing values from an already
completely filled sudoku board.

In solved_board, I have a possible solution of a Sudoku game.
I have the numbers represented as alphabets because all we care about
in Sudoku is that the entries are unique.
I will, therefore, use this representation of the solution to generate a
concrete solution by mapping the alphabets to specific numbers.
Observe that this technique allows me to represent a unique alphabet
in 9 different ways, i.e. a can be 1 in one solution but 2 in another.
If we work out the math, this alone gives me 9! = 362880 possible solutions

Other ways to increase the number of solutions would be
    - to rotate the board 90, 180, 270 degrees
    - to reflect the entries along column 5 and/or row 5
    - switching between two rows as long  as both of them belong to the
        same triplet, i.e. switching any two of from rows 1-3 is valid,
        but not one from rows 1-3 and one from rows 4-6.
    - switching between two columns as long as both of them
        belong to the same triplet

After running through all of these variations, if I did the math correctly,
we should end up with around:
    9!*6*3*6*3*4*4 = 1 881 169 920

This is almost 2 Billion possibilites/permutations of solutions
which should be more than enough for our puporses. It is hard for people
to know that they might be solving the same puzzle.

"""

import math
import copy
from random import randint, choice
from sudoku import *

class SudokuPuzzleGen():
    """ Sudoku class used to define a sudoku board for entertainement"""

    ROWS = COLUMNS = 9

    REF_BOARD = \
    [
        ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
        ['f', 'i', 'h',     'g', 'b', 'c',      'd', 'e', 'a'],
        ['g', 'd', 'e',     'i', 'h', 'a',      'b', 'c', 'f'],

        ['b', 'g', 'd',     'e', 'a', 'i',      'h', 'f', 'c'],
        ['i', 'h', 'a',     'c', 'f', 'd',      'e', 'g', 'b'],
        ['c', 'e', 'f',     'b', 'g', 'h',      'a', 'i', 'd'],

        ['d', 'a', 'g',     'f', 'c', 'e',      'i', 'b', 'h'],
        ['h', 'f', 'b',     'a', 'i', 'g',      'c', 'd', 'e'],
        ['e', 'c', 'i',     'h', 'd', 'b',      'f', 'a', 'g'],
    ]

    # I tried putting COLUMNS and ROWS instead of hard-coding the value of 9
    # here, but I ran into the following error:
    # NameError: name 'COLUMNS' is not defined
    solved_board = [[0 for j in range(9)] for i in range(9)]

    unique_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    unique_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    # static method
    def rotate0(board):
        """
        This method does not change the board configuration at all
        It is just here for consistency
        """
        return board

    # static method
    def rotate90(board):
        """
        Given an n x n board representation
        Rotates the board 90 degrees clockwise
        """
        new_board = []
        cols = len(board[0])
        rows = len(board)
        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(board[-1-j][i])
            new_board.append(row)

        return new_board

    # static method
    def rotate180(board):
        """
        Given an n x n board representation
        Rotates the board 180 degrees clockwise
        """
        new_board = []
        for row in board:
            new_row = []
            for col in row:
                new_row.insert(0, col)
            new_board.insert(0, new_row)

        return new_board

    # static method
    def rotate270(board):
        """
        Given an n x n board representation
        Rotates the board 270 degrees clockwise
        """
        cols = len(board[0])
        rows = len(board)
        new_board = [[] for k in range(rows)]

        for i in range(rows):
            for j in range(cols):
                new_board[-1-j].append(board[i][j])

        return new_board

    def reflect_horz(board):
        """
        Given an n x n board representation
        Returns a new board that is the reflection of the board
        in a horizontal line about row 5 (the middle row)
        """
        new_board = []
        for row in board:
            new_row = row[:]
            new_board.insert(0, new_row)

        return new_board

    def reflect_vert(board):
        """
        Given an n x n board representation
        Returns a new board that is the reflection of the board
        in a vertical line about col 5 (the middle column)
        """
        new_board = []
        for row in board:
            new_row = []
            for col in row:
                new_row.insert(0, col)
            new_board.append(new_row)

        return new_board

    # static method
    def swap_rows(board, row1, row2):
        """
        Given a board representation and two row indices, verifies whether the
        two rows can be swapped and swaps them if they can be
        """
        assert row1//3 == row2//3, "Rows not in the same grid"

        new_board = copy.deepcopy(board)
        new_board[row1], new_board[row2] = new_board[row2], new_board[row1]
        return new_board

    # static method
    def swap_cols(board, col1, col2):
        """
        Given a board representation and two col indices, verifies whether the
        two cols can be swapped and swaps them if they can be
        """
        assert col1//3 == col2//3, "Cols not in the same grid"

        new_board = copy.deepcopy(board)
        for row in new_board:
            row[col1], row[col2] = row[col2], row[col1]
        return new_board

    RANDOM_ROT = [rotate90, rotate180, rotate270, rotate0]
    RANDOM_REF = [reflect_horz, reflect_vert, rotate0]



    def __init__(self):
        """
        Creates a completely solved board
        """
        self.genrate_soln_board()


    def getBoard(self):
        """ Returns a generated fully solved board """
        return self.solved_board

    def genrate_soln_board(self):
        """
        Generates a random fully complete solution board based on
        above description stored in the puzzle instance
        """
        self.place_values()
        randRotation = choice(self.RANDOM_ROT)
        self.solved_board = randRotation(self.solved_board)

        for _ in range(2):
            for i in range(2, 8, 3):
                row1 = randint(i-2,i)
                row2 = randint(i-2,i)
                self.solved_board = SudokuPuzzleGen.swap_rows(self.solved_board, row1, row2)

        for _ in range(2):
            for i in range(2, 8, 3):
                col1 = randint(i-2,i)
                col2 = randint(i-2,i)
                self.solved_board = SudokuPuzzleGen.swap_cols(self.solved_board, col1, col2)

        randReflection = choice(self.RANDOM_REF)
        self.solved_board = randReflection(self.solved_board)


    def get_mapping(self):
        """
        Returns a random created one-to-one map from alphabets to numbers
        """
        values_to_add = self.unique_values[:]
        mapping = {}
        count = 0
        while len(values_to_add) != 0:
            rand_val = choice(values_to_add)
            mapping[self.unique_symbols[count]] = rand_val
            values_to_add.remove(rand_val)
            count += 1
        return mapping

    def place_values(self):
        """
        Places numerical values on the Sudoku board to form a fully
        completed solution
        """
        mapping = self.get_mapping()
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                num = mapping[self.REF_BOARD[row][col]]
                self.solved_board[row][col] = num


if __name__ == "__main__":
    gen = SudokuPuzzleGen()
    game_sol = Sudoku(gen.getBoard())
    game_sol.printBoard()
