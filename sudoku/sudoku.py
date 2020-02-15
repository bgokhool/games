"""
This is module contains a Sudoku class used to play the famous game.
Sudoku game description:
    * It consists of a 9x9 grid.
    * A typical game contains a partially filled board and the objective
        is completely fill the board with numbers ranging from 1 to 9
    * The constraints are that every row, column, and consecutive 3x3 grid
        should have a number only once
Example of a partially filled initial board (underscore characters
represent a blank entry):

    1 _ 6 | _ _ 2 | 3 _ _
    _ 5 _ | _ _ 6 | _ 9 1
    _ _ 9 | 5 _ 1 | 4 6 2
    =====================
    _ 3 7 | 9 _ 5 | _ _ _
    5 8 1 | _ 2 7 | 9 _ _
    _ _ _ | 4 _ 8 | 1 5 7
    =====================
    _ _ _ | 2 6 _ | 5 4 _
    _ _ 4 | 1 5 _ | 6 _ 9
    9 _ _ | 8 7 4 | 2 1 _

Corresponding solution board:

    1 4 6 | 7 9 2 | 3 8 5
    2 5 8 | 3 4 6 | 7 9 1
    3 7 9 | 5 8 1 | 4 6 2
    =====================
    4 3 7 | 9 1 5 | 8 2 6
    5 8 1 | 6 2 7 | 9 3 4
    6 9 2 | 4 3 8 | 1 5 7
    =====================
    7 1 3 | 2 6 9 | 5 4 8
    8 2 4 | 1 5 3 | 6 7 9
    9 6 5 | 8 7 4 | 2 1 3

The class first creates an empty board (where blank entries will be
represented by zeros).
A player is able to generate a new board depending on three levels of
difficulty:
    * Easy      (Generates a board with 34 ~ 37 entries already filled)
    * Medium    (Generates a board with 28 ~ 32 entries already filled)
    * Hard      (Generates a board with 26 ~ 27 entries already filled)


I will specify this as a Search Problem and use the Backtracking Search
Algorithm to generate a solution for any given board.

@author: Bhuwan (Ashvin) Gokhool
@version: Feb 2020
"""

import math
from random import randint, choice

class Sudoku:
    """ Sudoku class used to define a sudoku board for entertainement"""


    ENTRY = 0
    ROWS = COLUMNS = 9
    board = []

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

    def generate_start_values(self, level):
        """
        Takes an level from 0 to 2
        """
        if level == 0:
            return randint(34, 37)
        elif level == 1:
            return randint(28, 32)
        else:
            return randint(25, 28)


    def resetBoard(self):
        """
        Initializes the Sudoku board by adding zeros to the empty entries
        """
        for i in range(self.ROWS):
            row = []
            for j in range(self.COLUMNS):
                row.append(self.ENTRY)
            self.board.append(row)

    def clearBoard(reset):
        """
        Takes a Sudoku board and clears it by adding zeros to all the entries
        """
        self.resetBoard()


    def printBoard(self):
        """
        Formats and prints the Sudoku Board to the command line
        in a nice 9x9 grid
        """
        print("===========================")
        for i in range(self.ROWS):
            print("||", end=" ")
            for j in range(self.COLUMNS):
                print(self.board[i][j], end=" ")
                if j != (self.COLUMNS-1) and (j%3) == 2:
                    print("|", end=" ")
                if j == (self.COLUMNS-1):
                    print("||", end="\n")
            if i != (self.ROWS-1) and (i%3) == 2:
                print("---------------------------")

        print("===========================")

    def __str__(self):
        """
        return: string representation of the Sudoku str_board

        The entries are separated by a comma and the rows
        by a newline character
        """
        str_board = ""
        for i in range(self.ROWS):
            if i != 0 and (i%3) == 0:
                str_board += "-"*17 + "\n"

            for j in range(self.COLUMNS):
                str_board += str(self.board[i][j])
                if j != (self.COLUMNS-1) and (j%3) == 2:
                    str_board += "|"
                elif j == (self.COLUMNS-1):
                    str_board += "\n"
                else:
                    str_board += ","
        return str_board

    # needs more documentation on specific parameters that can be used
    # I also need to and error checking features, security of my code, make it more robust
    def updateEntry(self, row, col, number):
        """
        Takes a number from 1 to 9 with a location in the grid given by a row
        number and a column number and updates the sudoku board with that
        number
        """
        row_index = row-1
        col_index = col-1
        self.board[row_index][col_index] = number

    def __isValidRow(self, row, number):
        """
        Takes a number with the index of row (0 to 8)
        and verifies whether the given number is allowed in the given row

        return: True iff number is not already present in the row
        """
        for col in range(self.COLUMNS):
            if self.board[row][col] == number:
                return False
        return True

    def __isValidCol(self, col, number):
        """
        Takes a number with the index of column (0 to 8)
        and verifies whether the given number is allowed in the given column

        return: True iff number is not already present in the column
        """
        for row in range(self.ROWS):
            if self.board[row][col] == number:
                return False
        return True

    def __isValidGrid(self, row, col, number):
        """
        Takes a number with the index of its row (0 to 8) and the index
        of column (0 to 8).
        By figuring out which 3x3 grid the number belongs to it and verifies
        whether the given number is allowed in the given 3x3 grid

        return: True iff number is not already present in 3x3 grid
        """
        row_triplet = row//3
        col_triplet = col//3

        for row in range(3):
            for col in range(3):
                if number == self.board[row_triplet*3 + row][col_triplet*3 + col]:
                    return False
        return True

    def isValid(self, row, col, number):
        """
        Takes a number with coordinate location in the sudoku board,
        i.e. its row (1 to 9) and its column (1 to 9),
        and verifies whether the given entry is allowed or not.

        return: True iff the number is allowed in that specific location
        """
        row_index = row-1
        col_index = col-1
        return self.__isValidGrid(row_index, col_index, number) and\
            self.__isValidRow(row_index, number) and\
            self.__isValidCol(col_index, number)

    """
    METHODS AND VARIABLES TO GENERATE A NEW BOARD FROM A SOLUTION BOARD BELOW

    In solved_board, I have a possible solution of a Sudoku game.
    I have the numbers represented as alphabets because all we care about
    in Sudoku is that the entries are unique.
    I will there use this representation of the solution to generate a
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

    This is almost 2 Billion possibilites of solutions which should be more
    than enough for our puporses.
    """
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
                num = mapping[self.solved_board[row][col]]
                self.solved_board[row][col] = num

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




if __name__ == "__main__":
    game1 = Sudoku(1)
    print(game1)
    game1.board = Sudoku.rotate90(game1.board)
    print(game1)

    game1.board = Sudoku.rotate270(game1.board)
    print(game1)
