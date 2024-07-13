import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise1(CustomTestCase):

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
        Prints the name of the day for the entered ordinal number 3, which should be 'Wednesday'
        """
        inputs = [3]
        output = self.run_exercise(inputs)
        expected_output = "Wednesday"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Prints the name of the day for the entered ordinal number 0, which should be 'Sunday'
        """
        inputs = [0]
        output = self.run_exercise(inputs)
        expected_output = "Sunday"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Prints the name of the day for the entered ordinal number 5, which should be 'Friday'
        """
        inputs = [5]
        output = self.run_exercise(inputs)
        expected_output = "Friday"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Does not print any output for the entered ordinal number 7
        """
        inputs = [7]
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Prints the name of the day for the entered ordinal number 1, which should be 'Monday'
        """
        inputs = [1]
        output = self.run_exercise(inputs)
        expected_output = "Monday"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Prints the name of the day for the entered ordinal number 2, which should be 'Tuesday'
        """
        inputs = [2]
        output = self.run_exercise(inputs)
        expected_output = "Tuesday"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Prints the name of the day for the entered ordinal number 4, which should be 'Thursday'
        """
        inputs = [4]
        output = self.run_exercise(inputs)
        expected_output = "Thursday"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Prints the name of the day for the entered ordinal number 6, which should be 'Saturday'
        """
        inputs = [6]
        output = self.run_exercise(inputs)
        expected_output = "Saturday"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Prints the name of the day for the entered ordinal number 8, which should be 'Invalid input'
        """
        inputs = [8]
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Prints the name of the day for the entered ordinal number -1, which should be 'Invalid input'
        """
        inputs = [-1]
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
