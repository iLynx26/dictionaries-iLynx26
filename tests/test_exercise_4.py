import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise4(CustomTestCase):

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
        Tests frequency count with repeated characters.
        """
        inputs = ['google']
        output = self.run_exercise(inputs)
        expected_output = "g 2\no 2\nl 1\ne 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Tests frequency count with a common greeting.
        """
        inputs = ['hello']
        output = self.run_exercise(inputs)
        expected_output = "h 1\ne 1\nl 2\no 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Tests frequency count with a programming language name.
        """
        inputs = ['python']
        output = self.run_exercise(inputs)
        expected_output = "p 1\ny 1\nt 1\nh 1\no 1\nn 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Tests frequency count with a string of alternating characters.
        """
        inputs = ['abcabc']
        output = self.run_exercise(inputs)
        expected_output = "a 2\nb 2\nc 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Tests frequency count with a single character.
        """
        inputs = ['aaaaa']
        output = self.run_exercise(inputs)
        expected_output = "a 5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Tests frequency count with a numeric string.
        """
        inputs = ['123321']
        output = self.run_exercise(inputs)
        expected_output = "1 2\n2 2\n3 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Tests frequency count with a mix of characters and numbers.
        """
        inputs = ['a1b2c3a3b2c1']
        output = self.run_exercise(inputs)
        expected_output = "a 2\n1 2\nb 2\n2 2\nc 2\n3 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Tests frequency count with uppercase and lowercase letters.
        """
        inputs = ['AaBbCc']
        output = self.run_exercise(inputs)
        expected_output = "A 1\na 1\nB 1\nb 1\nC 1\nc 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Tests frequency count with special characters.
        """
        inputs = ['!@!@']
        output = self.run_exercise(inputs)
        expected_output = "! 2\n@ 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Tests frequency count with an empty string.
        """
        inputs = ['']
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
