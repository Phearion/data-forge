import os
import unittest
from unittest.mock import patch, mock_open
from dotenv import load_dotenv
import openai

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, base_dir)
# pylint: disable=wrong-import-position
from main import OpenAIGenerator

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class TestOpenAIGenerator(unittest.TestCase):
    """
    Test class for OpenAIGenerator
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
            "first-step-iterations": 1,
            "second-step-iterations": 1,
            "themes_dict": {"maths": ["general", "matrices", "derivatives"]}
        }
        self.generator = OpenAIGenerator()
        self.response = None

    def tearDown(self):
        """
        Tear down method that does clean up after each test case has run.
        """

        self.generator = None

    def test_model(self):
        """
        Test the model method
        """

        prompt = "Bonjour, comment allez-vous ?"
        self.generator.model(prompt)

        self.assertGreater(len(self.response), 0)

    def test1_write_csv(self):
        """
        Test if the csv file is created
        """

        subject = "maths"
        self.generator.write_csv(subject)

        self.assertTrue(os.path.exists(f"src/datasets/generated/llama-{subject}-dataset.csv"))

    def test2_write_csv(self):
        """
        Test if the csv file is not empty
        """

        subject = "maths"
        self.generator.write_csv(subject)

        self.assertGreater(os.stat(f"src/datasets/generated/llama-{subject}-dataset.csv").st_size,
                           0)


if __name__ == '__main__':
    unittest.main()
