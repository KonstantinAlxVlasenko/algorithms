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


def power(base, exponent):
    """Function accepts a base and an exponent. 
    The function returns the power of the base to the exponent.
    """
    
    if exponent == 0:
        return 1
    return base*power(base, exponent - 1)


def list_product(lst):
    """Function takes list of numbers and returns the product of them all."""
    
    if len(lst) == 0:
        return 1
    
    return lst[0] * list_product(lst[1:])


def recursive_range(num):
    """Function accepts a number and adds up all the numbers 
    from 0 to the number passed to the function
    """
    if num == 0:
        return 0
    
    return num + recursive_range(num -1)
       
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
        
    def test_power(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(6, 2), 36)
        
    def list_product(self):
        self.assertEqual(list_product([1,2,3]), 6)
        self.assertEqual(list_product([1,2,3, 10]), 60)
        
    def test_recursive_range(self):
        self.assertEqual(recursive_range(6), 21)
        self.assertEqual(recursive_range(10), 55)

if __name__ == '__main__':
    unittest.main()