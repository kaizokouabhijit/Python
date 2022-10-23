import unittest
import pytest


def check_Palindrome(N):
    temp = N
    rev = 0
    while (N!=0):
        n = N%10
        rev = rev*10+n
        N = N//10
    return rev

# print(check_Palindrome(123))

@pytest.mark.parametrize("a, expected", [[54321, 12345], [121,121]])
def test_palindrome(a, expected):
    assert check_Palindrome(a) == expected