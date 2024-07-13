import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise7(CustomTestCase):

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
        Removes duplicates from a mixed list with multiple duplicates.
        """
        inputs = ['10 5 11 2 3 5 8 9 3 4 2']
        output = self.run_exercise(inputs)
        expected_output = "2 3 4 5 8 9 10 11"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Removes duplicates from a list where all elements are the same.
        """
        inputs = ['1 1 1 1 1 1']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Removes duplicates from a list that is in descending order.
        """
        inputs = ['5 4 3 2 1']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Removes duplicates from a list with pairs of duplicates.
        """
        inputs = ['2 2 3 3 4 4 5 5']
        output = self.run_exercise(inputs)
        expected_output = "2 3 4 5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Removes duplicates from a list with negative and positive integers.
        """
        inputs = ['-1 -2 -2 0 1 1']
        output = self.run_exercise(inputs)
        expected_output = "-2 -1 0 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Removes duplicates from a list with a single element.
        """
        inputs = ['7']
        output = self.run_exercise(inputs)
        expected_output = "7"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Removes duplicates from an empty list.
        """
        inputs = ['']
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Removes duplicates from a list with non-sequential duplicates.
        """
        inputs = ['1 3 5 7 9 1 3 5']
        output = self.run_exercise(inputs)
        expected_output = "1 3 5 7 9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Removes duplicates from a list with large numbers.
        """
        inputs = ['1000 2000 3000 2000 1000']
        output = self.run_exercise(inputs)
        expected_output = "1000 2000 3000"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Removes duplicates from a list with a mix of single and duplicate integers.
        """
        inputs = ['2 3 4 5 6 6 7 8 9 9']
        output = self.run_exercise(inputs)
        expected_output = "2 3 4 5 6 7 8 9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
