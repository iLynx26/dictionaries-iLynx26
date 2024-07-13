import json
import os

# Example test data for each exercise
example_tests = [
    {
        "docstring": "Example test case 1",
        "inputs": ["example input 1"],
        "expected_output": "example output 1"
    },
    {
        "docstring": "Example test case 2",
        "inputs": ["example input 2"],
        "expected_output": "example output 2"
    },
    {
        "docstring": "Example test case 3",
        "inputs": ["example input 3"],
        "expected_output": "example output 3"
    }
]

# Function to create a JSON file for an exercise
def create_json_file(exercise_number):
    file_name = f"test_exercise_{exercise_number}.json"
    with open(file_name, 'w') as file:
        json.dump({"tests": example_tests}, file, indent=4)
    print(f"Created {file_name}")

# Create 38 JSON files
for i in range(2, 39):
    create_json_file(i)
