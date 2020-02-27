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
import copy
from random import randint, choice
from search_problem import *

class Sudoku(ProblemState):
    """
    Sudoku class used to define a sudoku board for entertainment

    1. This Sudoku Class takes a board to create a game.

    Every method assumes both rows and columns range from index 0 to 8.
    This logic has to be kept in mind when calling this class in a main game
    module.

    """


    ENTRY = 0
    ROWS = COLUMNS = 9

    def __init__(self, boardState):
        """ Takes a Sudoku Board and creates a game """
        self.board = boardState

    def __str__(self):
        """
        return: string representation of the Sudoku Board

        If there is an operator, we add it to the string.
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


    def dictkey(self):
        """
        Returns a string that can be used as a dictionary key to
        represent unique states.
        This is basically similar to __str__ w/o the operator
        """
        result = ""
        for i in range(self.ROWS):
            if i != 0 and (i%3) == 0:
                result += "-"*17 + "\n"

            for j in range(self.COLUMNS):
                result += str(self.board[i][j])
                if j != (self.COLUMNS-1) and (j%3) == 2:
                    result += "|"
                elif j == (self.COLUMNS-1):
                    result += "\n"
                else:
                    result += ","
        return result

    def equals(self, other):
        """
        Tests whether the self (this) state instance
        equals the given other state.
        """
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if self.board[i][j] != other.board[i][j]:
                    return False
        return True

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


    def updateEntry(self, row, col, number):
        """
        Takes a number from 1 to 9 with a location in the grid given by a row
        number and a column number and updates the sudoku board with that
        number
        """
        self.board = self.newBoard(row, col, number)

    def newBoard(self, row, col, number):
        """
        Takes an index from 0 to 8 with a location in the grid given by a row
        index and a column index
        Creates an updated version the sudoku board with that number
        Returns the new board
        """
        updatedBoard = copy.deepcopy(self.board)
        updatedBoard[row][col] = number
        return updatedBoard

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
        Takes a number and a location on the sudoku board,
        i.e. a row index (0 to 8) and a column index (0 to 8),
        and verifies whether the given entry is allowed or not.

        return: True iff the number is allowed in that specific location
        """
        return self.__isValidGrid(row, col, number) and\
            self.__isValidRow(row, number) and\
            self.__isValidCol(col, number)

    def getFirstBlankEntry(self):
        """
        Returns a tuple of the index of the first blank entry or None otherwise
        """
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if self.board[i][j] == 0:
                    return (i,j)
        return None


    def successors(self):
        """
        Returns a list of valid successors to the current state.
        """
        indices = self.getFirstBlankEntry()
        result = []
        if indices is not None:
            row = indices[0]
            col = indices[1]
            for i in range(1, 10):
                if self.isValid(row, col, i):
                    succBoard = self.newBoard(row, col, i)
                    result.append(Sudoku(succBoard))
        return result



if __name__ == "__main__":
    # board = [[0 for j in range(9)] for i in range(9)]
    # print(Sudoku(board))
    pass
