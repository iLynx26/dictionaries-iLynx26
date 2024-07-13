import json

# Load the test data from the JSON file
with open('test_exercise_1.json', 'r') as file:
    test_data = json.load(file)

# Template for the test file
test_file_template = """import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise1(CustomTestCase):

    def test_dict_usage(self):
        \"""
        The program should not use dictionaries to solve the exercise.
        \"""

        self.assertNoUsesDictionary()

    def test_function_usage(self):
        \"""
        The program should not use functions to solve the exercise.
        \"""

        self.assertNotUseSelfDefinedFunctions()

    def provided_soltuion_usage(self):
        \"""
        The program should not use the provided solution to solve the exercise.
        \"""

        self.assertNotUsingProvidedSolution()
"""

# Adding the test cases
for idx, test in enumerate(test_data["tests"], start=1):
    test_case = f"""
    def test_case_{idx}(self):
        \"""
        {test["docstring"]}
        \"""
        inputs = {test["inputs"]}
        output = self.run_exercise(inputs)
        expected_output = "{test["expected_output"]}"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)
    """
    test_file_template += test_case

# Ending the test file
test_file_template += """
if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
"""

# Write the test file
with open('test_exercise_1.py', 'w') as file:
    file.write(test_file_template)
