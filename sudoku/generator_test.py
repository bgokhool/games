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







if __name__ == "__main__":
    u.main()
