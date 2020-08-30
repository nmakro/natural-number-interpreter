import unittest
from unittest.mock import patch
from .context import utils


class UtilsTest(unittest.TestCase):

    def setUp(self) -> None:
        patcher = patch("number_interpreter.utils.sys")
        self.mock_sys = patcher.start()

    def tearDown(self) -> None:
        self.mock_sys.stop()

    def test_interpreter_accepts_only_numbers(self):
        self.assertRaises(utils.RetryNeeded, utils.validate_input, "123123asd")

    def test_interpreter_accepts_numbers_per_three(self):
        self.assertRaises(utils.RetryNeeded, utils.validate_input, "1234 123")

    def test_interpreter_validates_greek_numbers(self):
        self.assertTrue("VALID", utils.is_greek_number("00306972413502"))
        self.assertTrue("VALID", utils.is_greek_number("2106930664"))
        self.assertTrue("INVALID", utils.is_greek_number("00316972413502"))
        self.assertTrue("INVALID", utils.is_greek_number("2116930664"))


if __name__ == '__main__':
    unittest.main()
