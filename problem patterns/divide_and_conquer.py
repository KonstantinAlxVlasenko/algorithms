"""Module Divide and Conquer"""

import unittest

def count_zeroes(lst):
    """
    Given a list of 1s and 0s which has all 1s first followed by all 0s.
    Function returns the number of zeroes in the list.
    Time complexity O(logn) 
    """
    
    # edge cases
    # an empty list or list of 1s
    if not lst or lst[-1] == 1:
        return 0
    # list of 0s
    elif lst[0] == 0:
        return len(lst)
    
    current_idx = 0
    # index of last met 1
    one_idx = 0
    # index of last met 0
    zero_idx = len(lst) - 1
    while True:
        # if 0 and 1 are neighbour elements
        if zero_idx - one_idx == 1:
            return len(lst) - zero_idx
        # if current element is 0
        if lst[current_idx] == 0:
            zero_idx = current_idx
            # move current index to the left 
            current_idx = int((current_idx - one_idx)/2) + one_idx
        else:
            one_idx = current_idx
            # move current index to the right
            current_idx = int((zero_idx - current_idx)/2) + current_idx 


def sorted_freq(lst, num):
    """
    Given a sorted list and number.
    Function counts the occurreneces of the number in the list.
    If number is not found returns -1. Time complexity O(logn) 
    
    """
    
    # if list empty 
    if not lst:
        return -1
    
    # find index where nums sequence starts
    start_idx = _search_idx(lst, num, 'start')
    # find index where nums sequence ends
    end_idx = _search_idx(lst, num, 'end')
    # if indexes were founded calculate num of nums in list
    if all([isinstance(idx, int) for idx in [start_idx, end_idx]]):
        return end_idx - start_idx + 1
    else:
        return -1
    

def _search_idx(lst, num, position = 'start'):
    """
    Helper function for sorted_freq function.
    Finds index in the list where nums sequence starts or ends depending on position parameter
    """
    
    # index on which num is in the list
    idx = None
    # if num is the last element of the list
    idx_end = False
    # check last element of the list since algoritm is not able to check it
    if lst[-1] == num:
        idx = len(lst) - 1
        idx_end = True
        
    # left border of list section to check    
    left = 0
    # right border of list section to check
    right = len(lst) - 1
        
    while True:
        # calculate current index (mean value between left and right borders)
        current_idx = int((right - left)/2) + left
        # num is found in the list
        if lst[current_idx] == num:
            # when looking for start index
            if position == 'start':
                # update num idx value
                idx = current_idx
                # move right border towards left border
                right = current_idx
            # when looking for end index
            elif position == 'end':
                # if num is not last element update idx value
                if not idx_end:
                    idx = current_idx
                # move left border towards right border
                left = current_idx
        # if current element is less then num in sorted list
        elif lst[current_idx] < num:
            # cut off left part of list till current element
            # (move right border towards left border)   
            left = current_idx
        # if current element is greater then num in sorted list
        else:
            # cut off right part of list till current element
            # (move right border towards left border) 
            right = current_idx
        # if current index reached beggining of the list
        # or element befor last element stop checking
        if current_idx in [0, len(lst) - 2]:
            break
        # if left and right list section borders are neighbour elements
        # stop checking 
        elif right - left == 1 and left > 0 and right < len(lst)-1:
            break
    
    return idx


def find_rotated_index(lst, num):
    """
    Function accepts a rotated list of sorted numbers and an integer.
    Function returns the index of the integer in the array.
    If the value is not found return -1.
    Time Complexity O(logN). Space Coplexity O(1)
    """
    
    if not lst:
        return None
    
    # find rotated index
    rotated_idx = _rotated_index(lst)
    
    if not rotated_idx:
        return None
    
    # if rotated index is found create sorted list out of lst
    sorted_lst = lst[rotated_idx:] + lst[:rotated_idx]
    # find num index in sorted list
    sorted_idx = _search_idx(sorted_lst, num)
    # offset for nums located in the left part of the lst (shift sorted list index to the left) 
    offset_left = len(lst[rotated_idx:])
    # offset for nums located in right part of the lst (shift sorted list index to the right)
    offset_right = len(lst[:rotated_idx])
    
    if sorted_idx == None:
        return -1
    
    # shift sorted list index of num
    # to offset_right value to the right for samller nums of lst
    if num <= lst[-1]:
        idx = sorted_idx + offset_right
    # to offset_left value to the left for larger nums of lst
    else:
        idx = sorted_idx - offset_left
    
    return idx


def _rotated_index(lst):
    """
    Helper function for find_rotated_index function.
    Finds an index of the list element which sorted list is rotated on.
    Example: [3,4,1,2]. Index 2. Time complexity O(logN)
    """
    
    first_element = lst[0]   
    left_edge = 0
    right_edge = len(lst) - 1
        
    while True:
        # calculate current index (mean value between left and right borders)
        current_idx = int((right_edge - left_edge)/2) + left_edge
        # if prev_element is greater than current_element then index of current_element is rotated index
        if lst[current_idx - 1] > lst[current_idx]:
            return current_idx
        # if current_element is greater than next_element then index of next elelemnt is rotated index
        elif lst[current_idx] > lst[current_idx + 1]:
            return current_idx + 1
        else:
            # if current_element is behind rotated part of list
            if lst[current_idx]  > first_element:
                left_edge = current_idx
            # if current_element is before rotated part of list
            elif lst[current_idx] < first_element:
                right_edge = current_idx
            
        # if [oXooooXo] indecies reached and no rotated index found then stop checking   
        if current_idx in [1, len(lst) - 2]:
            break
    
    return None


# tesing functions above
class CountUniqueValues(unittest.TestCase):


    def test_count_zeroes(self):
        self.assertEqual(count_zeroes([]), 0)
        self.assertEqual(count_zeroes([1,1,1,1,0,0]), 2)
        self.assertEqual(count_zeroes([1,0,0,0,0]), 4)
        self.assertEqual(count_zeroes([0,0,0]), 3)
        self.assertEqual(count_zeroes([1,1,1,1,1]), 0)
        
        
    def test_sorted_freq(self):
        self.assertEqual(sorted_freq([1,1,2,2,2,2,3], 2), 4)
        self.assertEqual(sorted_freq([1,1,2,2,2,2,3], 3), 1)
        self.assertEqual(sorted_freq([1,1,2,2,2,2,3], 1), 2)
        self.assertEqual(sorted_freq([1,1,2,2,2,2,3], 4), -1)
        
    
    def test_find_rotated_index(self):
        self.assertEqual(find_rotated_index([3, 4, 1, 2], 4), 1)
        self.assertEqual(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 8), 2)
        self.assertEqual(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 3), 6)
        self.assertEqual(find_rotated_index([37, 44, 66, 102, 10, 22], 14), -1)
        self.assertEqual(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 12), -1)
        self.assertEqual(find_rotated_index([11, 12, 13, 14, 15, 16, 3, 5, 7, 9], 16), 5)
        
        

    
if __name__ == '__main__':
    unittest.main()