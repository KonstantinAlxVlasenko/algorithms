"""Module Recursion pattern"""

import unittest

def factorial(num):
    """Functions returns num factorial"""
    # base case 0!=1, 1!=1
    if num <= 1:
        return 1
    return num*factorial(num - 1)


def filter_odd(lst):
    """Function takes list of integers and returns list of odd numbers"""
    odd_lst = []
    if len(lst) == 0:
        return []
    # if number is odd add it to the list
    if lst[0] % 2 != 0:
        odd_lst.append(lst[0])

    # recursion
    # call function with sliced list
    odd_lst.extend(filter_odd(lst[1:]))

    return odd_lst

    
class TestRecursion(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(0), 1)

    def test_filter_odd(self):
        self.assertEqual(filter_odd([0,1,2,3,4,5,6,7]), [1,3,5,7])
        self.assertEqual(filter_odd([0,2,4,6]), [])
        self.assertEqual(filter_odd([1]), [1])

if __name__ == '__main__':
    unittest.main()