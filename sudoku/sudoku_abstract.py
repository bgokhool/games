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

class SudokuRules():
    """ Sudoku class used to define a sudoku board for entertainement"""


    ENTRY = 0
    ROWS = COLUMNS = 9
    board = []

    def __init__(self):
        """ Initializes an empty Sudoku Board """
        self.resetBoard()


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
        board = []
        for i in range(self.ROWS):
            row = []
            for j in range(self.COLUMNS):
                row.append(self.ENTRY)
            board.append(row)
        self.board = board


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



if __name__ == "__main__":
    pass
