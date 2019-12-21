"""Function to calculate the maximum sum of n consecutive elements in the list
Functions accepts list of integers and number of required consecutive elements"""

import unittest

def max_sub_list(lst, n):
    
    # check if all elements of the not null list are integers
    if len(lst) != 0 and not all([isinstance(element, int) for element in lst]):
        return 'List has to contain integers only'
    # return None if n is not in permitted limit
    if n < 1 or n > len(lst):
        return None

    print('\nlist:', lst, '\nn:', n)
    # calculate sum of first n elements
    current_sub_sum = sum(lst[:n])
    # initial maximum sum of n elements 
    max_sub_sum = current_sub_sum

    # iterate over list elements starting from element with index n
    for i in range(n, len(lst)):
        # calculate sum of next n elements by subtraction from
        # previous sum of n elements of first element and add index i element
        current_sub_sum = current_sub_sum - lst[i-n] + lst[i]
        # check if calculated sum is greater than maximum sum 
        if current_sub_sum > max_sub_sum:
            max_sub_sum = current_sub_sum
    print('max_sum:', max_sub_sum)

    return max_sub_sum


# test func
class TestMaxSubList(unittest.TestCase):

    def test_max_sub_list(self):
        self.assertEqual(max_sub_list([1,2,5,2,8,1,5], 2), 10)
        self.assertEqual(max_sub_list([1,2,5,2,8,1,5], 4), 17)
        self.assertEqual(max_sub_list([4,2,1,6], 1), 6)
        self.assertEqual(max_sub_list([4,2,1,6,2], 4), 13)
        self.assertEqual(max_sub_list([], 4), None)
        self.assertEqual(max_sub_list(['dff', 'errt'], 2), 'List has to contain integers only')

if __name__ == '__main__':
    unittest.main()