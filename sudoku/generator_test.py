from generator import *
import unittest as u
import copy

class SudokuPuzzleGenTest(u.TestCase):

    def test_get_mapping(self):
        """
        A general test to make sure that all the keys are mapped to different values
        """
        gen = SudokuPuzzleGen()
        s_map = gen.get_mapping()

        result = True
        for eachMap in s_map:
            r_map = copy.deepcopy(s_map)
            del r_map[eachMap]
            for restMap in r_map:
                if s_map[eachMap] == r_map[restMap]:
                    result = False

        self.assertTrue(result, "Correct one-to-one map received")

    def test_get_mapping_specific(self):
        """
        A specific test to check that all alphabet characters (from 'a' to 'i')
        are mapped to different integers (from 1 to 9)
        """
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        gen = SudokuPuzzleGen()
        s_map = gen.get_mapping()

        for alpha in alphabets:
            numbers.remove(s_map[alpha])

        self.assertTrue(len(numbers)==0, "Correct one-to-one map for specific test")

    def test_place_values(self):

        gen = SudokuPuzzleGen()
        gen.place_values()
        board = gen.getBoard()

        allNum = True
        for row in board:
            for col in row:
                if type(col) is not type(0):
                    allNum =False
        self.assertTrue(allNum, "Verify that all the board entries are numerical values")

    def test_rotate90(self):
        test_board = \
        [
            ['a', 'a', 'a',     'b', 'b', 'b',      'c', 'c', 'c'],
            ['a', 'a', 'a',     'b', 'b', 'b',      'c', 'c', 'c'],
            ['a', 'a', 'a',     'b', 'b', 'b',      'c', 'c', 'c'],

            ['d', 'd', 'd',     'e', 'e', 'e',      'f', 'f', 'f'],
            ['d', 'd', 'd',     'e', 'e', 'e',      'f', 'f', 'f'],
            ['d', 'd', 'd',     'e', 'e', 'e',      'f', 'f', 'f'],

            ['g', 'g', 'g',     'h', 'h', 'h',      'i', 'i', 'i'],
            ['g', 'g', 'g',     'h', 'h', 'h',      'i', 'i', 'i'],
            ['g', 'g', 'g',     'h', 'h', 'h',      'i', 'i', 'i'],
        ]

        result_board = SudokuPuzzleGen.rotate90(test_board)

        expected_board = \
        [
            ['g', 'g', 'g',     'd', 'd', 'd',      'a', 'a', 'a'],
            ['g', 'g', 'g',     'd', 'd', 'd',      'a', 'a', 'a'],
            ['g', 'g', 'g',     'd', 'd', 'd',      'a', 'a', 'a'],

            ['h', 'h', 'h',     'e', 'e', 'e',      'b', 'b', 'b'],
            ['h', 'h', 'h',     'e', 'e', 'e',      'b', 'b', 'b'],
            ['h', 'h', 'h',     'e', 'e', 'e',      'b', 'b', 'b'],

            ['i', 'i', 'i',     'f', 'f', 'f',      'c', 'c', 'c'],
            ['i', 'i', 'i',     'f', 'f', 'f',      'c', 'c', 'c'],
            ['i', 'i', 'i',     'f', 'f', 'f',      'c', 'c', 'c'],
        ]

        self.assertEqual(result_board, expected_board, "Correctly rotating board 90 deg clockwise")


    def test_rotate180(self):
        test_board = \
        [
            ['a', 'a', 'a',     'b', 'b', 'b',      'c', 'c', 'c'],
            ['a', 'a', 'a',     'b', 'b', 'b',      'c', 'c', 'c'],
            ['a', 'a', 'a',     'b', 'b', 'b',      'c', 'c', 'c'],

            ['d', 'd', 'd',     'e', 'e', 'e',      'f', 'f', 'f'],
            ['d', 'd', 'd',     'e', 'e', 'e',      'f', 'f', 'f'],
            ['d', 'd', 'd',     'e', 'e', 'e',      'f', 'f', 'f'],

            ['g', 'g', 'g',     'h', 'h', 'h',      'i', 'i', 'i'],
            ['g', 'g', 'g',     'h', 'h', 'h',      'i', 'i', 'i'],
            ['g', 'g', 'g',     'h', 'h', 'h',      'i', 'i', 'i'],
        ]

        result_board = SudokuPuzzleGen.rotate180(test_board)

        expected_board = \
        [
            ['i', 'i', 'i',     'h', 'h', 'h',      'g', 'g', 'g'],
            ['i', 'i', 'i',     'h', 'h', 'h',      'g', 'g', 'g'],
            ['i', 'i', 'i',     'h', 'h', 'h',      'g', 'g', 'g'],

            ['f', 'f', 'f',     'e', 'e', 'e',      'd', 'd', 'd'],
            ['f', 'f', 'f',     'e', 'e', 'e',      'd', 'd', 'd'],
            ['f', 'f', 'f',     'e', 'e', 'e',      'd', 'd', 'd'],

            ['c', 'c', 'c',     'b', 'b', 'b',      'a', 'a', 'a'],
            ['c', 'c', 'c',     'b', 'b', 'b',      'a', 'a', 'a'],
            ['c', 'c', 'c',     'b', 'b', 'b',      'a', 'a', 'a'],
        ]

        self.assertEqual(result_board, expected_board, "Correctly rotating board 180 deg clockwise")


    def test_rotate270(self):
        test_board = \
        [
            ['a', 'a', 'a',     'b', 'b', 'b',      'c', 'c', 'c'],
            ['a', 'a', 'a',     'b', 'b', 'b',      'c', 'c', 'c'],
            ['a', 'a', 'a',     'b', 'b', 'b',      'c', 'c', 'c'],

            ['d', 'd', 'd',     'e', 'e', 'e',      'f', 'f', 'f'],
            ['d', 'd', 'd',     'e', 'e', 'e',      'f', 'f', 'f'],
            ['d', 'd', 'd',     'e', 'e', 'e',      'f', 'f', 'f'],

            ['g', 'g', 'g',     'h', 'h', 'h',      'i', 'i', 'i'],
            ['g', 'g', 'g',     'h', 'h', 'h',      'i', 'i', 'i'],
            ['g', 'g', 'g',     'h', 'h', 'h',      'i', 'i', 'i'],
        ]

        result_board = SudokuPuzzleGen.rotate270(test_board)

        expected_board = \
        [
            ['c', 'c', 'c',     'f', 'f', 'f',      'i', 'i', 'i'],
            ['c', 'c', 'c',     'f', 'f', 'f',      'i', 'i', 'i'],
            ['c', 'c', 'c',     'f', 'f', 'f',      'i', 'i', 'i'],

            ['b', 'b', 'b',     'e', 'e', 'e',      'h', 'h', 'h'],
            ['b', 'b', 'b',     'e', 'e', 'e',      'h', 'h', 'h'],
            ['b', 'b', 'b',     'e', 'e', 'e',      'h', 'h', 'h'],

            ['a', 'a', 'a',     'd', 'd', 'd',      'g', 'g', 'g'],
            ['a', 'a', 'a',     'd', 'd', 'd',      'g', 'g', 'g'],
            ['a', 'a', 'a',     'd', 'd', 'd',      'g', 'g', 'g'],
        ]

        self.assertEqual(result_board, expected_board, "Correctly rotating board 270 deg clockwise")

    def test_reflect_horz(self):
        test_board = \
        [
            ['a', 'a', 'a',     'a', 'a', 'a',      'a', 'a', 'a'],
            ['b', 'b', 'b',     'b', 'b', 'b',      'b', 'b', 'b'],
            ['c', 'c', 'c',     'c', 'c', 'c',      'c', 'c', 'c'],

            ['d', 'd', 'd',     'd', 'd', 'd',      'd', 'd', 'd'],
            ['e', 'e', 'e',     'e', 'e', 'e',      'e', 'e', 'e'],
            ['f', 'f', 'f',     'f', 'f', 'f',      'f', 'f', 'f'],

            ['g', 'g', 'g',     'g', 'g', 'g',      'g', 'g', 'g'],
            ['h', 'h', 'h',     'h', 'h', 'h',      'h', 'h', 'h'],
            ['i', 'i', 'i',     'i', 'i', 'i',      'i', 'i', 'i'],
        ]

        result_board = SudokuPuzzleGen.reflect_horz(test_board)

        expected_board = \
        [
            ['i', 'i', 'i',     'i', 'i', 'i',      'i', 'i', 'i'],
            ['h', 'h', 'h',     'h', 'h', 'h',      'h', 'h', 'h'],
            ['g', 'g', 'g',     'g', 'g', 'g',      'g', 'g', 'g'],

            ['f', 'f', 'f',     'f', 'f', 'f',      'f', 'f', 'f'],
            ['e', 'e', 'e',     'e', 'e', 'e',      'e', 'e', 'e'],
            ['d', 'd', 'd',     'd', 'd', 'd',      'd', 'd', 'd'],

            ['c', 'c', 'c',     'c', 'c', 'c',      'c', 'c', 'c'],
            ['b', 'b', 'b',     'b', 'b', 'b',      'b', 'b', 'b'],
            ['a', 'a', 'a',     'a', 'a', 'a',      'a', 'a', 'a'],
        ]

        self.assertEqual(result_board, expected_board, "Correctly reflecting the board horizontally")

    def test_reflect_vert(self):
        test_board = \
        [
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],

            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],

            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
        ]

        result_board = SudokuPuzzleGen.reflect_vert(test_board)

        expected_board = \
        [
            ['i', 'h', 'g',     'f', 'e', 'd',      'c', 'b', 'a'],
            ['i', 'h', 'g',     'f', 'e', 'd',      'c', 'b', 'a'],
            ['i', 'h', 'g',     'f', 'e', 'd',      'c', 'b', 'a'],

            ['i', 'h', 'g',     'f', 'e', 'd',      'c', 'b', 'a'],
            ['i', 'h', 'g',     'f', 'e', 'd',      'c', 'b', 'a'],
            ['i', 'h', 'g',     'f', 'e', 'd',      'c', 'b', 'a'],

            ['i', 'h', 'g',     'f', 'e', 'd',      'c', 'b', 'a'],
            ['i', 'h', 'g',     'f', 'e', 'd',      'c', 'b', 'a'],
            ['i', 'h', 'g',     'f', 'e', 'd',      'c', 'b', 'a'],
        ]

        self.assertEqual(result_board, expected_board, "Correctly reflecting the board vertically")

    def test_swap_rows(self):
        test_board = \
        [
            ['a', 'a', 'a',     'a', 'a', 'a',      'a', 'a', 'a'],
            ['b', 'b', 'b',     'b', 'b', 'b',      'b', 'b', 'b'],
            ['c', 'c', 'c',     'c', 'c', 'c',      'c', 'c', 'c'],

            ['d', 'd', 'd',     'd', 'd', 'd',      'd', 'd', 'd'],
            ['e', 'e', 'e',     'e', 'e', 'e',      'e', 'e', 'e'],
            ['f', 'f', 'f',     'f', 'f', 'f',      'f', 'f', 'f'],

            ['g', 'g', 'g',     'g', 'g', 'g',      'g', 'g', 'g'],
            ['h', 'h', 'h',     'h', 'h', 'h',      'h', 'h', 'h'],
            ['i', 'i', 'i',     'i', 'i', 'i',      'i', 'i', 'i'],
        ]

        # Swap rows with a's and f's
        result_board = SudokuPuzzleGen.swap_rows(test_board, 0, 5)

        # Swap rows with g's and d's
        result_board = SudokuPuzzleGen.swap_rows(result_board, 6, 3)

        # Swap rows with b's and h's
        result_board = SudokuPuzzleGen.swap_rows(result_board, 1, 7)

        # Swap rows with c's and e's
        result_board = SudokuPuzzleGen.swap_rows(result_board, 2, 4)

        expected_board = \
        [
            ['f', 'f', 'f',     'f', 'f', 'f',      'f', 'f', 'f'],
            ['h', 'h', 'h',     'h', 'h', 'h',      'h', 'h', 'h'],
            ['e', 'e', 'e',     'e', 'e', 'e',      'e', 'e', 'e'],

            ['g', 'g', 'g',     'g', 'g', 'g',      'g', 'g', 'g'],
            ['c', 'c', 'c',     'c', 'c', 'c',      'c', 'c', 'c'],
            ['a', 'a', 'a',     'a', 'a', 'a',      'a', 'a', 'a'],

            ['d', 'd', 'd',     'd', 'd', 'd',      'd', 'd', 'd'],
            ['b', 'b', 'b',     'b', 'b', 'b',      'b', 'b', 'b'],
            ['i', 'i', 'i',     'i', 'i', 'i',      'i', 'i', 'i'],
        ]

        self.assertEqual(result_board, expected_board, "Testing swap_rows for rows 0->5, 6->3, 1->7, and 2->4")


    def test_swap_cols(self):
        test_board = \
        [
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],

            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],

            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
            ['a', 'b', 'c',     'd', 'e', 'f',      'g', 'h', 'i'],
        ]

        # Swap rows with a's and f's
        result_board = SudokuPuzzleGen.swap_cols(test_board, 0, 5)

        # Swap rows with g's and d's
        result_board = SudokuPuzzleGen.swap_cols(result_board, 6, 3)

        # Swap rows with b's and h's
        result_board = SudokuPuzzleGen.swap_cols(result_board, 1, 7)

        # Swap rows with c's and e's
        result_board = SudokuPuzzleGen.swap_cols(result_board, 2, 4)

        expected_board = \
        [
            ['f', 'h', 'e',     'g', 'c', 'a',      'd', 'b', 'i'],
            ['f', 'h', 'e',     'g', 'c', 'a',      'd', 'b', 'i'],
            ['f', 'h', 'e',     'g', 'c', 'a',      'd', 'b', 'i'],

            ['f', 'h', 'e',     'g', 'c', 'a',      'd', 'b', 'i'],
            ['f', 'h', 'e',     'g', 'c', 'a',      'd', 'b', 'i'],
            ['f', 'h', 'e',     'g', 'c', 'a',      'd', 'b', 'i'],
            
            ['f', 'h', 'e',     'g', 'c', 'a',      'd', 'b', 'i'],
            ['f', 'h', 'e',     'g', 'c', 'a',      'd', 'b', 'i'],
            ['f', 'h', 'e',     'g', 'c', 'a',      'd', 'b', 'i'],
        ]

        self.assertEqual(result_board, expected_board, "Testing swap_cols for cols 0->5, 6->3, 1->7, and 2->4")



if __name__ == "__main__":
    u.main()
