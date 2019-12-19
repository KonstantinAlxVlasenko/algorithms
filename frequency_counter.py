"""Function to determine if two given strings are anagram.
Anagram is a word, phrase, or name formed by rearranging the letters of another.
Second string is anagram to the first one (such as cinema and iceman).
Output is true or false.
"""

import unittest

def valid_anagram(str1: str, str2: str):
    # check if both parametsr are strings
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

if __name__ == '__main__':
    unittest.main()

