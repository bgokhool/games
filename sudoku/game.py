"""
This class combines the Sudoku and SudokuPuzzleGen to randomly
generate a Sudoku Board.
"""
import copy
from random import randint, shuffle
from sudoku import *
from generator import *

class Game(Sudoku):

    EASY = 0
    MEDIUM = 1
    HARD = 2
    MAX_TRIES = 10

    def __init__(self, level):
        """
        Starts a Sudoku Game based on the level chosen

        Level specified from 0 to 2 corresponding to the level of difficulty:
            0 - Easy
            1 - Medium
            2 - Hard
        """
        self.solution = self.generateSolution()
        self.initPuzzle = self.generatePuzzle(level)
        initBoard = copy.deepcopy(self.initPuzzle)
        Sudoku.__init__(self, initBoard)

    def generateValuesToRemove(self, level):
        """
        Takes a level 0,1, or 2
        Returns number of values to remove from solution
        board to create new game
        """
        if level == self.EASY:
            valuesToRemove = randint(44, 47)
        elif level == self.MEDIUM:
            valuesToRemove = randint(49, 53)
        else:
            valuesToRemove = randint(54, 55)

        return valuesToRemove

    def generatePuzzle(self, level):
        """For now I will generate a prototype and use backtracking on it"""
        # puzzleBoard = copy.deepcopy(self.solution)
        # set_of_vals_to_rem = []
        # for _ in range(6):
        #     values_to_remove = list(range(9))
        #     shuffle(values_to_remove)
        #     set_of_vals_to_rem.append(values_to_remove)
        # for vals_to_rem in set_of_vals_to_rem:
        #     for i in range(9):
        #         if puzzleBoard[i][vals_to_rem[i]] != 0:
        #             puzzleBoard[i][vals_to_rem[i]] = 0
        # return puzzleBoard

        # this part of the code is in use right now
        toRemove = self.generateValuesToRemove(level)
        puzzleBoard = copy.deepcopy(self.solution)
        return self.generatePuzzleHelper(puzzleBoard, toRemove, 0)


    def generatePuzzleHelper(self, board, valuesToRemove, failedTries):
        """
        Recursively removes value and verifies unique
        solution using backtracking
        """
        if failedTries > self.MAX_TRIES:
            return board
        if valuesToRemove <= 0:
            return board
        else:
            randomRow = randint(0, 8)
            randomCol = randint(0, 8)
            newBoard = copy.deepcopy(board)
            newBoard[randomRow][randomCol] = 0
            initialState = Sudoku(newBoard, f"Removed Num at Row {randomRow+1}, Col {randomCol+1}")
            search = Search(initialState)
            numSolns = search.getNumSolns()

            if numSolns != 1:
                return self.generatePuzzleHelper(board, valuesToRemove, failedTries+1)
            else:
                return self.generatePuzzleHelper(newBoard, valuesToRemove-1, 0)


    def generateSolution(self):
        """ Returns a new complete Sudoku Puzzle created through generator """
        gen = SudokuPuzzleGen()
        return gen.getBoard()

    def clearBoard(self):
        """
        Takes a Sudoku board and clears it by removing all the entries that
        were previously added by the player
        """
        self.board = copy.deepcopy(self.initPuzzle)

if __name__ == "__main__":
    game = Game(0)
    # print(game)
    game.printBoard()
    Sudoku(game.solution).printBoard()
