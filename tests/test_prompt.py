import os
import re
import unittest
from unittest.mock import patch, mock_open

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, base_dir)
# pylint: disable=wrong-import-position
from src.prompt import Prompt


class TestPrompt(unittest.TestCase):
    """
    Test class for Prompt
    """

    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open, read_data='data')
    def setUp(self, _, mock_json):  # pylint: disable=arguments-differ
        """
        Set up method to run before each test cases.
        """

        mock_json.return_value = {
            "dynamic-prompting": True,
            "dynamic-prompting-examples": 3,
            "themes_dict": {"maths": ["general", "matrices", "derivatives"]}
        }
        self.prompt = Prompt()
        self.file1 = os.path.join(base_dir, "src/datasets/manual/manual-questions-maths.csv")
        self.file2 = os.path.join(base_dir, "src/datasets/generated/llama-maths-dataset.csv")

    def tearDown(self):
        """
        Tear down method that does clean up after each test case has run.
        """

        self.prompt = None

    def test_dynamic_prompt(self):
        """
        Test case to check if dynamic prompt is generated
        """

        identifier = 1
        self.assertEqual(len(self.prompt.dynamic_prompt(self.file1, identifier)), 3)

        identifier = 2
        self.assertEqual(len(self.prompt.dynamic_prompt(self.file2, identifier)), 3)

    def test_get_prompt(self):
        """
        Test case to check if prompt is a string
        """

        subject = "maths"
        identifier = 1
        self.assertEqual(type(self.prompt.get_prompt(self.file1, subject, identifier)), str)

        self.assertTrue(
            re.search('instruction:', self.prompt.get_prompt(self.file1, subject, identifier)))
        self.assertTrue(
            re.search('input:', self.prompt.get_prompt(self.file1, subject, identifier)))
        self.assertTrue(
            re.search('output:', self.prompt.get_prompt(self.file1, subject, identifier)))

        identifier = 2
        self.assertEqual(type(self.prompt.get_prompt(self.file2, subject, identifier)), str)

        self.assertTrue(
            re.search('instruction:', self.prompt.get_prompt(self.file2, subject, identifier)))
        self.assertTrue(
            re.search('input:', self.prompt.get_prompt(self.file2, subject, identifier)))
        self.assertTrue(
            re.search('output:', self.prompt.get_prompt(self.file2, subject, identifier)))


if __name__ == '__main__':
    unittest.main()
