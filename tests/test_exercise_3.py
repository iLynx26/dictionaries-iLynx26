import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise3(CustomTestCase):

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
        Tests with a mix of uppercase, lowercase, and other characters.
        """
        inputs = ['The quick brown FOX jumps over a lazy DOG']
        output = self.run_exercise(inputs)
        expected_output = "UPPER CASE 7
LOWER CASE 26"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Tests with a simple greeting.
        """
        inputs = ['Hello World']
        output = self.run_exercise(inputs)
        expected_output = "UPPER CASE 2
LOWER CASE 8"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Tests with a mix of uppercase and lowercase in programming context.
        """
        inputs = ['PYTHON programming']
        output = self.run_exercise(inputs)
        expected_output = "UPPER CASE 6
LOWER CASE 11"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Tests with an equal mix of uppercase and lowercase letters.
        """
        inputs = ['ABCdefGHIjklMNO']
        output = self.run_exercise(inputs)
        expected_output = "UPPER CASE 9
LOWER CASE 6"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Tests with all uppercase letters.
        """
        inputs = ['UPPERCASE']
        output = self.run_exercise(inputs)
        expected_output = "UPPER CASE 9
LOWER CASE 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Tests with all lowercase letters.
        """
        inputs = ['lowercase']
        output = self.run_exercise(inputs)
        expected_output = "UPPER CASE 0
LOWER CASE 9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Tests with numbers and letters.
        """
        inputs = ['1234abcdEFGH']
        output = self.run_exercise(inputs)
        expected_output = "UPPER CASE 4
LOWER CASE 4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Tests with special characters and spaces.
        """
        inputs = ['!@#$%^&*() ABC abc']
        output = self.run_exercise(inputs)
        expected_output = "UPPER CASE 3
LOWER CASE 3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Tests with an empty string.
        """
        inputs = ['']
        output = self.run_exercise(inputs)
        expected_output = "UPPER CASE 0
LOWER CASE 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Tests with a long string of mixed characters.
        """
        inputs = ['Long String with MIXED Case Letters']
        output = self.run_exercise(inputs)
        expected_output = "UPPER CASE 6
LOWER CASE 23"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
