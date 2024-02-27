import sensors_main
import unittest
import sys # needed for setting the command line parameters for test cases
from unittest.mock import patch # needed for the integration test case


class TestSystem(unittest.TestCase):
    def test_start_sensors_main_with_incorrect_arguments(self):
        result = subprocess.run(['python', 'sensors_main.py', '22', '18'], capture_output=True, text=True)
        self.assertIn('Error: Incorrect command line arguments.', result.stdout)

if __name__ == '__main__':
    unittest.main()
