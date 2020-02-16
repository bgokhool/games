"""
METHODS AND VARIABLES TO GENERATE A NEW BOARD FROM A SOLUTION BOARD BELOW

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
from sudoku import *
from search_problem import *

class SudokuGame(Sudoku, ProblemState):
    """ Sudoku class used to define a sudoku board for entertainement"""

    solved_board = \
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

    unique_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    unique_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    def __init__(self, level):
        """
        Takes an INT number from 0 to 2 corresponding to the difficulty level
        and generates a Sudoku game based on that difficulty
        Level of difficulty:
            0 - Easy
            1 - Medium
            2 - Hard
        """
        self.level = level
        self.sum_start_values = self.generate_start_values(level)
        self.resetBoard()
        self.place_values()
        self.board = self.solved_board

    def updatedSudoku(self, row, col, number):
        """
        Takes a number from 0 to 8 with a location in the grid given by a row
        number and a column number and updates the sudoku board with that
        number
        """
        game = Sudoku()
        game.updateEntry(row+1, col+1, number)
        return game

    def getBlankIndex(self):
        """
        Returns a tuple of the index of the first blank entry or None otherwise
        """
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if self.board[i][j] == 0:
                    return (i,j)
        return None

    def applyOperators(self):
        """
        Returns a list of valid successors to the current state.
        """
        indices = self.getBlankIndex()
        result = []
        if indices not None:
            for i in range(1, 10):
                result.append(self.updatedSudoku(indices[0], indices[1], i))
        return result


    def clearBoard(self):
        """
        Takes a Sudoku board and clears it by removing all the entries that
        were previously added by the player
        """
        board = []
        for row in self.puzzle_board:
            new_row = row[:]
            board.append(new_row)
        self.board = board

    def genrate_soln_board(self):
        """
        Generates a random fully complete solution board based on
        above description
        """
        self.place_values(self)

    def get_mapping(self):
        """
        Returns a random created one-to-one map from alphabets to numbers
        """
        values_to_add = unique_values[:]
        mapping = {}
        count = 0
        while len(values_to_add) != 0:
            rand_val = choice(values_to_add)
            mapping[unique_symbols[count]] = rand_val
            values_to_add.remove(rand_val)
            count += 1
        return mapping

    def place_values(self):
        """
        Places numerical values on the Sudoku board to form a fully
        completed solution
        """
        mapping = self.get_mapping()
        for row in range(s.ROWS):
            for col in range(s.COLUMNS):
                num = mapping[solved_board[row][col]]
                solved_board[row][col] = num

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
        pass

    # static method
    def swap_cols(board, row1, row2):
        """
        Given a board representation and two col indices, verifies whether the
        two cols can be swapped and swaps them if they can be
        """
        pass
