import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise6(CustomTestCase):

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
        Tests with a date within the range.
        """
        inputs = ['2018', '5']
        output = self.run_exercise(inputs)
        expected_output = "YES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Tests with a date just before the range starts.
        """
        inputs = ['2014', '11']
        output = self.run_exercise(inputs)
        expected_output = "NO"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Tests with a date just after the range ends.
        """
        inputs = ['2019', '7']
        output = self.run_exercise(inputs)
        expected_output = "NO"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Tests with a date in the middle of the range.
        """
        inputs = ['2016', '3']
        output = self.run_exercise(inputs)
        expected_output = "YES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Tests with the start date of the range.
        """
        inputs = ['2014', '12']
        output = self.run_exercise(inputs)
        expected_output = "YES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Tests with the end date of the range.
        """
        inputs = ['2019', '6']
        output = self.run_exercise(inputs)
        expected_output = "YES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Tests with a date far before the range starts.
        """
        inputs = ['2010', '1']
        output = self.run_exercise(inputs)
        expected_output = "NO"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Tests with a date far after the range ends.
        """
        inputs = ['2020', '12']
        output = self.run_exercise(inputs)
        expected_output = "NO"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Tests with a date very close to the start of the range.
        """
        inputs = ['2014', '12']
        output = self.run_exercise(inputs)
        expected_output = "YES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Tests with a date very close to the end of the range.
        """
        inputs = ['2019', '6']
        output = self.run_exercise(inputs)
        expected_output = "YES"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
