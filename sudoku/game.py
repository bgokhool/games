"""
This class combines the Sudoku and SudokuPuzzleGen to randomly
generate a Sudoku Board.
"""
import copy
from random import randint
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
        self.solution = generateSolution()
        self.initPuzzle = self.generatePuzzle(level)
        self.board = copy.deepcopy(self.initPuzzle)


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
            newBoard[randomRow][randomCol] == 0
            initialState = Sudoku(newBoard)
            root = Node(initialState, None, 0)
            numSolns = Search(root)
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
