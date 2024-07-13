import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise9(CustomTestCase):

    def test_dict_usage(self):
        """
        The program should not use dictionaries to solve the exercise.
        """

        self.assertNoUsesDictionary()

    def test_function_usage(self):
        """
        The program should not use functions to solve the exercise.
        """

        self.assertNotUseSelfDefinedFunctions()

    def provided_soltuion_usage(self):
        """
        The program should not use the provided solution to solve 
        the exercise.
        """

        self.assertNotUsingProvidedSolution()

    def test_case_1(self):
        """
        Counts previous occurrences of words in a line with multiple repetitions.
        """
        inputs = ['var list set tuple list tuple tuple dict var']
        output = self.run_exercise(inputs)
        expected_output = "0 0 0 0 1 1 2 0 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Counts previous occurrences of words in a line with sequential repetitions.
        """
        inputs = ['hello world hello hello world']
        output = self.run_exercise(inputs)
        expected_output = "0 0 1 2 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Counts previous occurrences of words in a line with evenly distributed repetitions.
        """
        inputs = ['a b c a b c a b c']
        output = self.run_exercise(inputs)
        expected_output = "0 0 0 1 1 1 2 2 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Counts previous occurrences of words in a line with mixed repetitions.
        """
        inputs = ['one two one two three two four three']
        output = self.run_exercise(inputs)
        expected_output = "0 0 1 1 0 2 0 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Counts previous occurrences of words in a line with no repetitions.
        """
        inputs = ['unique words only here']
        output = self.run_exercise(inputs)
        expected_output = "0 0 0 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Counts previous occurrences of words in a line with a single word repeated.
        """
        inputs = ['repeat repeat repeat']
        output = self.run_exercise(inputs)
        expected_output = "0 1 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Counts previous occurrences of words in an empty line.
        """
        inputs = ['']
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Counts previous occurrences of words in a line with numbers as words.
        """
        inputs = ['1 2 3 1 2 3 1 2 3']
        output = self.run_exercise(inputs)
        expected_output = "0 0 0 1 1 1 2 2 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Counts previous occurrences of words in a line with a single word.
        """
        inputs = ['lonely']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Counts previous occurrences of words in a line with special characters as words.
        """
        inputs = ['! @ # ! @ #']
        output = self.run_exercise(inputs)
        expected_output = "0 0 0 1 1 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
