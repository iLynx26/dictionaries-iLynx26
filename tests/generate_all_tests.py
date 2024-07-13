import json
import os


# Function to generate test file content from JSON data
def generate_test_file(test_data, exercise_number):
    # Template for the test file
    test_file_template = f"""import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise{exercise_number}(CustomTestCase):

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
        The program should not use the provided solution to solve 
        the exercise.
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
    return test_file_template


# Main script to generate all test files
def main():
    # Directory containing the JSON files
    json_directory = '.'  # Current directory

    # Iterate over each JSON file
    for json_file in os.listdir(json_directory):
        if json_file.startswith('test_exercise_') and \
                json_file.endswith('.json'):
            print(f"Generating test file from {json_file}")
            exercise_number = json_file.split('_')[-1].split('.')[0]
            with open(os.path.join(json_directory, json_file), 'r') as file:
                test_data = json.load(file)
                test_file_content = generate_test_file(test_data,
                                                       exercise_number)
                test_file_name = f'test_exercise_{exercise_number}.py'
                with open(os.path.join(json_directory, test_file_name),
                          'w') as test_file:
                    test_file.write(test_file_content)
            print(f"Generated {test_file_name} from {json_file}")


if __name__ == "__main__":
    main()
