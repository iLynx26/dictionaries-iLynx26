import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise2(CustomTestCase):

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
        Tests with a mix of letters, digits, and other characters.
        """
        inputs = ['Project Gutenberg offers over 59,000 free eBooks']
        output = self.run_exercise(inputs)
        expected_output = "LETTERS 36
DIGITS 5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Tests with a mix of letters and digits.
        """
        inputs = ['123abc456def']
        output = self.run_exercise(inputs)
        expected_output = "LETTERS 6
DIGITS 6"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Tests with digits only.
        """
        inputs = ['9876543210']
        output = self.run_exercise(inputs)
        expected_output = "LETTERS 0
DIGITS 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Tests with letters only.
        """
        inputs = ['abcdefghijklmnopqrstuvwxyz']
        output = self.run_exercise(inputs)
        expected_output = "LETTERS 26
DIGITS 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Tests with empty string.
        """
        inputs = ['']
        output = self.run_exercise(inputs)
        expected_output = "LETTERS 0
DIGITS 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Tests with special characters and spaces only.
        """
        inputs = ["!@#$%^&*() _+-=[]{}|;':,.<>/?`~"]
        output = self.run_exercise(inputs)
        expected_output = "LETTERS 0
DIGITS 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Tests with uppercase letters and digits.
        """
        inputs = ['ABC123']
        output = self.run_exercise(inputs)
        expected_output = "LETTERS 3
DIGITS 3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Tests with a long string of mixed characters.
        """
        inputs = ['The quick brown fox jumps over the lazy dog 1234567890']
        output = self.run_exercise(inputs)
        expected_output = "LETTERS 35
DIGITS 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Tests with numbers written in words.
        """
        inputs = ['One two three four five']
        output = self.run_exercise(inputs)
        expected_output = "LETTERS 19
DIGITS 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Tests with alphanumeric codes.
        """
        inputs = ['Code1234Test5678']
        output = self.run_exercise(inputs)
        expected_output = "LETTERS 8
DIGITS 8"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
