import os
import unittest
import pandas as pd

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, base_dir)
# pylint: disable=wrong-import-position
from src.duplicates_verification import DuplicatesVerification


class TestDuplicatesVerification(unittest.TestCase):
    """
    Test class for DuplicatesVerification
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """

        file1 = os.path.join(base_dir, "src/datasets/generated/llama-maths-dataset.csv")
        file2 = os.path.join(base_dir, "src/datasets/generated/llama-physics-dataset.csv")
        file3 = os.path.join(base_dir, "src/datasets/bigbrain-dataset.csv")

        duplicates_verification1 = DuplicatesVerification(file1)
        duplicates_verification2 = DuplicatesVerification(file2)
        duplicates_verification3 = DuplicatesVerification(file3)

        duplicates_verification1.verify_duplicates()
        duplicates_verification2.verify_duplicates()
        duplicates_verification3.verify_duplicates()

        self.df1 = pd.read_csv(file1, sep=';')
        self.df2 = pd.read_csv(file2, sep=';')
        self.df3 = pd.read_csv(file3, sep=';')

    def tearDown(self):
        """
        Tear down method that does clean up after each test case has run.
        """

        self.df1 = None
        self.df2 = None
        self.df3 = None

    def test_duplicates_verification_file_1(self):
        """
        test case to check if duplicates are removed
        """

        self.assertEqual(self.df1.duplicated().sum(), 0)

    def test_duplicates_verification_file_2(self):
        """
        test case to check if duplicates are removed
        """

        self.assertEqual(self.df2.duplicated().sum(), 0)

    def test_duplicates_verification_file_3(self):
        """
        test case to check if duplicates are removed
        """

        self.assertEqual(self.df3.duplicated().sum(), 0)


if __name__ == '__main__':
    unittest.main()
