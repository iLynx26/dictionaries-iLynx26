import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise8(CustomTestCase):

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
        Counts occurrences of each character in a string with no spaces.
        """
        inputs = ['abcabcdfghj']
        output = self.run_exercise(inputs)
        expected_output = "a, 2\nb, 2\nc, 2\nd, 1\nf, 1\ng, 1\nh, 1\nj, 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Counts occurrences of each character including spaces.
        """
        inputs = ['hello world']
        output = self.run_exercise(inputs)
        expected_output = "h, 1\ne, 1\nl, 3\no, 2\n , 1\nw, 1\nr, 1\nd, 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Counts occurrences of each character in a string with repeating pairs.
        """
        inputs = ['aabbcc']
        output = self.run_exercise(inputs)
        expected_output = "a, 2\nb, 2\nc, 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Counts occurrences of each character in a string with multiple occurrences.
        """
        inputs = ['programming']
        output = self.run_exercise(inputs)
        expected_output = "p, 1\nr, 2\no, 1\ng, 2\nm, 2\na, 1\ni, 1\nn, 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Counts occurrences of each character in a string with uppercase and lowercase.
        """
        inputs = ['AaBbCcAa']
        output = self.run_exercise(inputs)
        expected_output = "A, 2\na, 2\nB, 1\nb, 1\nC, 1\nc, 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Counts occurrences of each character in a string with special characters.
        """
        inputs = ['!@#!!@#']
        output = self.run_exercise(inputs)
        expected_output = "!, 3\n@, 2\n#, 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Counts occurrences of each character in an empty string.
        """
        inputs = ['']
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Counts occurrences of each character in a string with numbers.
        """
        inputs = ['1122334455']
        output = self.run_exercise(inputs)
        expected_output = "1, 2\n2, 2\n3, 2\n4, 2\n5, 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Counts occurrences of each character in a string with a single character.
        """
        inputs = ['aaaaa']
        output = self.run_exercise(inputs)
        expected_output = "a, 5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Counts occurrences of each character in a string with mixed characters.
        """
        inputs = ['a1b2c3d4']
        output = self.run_exercise(inputs)
        expected_output = "a, 1\n1, 1\nb, 1\n2, 1\nc, 1\n3, 1\nd, 1\n4, 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
