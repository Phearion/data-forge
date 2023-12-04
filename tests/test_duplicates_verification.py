import os
import unittest
from unittest import mock

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, base_dir)
# pylint: disable=wrong-import-position
from src.duplicates_verification import DuplicatesVerification


class TestDuplicatesVerification(unittest.TestCase):
    """
    Test class for DuplicatesVerification
    """

    def test_duplicates_verification(self):
        """
        test case to check if duplicates are removed
        """

        # create a mock file to test the duplicates verification
        mock_file = mock.mock_open(read_data="instruction;input;output\n"
                                             "What is 1+1?;1+1;2\n"
                                             "What is 1+1?;1+1;2\n"
                                             "What is 2+1?;2+1;3\n"
                                             "What is 3+1?;3+1;4\n"
                                             "What is 4+1?;4+1;5\n")

        # open the mock file
        with mock.patch('builtins.open', mock_file):
            duplicates_verification = DuplicatesVerification(file="mock.csv")
            duplicates_verification.verify_duplicates()


if __name__ == '__main__':
    unittest.main()
