import unittest
from unittest.mock import patch
import main

# from robust_division_calculator import safe_divide

class TestDivision(unittest.TestCase):
    @patch("sys.argv", ["main.py", "10", "5"])
    def test_correct(self):
        with patch("builtins.print") as mocked_print:
            main.main()
            mocked_print.assert_called_with("The result of the division is 2.0")

    @patch("sys.argv", ["main.py", "10", "0"])
    def test_zero_division(self):
        with patch("builtins.print") as mocked_print:
            main.main()
            mocked_print.assert_called_with("Error: Cannot divide by zero.")

    @patch("sys.argv", ["main.py", "ten", "5"])
    def test_non_numeric(self):
        with patch("builtins.print") as mocked_print:
            main.main()
            mocked_print.assert_called_with("Error: Please enter numeric values only.")


if __name__ == "__main__":
    unittest.main()
