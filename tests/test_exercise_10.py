import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise10(CustomTestCase):

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
        Finds the synonym for a word with multiple synonym pairs.
        """
        inputs = ['3', 'Solar Heliac', 'Day Daytime', 'Arrive Occur', 'Heliac']
        output = self.run_exercise(inputs)
        expected_output = "Solar"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Finds the synonym for a word with two synonym pairs.
        """
        inputs = ['2', 'Happy Joyful', 'Sad Unhappy', 'Joyful']
        output = self.run_exercise(inputs)
        expected_output = "Happy"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Finds the synonym for a word in a list with mixed synonym pairs.
        """
        inputs = ['4', 'Big Large', 'Small Tiny', 'Fast Quick', 'Smart Intelligent', 'Quick']
        output = self.run_exercise(inputs)
        expected_output = "Fast"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Finds the synonym for a word with a single synonym pair.
        """
        inputs = ['1', 'Hot Warm', 'Warm']
        output = self.run_exercise(inputs)
        expected_output = "Hot"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Finds the synonym for a word where the synonym is the first word in the pair.
        """
        inputs = ['2', 'Begin Start', 'End Finish', 'Start']
        output = self.run_exercise(inputs)
        expected_output = "Begin"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Finds the synonym for a word where the synonym is the second word in the pair.
        """
        inputs = ['3', 'Light Bright', 'Dark Gloomy', 'Heavy Light', 'Gloomy']
        output = self.run_exercise(inputs)
        expected_output = "Dark"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Finds the synonym for a word with synonym pairs containing multi-word phrases.
        """
        inputs = ['2', 'Take off Depart', 'Land Arrive', 'Depart']
        output = self.run_exercise(inputs)
        expected_output = "Take off"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Finds the synonym for a word with synonym pairs and the word is a common term.
        """
        inputs = ['3', 'Cool Chill', 'Warm Cozy', 'Exciting Thrilling', 'Chill']
        output = self.run_exercise(inputs)
        expected_output = "Cool"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Finds the synonym for a word with synonym pairs including antonyms.
        """
        inputs = ['2', 'Empty Full', 'Full Empty', 'Empty']
        output = self.run_exercise(inputs)
        expected_output = "Full"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Finds the synonym for a word with synonym pairs including technical terms.
        """
        inputs = ['2', 'Function Method', 'Variable Parameter', 'Method']
        output = self.run_exercise(inputs)
        expected_output = "Function"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
