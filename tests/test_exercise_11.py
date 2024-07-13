import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise11(CustomTestCase):

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
        Checks for previous occurrences in a sequence with mixed numbers.
        """
        inputs = ['4 6 1 8 4 9 0 1']
        output = self.run_exercise(inputs)
        expected_output = "NO\nNO\nNO\nNO\nYES\nNO\nNO\nYES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Checks for previous occurrences in a sequence with repeated numbers.
        """
        inputs = ['3 3 4 5 6 7 4 8 9 0']
        output = self.run_exercise(inputs)
        expected_output = "NO\nYES\nNO\nNO\nNO\nNO\nYES\nNO\nNO\nNO"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Checks for previous occurrences in a sequence with sequential numbers repeated.
        """
        inputs = ['1 2 3 4 5 1 2 3 4 5']
        output = self.run_exercise(inputs)
        expected_output = "NO\nNO\nNO\nNO\nNO\nYES\nYES\nYES\nYES\nYES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Checks for previous occurrences in a sequence with higher numbers repeated.
        """
        inputs = ['5 6 7 8 9 5 6 7 8 9']
        output = self.run_exercise(inputs)
        expected_output = "NO\nNO\nNO\nNO\nNO\nYES\nYES\nYES\nYES\nYES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Checks for previous occurrences in a sequence with no repetitions.
        """
        inputs = ['10 20 30 40 50']
        output = self.run_exercise(inputs)
        expected_output = "NO\nNO\nNO\nNO\nNO"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Checks for previous occurrences in a sequence with all numbers being the same.
        """
        inputs = ['2 2 2 2 2']
        output = self.run_exercise(inputs)
        expected_output = "NO\nYES\nYES\nYES\nYES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Checks for previous occurrences in a sequence with alternating numbers.
        """
        inputs = ['1 2 1 2 1 2']
        output = self.run_exercise(inputs)
        expected_output = "NO\nNO\nYES\nYES\nYES\nYES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Checks for previous occurrences in a sequence with a single number.
        """
        inputs = ['7']
        output = self.run_exercise(inputs)
        expected_output = "NO"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Checks for previous occurrences in a sequence with numbers in descending order.
        """
        inputs = ['9 8 7 6 5 4 3 2 1']
        output = self.run_exercise(inputs)
        expected_output = "NO\nNO\nNO\nNO\nNO\nNO\nNO\nNO\nNO"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Checks for previous occurrences in a sequence with numbers in ascending order but repeating in the middle.
        """
        inputs = ['1 2 3 2 1 4 5']
        output = self.run_exercise(inputs)
        expected_output = "NO\nNO\nNO\nYES\nYES\nNO\nNO"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
