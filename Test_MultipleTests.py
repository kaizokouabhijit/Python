import unittest

import pytest
import ArmstrongNumber
import ReverseANumber
import COuntDigits
import CheckPalindrome

class TestMultipleTest(unittest.TestCase):

    def test_ArmstrongNumber(self):
        self.assertEqual(ArmstrongNumber.IsArmstrongNumber(153), True)
    
    def test_ReverseNumber(self):
        self.assertEqual(ReverseANumber.reverse_number(123), 321)


    def test_countnumberofdigits(self):
        self.assertEqual(COuntDigits.count_digit(0), 1)
    
    # @pytest.mark.parametrize("a, expected", [[12345,54321],[121,121]])
    def test_CheckPalindrome(self):
        self.assertEqual(CheckPalindrome.check_Palindrome(321),123)

        # https://docs.pytest.org/en/7.1.x/how-to/parametrize.html#parametrizemark
        





