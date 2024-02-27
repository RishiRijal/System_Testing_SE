import sensors_main
import unittest
from io import StringIO
import sys

class TestSystem(unittest.TestCase):

    def test_system_main(self):
        sys.argv = ['sensors_main.py', '16', '16']
        expected_output = "Error: Incorrect command line arguments.\n"
        
        sys.stdout = StringIO()
        
        sensors_main.main()
        output = sys.stdout.getvalue()

        sys.stdout = sys.__stdout__

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

