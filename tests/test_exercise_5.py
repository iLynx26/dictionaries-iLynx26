import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise5(CustomTestCase):

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
        Test with uppercase letter at the start of the alphabet.
        """
        inputs = A
        output = self.run_exercise(inputs)
        expected_output = ".-"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Test with lowercase letter at the end of the alphabet.
        """
        inputs = z
        output = self.run_exercise(inputs)
        expected_output = "--.."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Test with uppercase letter in the middle of the alphabet.
        """
        inputs = M
        output = self.run_exercise(inputs)
        expected_output = "--"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Test with lowercase letter in the middle of the alphabet.
        """
        inputs = n
        output = self.run_exercise(inputs)
        expected_output = "-."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Test with letter that has a longer Morse code.
        """
        inputs = Q
        output = self.run_exercise(inputs)
        expected_output = "--.-"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Test with letter that has a shorter Morse code.
        """
        inputs = E
        output = self.run_exercise(inputs)
        expected_output = "."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Test with numeric input (invalid).
        """
        inputs = 1
        output = self.run_exercise(inputs)
        expected_output = "Invalid input"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Test with special character input (invalid).
        """
        inputs = @
        output = self.run_exercise(inputs)
        expected_output = "Invalid input"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Test with empty string input (invalid).
        """
        inputs = 
        output = self.run_exercise(inputs)
        expected_output = "Invalid input"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Test with multiple characters input (invalid).
        """
        inputs = AB
        output = self.run_exercise(inputs)
        expected_output = "Invalid input"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
