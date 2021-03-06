"""Module Sliding window pattern"""

import unittest

def max_sub_list(lst, n):
    """Function to calculate the maximum sum of n consecutive elements in the list
    Functions accepts list of integers and number of required consecutive elements
    
    Given an array of integers and a number. 
    Function finds the maximum sum of a subarray 
    with the length of the number passed to the function. 
    Subarray consist of consecutive elements from the original array. 
    """
    
    # check if all elements of the list are integers and not null
    if len(lst) != 0 and not all([isinstance(element, int) for element in lst]):
        return 'List has to contain integers only'
    # return None if n is not in permitted limit
    if n < 1 or n > len(lst):
        return None

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

    return max_sub_sum


def min_sublist_sum(lst, num):
    """
    Function accepts two parameters - an array of positive integers and a positive integer. 
    This function returns the minimal length of a contiguous subarray 
    of which the sum is greater than or equal to the integer passed to the function. 
    If there isn't one, returns 0 instead.
    """
    
    current_sum = 0
    min_len = None
    left_index = 0
    right_index = 0
    i = 1
    
    while left_index < len(lst):
        # if sum calculated on prev step is less than threshold(num)
        # and right_index hasn't reached end of list
        if current_sum < num and right_index < len(lst):
            # add value of list in right_index to prev sum (increase sum) 
            current_sum += lst[right_index]
            # move right_index to the right (extend window)
            right_index += 1
        # if sum calculated on prev step is greater than threshold(num)
        # temporary solution found
        elif current_sum >= num:
            # calculate current length of sublist with sum of elements greate or less then threshold 
            current_len = right_index - left_index
            # check if found sublist length is less then sublist length found on prev steps
            min_len = min(min_len, current_len) if min_len else current_len
            # substract value of list in left_index from prev sum (reduce sum)
            current_sum -= lst[left_index]
            # move left_index to the right (shrink window) 
            left_index += 1
        # if sum calculated on prev step is less than threshold(num)
        # but right_index reached the end of list then break 
        else:
            break
               
        i += 1
    
    return min_len if min_len else 0


def find_longest_substring(string):
    """Function accepts a string and returns the length 
    of the longest substring with all distinct characters.
    """
    # unique substring start index
    start_index = 0
    # longest unique substring length
    longest_len = 0
    # dictionary to store string chars indexes
    # if during looping over string chars met more then once value is ovwerritten
    char_index_dct = {}
    
    for char_index in range(len(string)):
        # current char in string
        char = string[char_index]
        
        if not char in char_index_dct:
            char_index_dct[char] = char_index
            # if char is last in the string and it's not duplicate
            # then calculate length of unique substring including last char
            if char_index == len(string) - 1:
                longest_len = max(longest_len, char_index - start_index + 1)
                
        # if char have been met already in string  
        else:           
            # if char is in dictionary check if start_index is less or equal than previous index 
            # of duplicated char. string is cut after previos index of duplicated char
            if start_index <= char_index_dct[char]:
                # calculate current unique substring lenghth and choose maximum
                longest_len = max(longest_len, char_index - start_index)
                # shift start index after index of duplicated char (cut the string)
                start_index = char_index_dct[char] + 1
                # ovwerrite char index with new value
                char_index_dct[char] = char_index
                
                # if char is last in the string calculate length of unique substring
                # including last char after start_index was shifted
                if char_index == len(string) - 1:
                    # calculate current unique substring lenghth and choose maximum
                    longest_len = max(longest_len, char_index - start_index + 1)
                               
            # if char is in dictionary but start_index is greater than 
            # previous index of duplicated char then update char index only
            else:                   
                char_index_dct[char] = char_index
                # if char is last in the string calculate length of unique substring including last char
                if char_index == len(string) - 1:                   
                    # calculate current unique substring lenghth and choose maximum
                    longest_len = max(longest_len, char_index - start_index + 1)
                                    
    return longest_len
                
    
        
     
            

# test func
class TestMaxSubList(unittest.TestCase):

    def test_max_sub_list(self):
        self.assertEqual(max_sub_list([1,2,5,2,8,1,5], 2), 10)
        self.assertEqual(max_sub_list([1,2,5,2,8,1,5], 4), 17)
        self.assertEqual(max_sub_list([4,2,1,6], 1), 6)
        self.assertEqual(max_sub_list([4,2,1,6,2], 4), 13)
        self.assertEqual(max_sub_list([], 4), None)
        self.assertEqual(max_sub_list(['dff', 'errt'], 2), 'List has to contain integers only')
        
    def test_min_sublist_sum(self):
        self.assertEqual(min_sublist_sum([2,3,1,2,4,3], 7), 2)
        self.assertEqual(min_sublist_sum([2,1,6,5,4], 9), 2)
        self.assertEqual(min_sublist_sum([3,1,7,11,2,9,8,21,62,33,19], 52), 1)
        self.assertEqual(min_sublist_sum([1,4,16,22,5,7,8,9,10], 39), 3)
        self.assertEqual(min_sublist_sum([1,4,16,22,5,7,8,9,10], 55), 5)
        self.assertEqual(min_sublist_sum([4,3,3,8,1,2,3], 11), 2)
        self.assertEqual(min_sublist_sum([1,4,16,22,5,7,8,9,10], 95), 0)
        self.assertEqual(min_sublist_sum([], 1), 0)
        
    def test_longest_substring(self):
        self.assertEqual(find_longest_substring(''), 0)
        self.assertEqual(find_longest_substring('rithmschool'), 7)
        self.assertEqual(find_longest_substring('thisisawesome'), 6)
        self.assertEqual(find_longest_substring('thecatinthehat'), 7)
        self.assertEqual(find_longest_substring('bbbbbb'), 1)
        self.assertEqual(find_longest_substring('longestsubstring'), 8)
        self.assertEqual(find_longest_substring('thisishowwedoit'), 6)
        self.assertEqual(find_longest_substring('abcdefgh'), 8)
        
                         
                         
if __name__ == '__main__':
    unittest.main()