"""Module Frequency counter pattern"""

import unittest

def valid_anagram(str1: str, str2: str):
    """Function to determine if two given strings are anagram.
    Anagram is a word, phrase, or name formed by rearranging the letters of another.
    Second string is anagram to the first one (such as cinema and iceman).
    Output is true or false.
    """

    # check if both parameters are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False
    # return False if strings lengths are different 
    elif len(str1) != len(str2):
        return False
    # create to dictionaries from char in both strings and compare
    else:
        str1_dct = {}
        str2_dct = {}
        for char in str1:
            str1_dct[char] = str1_dct[char] + 1 if str1_dct.get(char) else 1
        for char in str2:
            str2_dct[char] = str2_dct[char] + 1 if str2_dct.get(char) else 1
      
    return str1_dct == str2_dct


def split_integer(num: int, lst=None):
    """Function to split integer to numbers.
    When func is called for the first time takes integer as parameter. List with splitted numbers is None.
    Every recursion step call func with integer reduced by one number from the right side 
    and list with cut numbers on previos iterations.
    """

    if not lst:
        lst = []
    # when func is called with integer less then 10 add it to list and stop recursion
    if num < 10:
        return lst.append(num)
    # add last digit of num to the list 
    lst.append(num%10)
    # cut last digit from num and call func
    split_integer(num//10, lst)

    return lst

 
def same_frequency(num1: int, num2: int):
    """Function to check if given two positive integers have the same frequency of digits.
    Returns True or False"""

    # check if both parametsr are integers
    if not isinstance(num1, int) or not isinstance(num2, int):
        return False

    num1_lst = split_integer(num1)
    num2_lst = split_integer(num2)
    # return False if lists length are different 
    if len(num1_lst) != len(num2_lst):
        return False
    # create to dictionaries from char in both strings and compare
    else:
        num1_dct = {}
        num2_dct = {}
        for digit in num1_lst:
            num1_dct[digit] = num1_dct[digit] + 1 if num1_dct.get(digit) else 1
        for digit in num2_lst:
            num2_dct[digit] = num2_dct[digit] + 1 if num2_dct.get(digit) else 1

    return num1_dct == num2_dct


# test valid_anagram function
class TestAnagram(unittest.TestCase):

    def test_true_anagram(self):
        self.assertTrue(valid_anagram('', ''))
        self.assertTrue(valid_anagram('anagram', 'nagaram'))
        self.assertTrue(valid_anagram('qwerty', 'qeywrt'))
        self.assertTrue(valid_anagram('texttwisttime', 'timetwisttext'))

    def test_false_anagram(self):
        self.assertFalse(valid_anagram('aaz', 'zza'))
        self.assertFalse(valid_anagram('rat', 'car'))
        self.assertFalse(valid_anagram('amanaplanacanalpanama', 'acanalmanplanpamana'))
        self.assertFalse(valid_anagram(2, 4))
        self.assertFalse(valid_anagram('fghj', 4))

    def test_true_freq(self):
        self.assertTrue(same_frequency(182, 281))
        self.assertTrue(same_frequency(3589578, 5879385))

    def test_false_freq(self):
        self.assertFalse(same_frequency(34, 14))
        self.assertFalse(same_frequency(22, 222))
        self.assertFalse(same_frequency('22', 222))

if __name__ == '__main__':
    unittest.main()

