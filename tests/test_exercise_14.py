import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise14(CustomTestCase):

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
        Finds the country for cities across different countries.
        """
        inputs = ['5', 'UA Kyiv Zhytomyr Ternopil Dnipro', 'JP Tokyo Osaka Kyoto', 'CA Montreal Toronto Ottawa', 'USA Boston Pittsburgh Washington Seattle', 'UK London Edinburgh Cardiff Belfast', '3', 'Seattle', 'London', 'Kyiv']
        output = self.run_exercise(inputs)
        expected_output = "['USA', 'UK', 'UA']"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Identifies the country for cities in Asia.
        """
        inputs = ['3', 'IN Delhi Mumbai Bangalore', 'CN Beijing Shanghai Shenzhen', 'FR Paris Lyon Marseille', '2', 'Paris', 'Beijing']
        output = self.run_exercise(inputs)
        expected_output = "['FR', 'CN']"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Matches cities to their countries in Europe.
        """
        inputs = ['2', 'IT Rome Milan Naples', 'ES Madrid Barcelona Valencia', '3', 'Madrid', 'Rome', 'Naples']
        output = self.run_exercise(inputs)
        expected_output = "['ES', 'IT', 'IT']"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Finds the country for cities in Oceania and South America.
        """
        inputs = ['4', 'AU Sydney Melbourne Brisbane', 'NZ Auckland Wellington Christchurch', 'BR Rio Sao Paulo Brasilia', 'AR Buenos Aires Cordoba Rosario', '2', 'Sydney', 'Rio']
        output = self.run_exercise(inputs)
        expected_output = "['AU', 'BR']"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
