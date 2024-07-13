import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise13(CustomTestCase):

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
        Detects duplicate in a list with a repeated number at the end.
        """
        inputs = ['1 4 5 0 2 4']
        output = self.run_exercise(inputs)
        expected_output = "duplicate list"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Confirms all numbers are unique in a short list.
        """
        inputs = ['1 6 9 10']
        output = self.run_exercise(inputs)
        expected_output = "is unique sequence"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Detects duplicate in a longer list with the duplicate at the beginning and end.
        """
        inputs = ['2 3 4 5 6 7 8 9 1 2']
        output = self.run_exercise(inputs)
        expected_output = "duplicate list"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Confirms all numbers are unique in a sequential list.
        """
        inputs = ['0 1 2 3 4 5']
        output = self.run_exercise(inputs)
        expected_output = "is unique sequence"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Detects duplicate when all numbers are the same.
        """
        inputs = ['7 7 7 7']
        output = self.run_exercise(inputs)
        expected_output = "duplicate list"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Confirms uniqueness in a list with negative numbers.
        """
        inputs = ['-1 -2 -3 -4']
        output = self.run_exercise(inputs)
        expected_output = "is unique sequence"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Detects duplicate in a list with both positive and negative duplicates.
        """
        inputs = ['-1 1 2 3 -1']
        output = self.run_exercise(inputs)
        expected_output = "duplicate list"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Confirms uniqueness in a list with a single number.
        """
        inputs = ['42']
        output = self.run_exercise(inputs)
        expected_output = "is unique sequence"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Detects duplicate in a list with non-sequential duplicates.
        """
        inputs = ['5 6 7 8 9 5 10']
        output = self.run_exercise(inputs)
        expected_output = "duplicate list"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Confirms uniqueness in a mixed list of positive and negative numbers.
        """
        inputs = ['-10 -20 30 40 50']
        output = self.run_exercise(inputs)
        expected_output = "is unique sequence"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
