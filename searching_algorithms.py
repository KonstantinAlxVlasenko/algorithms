"""Module Searching algorithms"""

import unittest


def linear_search(lst, value):
    """Function accepts a list and a value, and returns the index 
    at which the value exists. If the value does not exist 
    in the list, return -1.
    """
    
    for i in range(len(lst)):
        if value == lst[i]:
            return i
        
    return -1


def binary_search(lst, value):
    """Function accepts a sorted list and a value 
    and returns the index at which the value exists. 
    Otherwise, return -1. 
    """
    left = 0
    right = len(lst) - 1
    middle = (right + left) // 2
    
    # check if searching value is in the middle index 
    # calculated on prev iteration
    while value != lst[middle] and left <= right:
        # check if value is less then
        # list value in middle index
        if value < lst[middle]:
            # right index is moved to index before middle
            # coz middle index has been checked during
            # entering the loop
            right = middle - 1
        # check if value is more then
        # list value in middle index
        else:
            # left index is moved to index after middle
            left = middle + 1
        # calculate new middle index 
        middle = (right + left) // 2
            
    return middle if value == lst[middle] else -1


def naive_string_search(string1, string2):
    """Function takes two strings and checks how many times repeats
    smaller inside the bigger.
    """
    
    if len(string1) == 0 or len(string2) == 0:
        return 0
    
    if len(string1) < len(string2):
        string1, string2 = string2, string1
    
    count = 0 
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string2[j] != string1[i+j]:
                break
            if j == len(string2) - 1:
                count += 1
            
    return count

def create_prefix_lst(string):
    """Auxiliary function to create prefix list
    used in KMP patterns matcing. Function finds
    if chars sequence in the string (suffix) is found from the
    start of the string as well (prefix). Used in kmp_string_search
    function
    """

    # left string index
    j = 0
    # first element in prefix list is always zero
    prefix_lst = [0]
    
    """Iterate over right indexes of string 
    starting from index 1. Left index char
    is compared with right index char
    """
    for i in range(1, len(string)):
        """if chars are not equal then new j index moved back 
        and takes value of prefix list element with index 'j-1'. 
        Checks are applied until chars equality found or left index
        moved back to start of the string 
        """
        while string[i] != string[j] and j != 0:
            j = prefix_lst[j-1]
        """If chars are equal prefix lst appeneded
        with index j+1 and j index incrimented"""
        if string[i] == string[j]:
            prefix_lst.append(j + 1)
            j += 1
        # If left index is at the start of the string but chars 
        # are still not equal append zero to the prefix list
        else:
            prefix_lst.append(0)
            
    return prefix_lst
            
            
def kmp_string_search(string1, string2):
    """Function takes two strings and checks how many times repeats
    smaller inside the bigger. 
    Knuth–Morris–Pratt(KMP) Pattern Matching(Substring search) algorithm applied
    https://www.youtube.com/watch?v=GTJr8OvyEVQ
    """
    
    if len(string1) == 0 or len(string2) == 0:
        return 0
    # string1 is the longest one
    if len(string1) < len(string2):
        string1, string2 = string2, string1
    
    # create prefix list for string2 
    prefix_lst = create_prefix_lst(string2)
    # string2 chars index
    j = 0
    # match counter
    count = 0
    
    for i in range(len(string1)):
        # check if chars at indexes i and j are not equal
        if string1[i] != string2[j]:
            # move j from index after suffix to index after prefix
            # if both present otherwise to the start of string2
            if j > 0:
                j = prefix_lst[j-1]
            # if index j is at the start of string2 do nothing
            else:
                continue
        """Check if chars at indexes i and j are equal.
        double 'if' allows check equality after j index has been
        moved to position after prefix but i index of string2
        is still at the same position 
        """  
        if string1[i] == string2[j]:
            """If equality is true for the last char of string2
            increase word counter and move j index
            to the start of string2
            """
            if j == len(string2) - 1:
                count += 1
                j = 0
            # if char is not the last char of string 2
            # move j index to the right
            else:
                j += 1
                          
    return count

class TestSearchingAlgorithms(unittest.TestCase):
    
    def test_linear_search(self):
        self.assertEqual(linear_search([10,15,20,25,30], 15), 1)
        self.assertEqual(linear_search([9,8,7,6,5,4,3,2,1,0], 4), 5)
        self.assertEqual(linear_search([100], 100), 0)
        self.assertEqual(linear_search([1,2,3,4,5], 6), -1)
        self.assertEqual(linear_search([9,8,7,6,5,4,3,2,1,0], 10), -1)
        self.assertEqual(linear_search([100], 200), -1)
        
    def test_binary_search(self):
        lst1 = [1, 2, 3, 4, 5]
        lst2 = [5, 6, 10, 13, 14, 
                18, 30, 34, 35, 37, 
                40, 44, 64, 79, 84, 
                86, 95, 96, 98, 99]
        self.assertEqual(binary_search(lst1, 2), 1)
        self.assertEqual(binary_search(lst1, 3), 2)
        self.assertEqual(binary_search(lst1, 5),4)
        self.assertEqual(binary_search(lst1, 6), -1)
        self.assertEqual(binary_search(lst2, 10), 2)
        self.assertEqual(binary_search(lst2, 95),16 )
        self.assertEqual(binary_search(lst2, 100), -1)
        
    def test_naive_string_searc(self):
        self.assertEqual(naive_string_search('qwertyasdfghqwerty', 'qwerty'), 2)
        self.assertEqual(naive_string_search('asdfghjk', 'zxcv'), 0)
        self.assertEqual(naive_string_search('asd', 'asdasdfghasd'), 3)
        self.assertEqual(naive_string_search('rt', ''), 0)
        
    def test_kmp_serach(self):
        self.assertEqual(kmp_string_search('qwertyasdfghqwerty', 'qwerty'), 2)
        self.assertEqual(kmp_string_search('asdfghjk', 'zxcv'), 0)
        self.assertEqual(kmp_string_search('asd', 'asdasdfghasd'), 3)
        self.assertEqual(kmp_string_search('rt', ''), 0)
        self.assertEqual(kmp_string_search('abxabcabcaby', 'abcaby'), 1)
        self.assertEqual(kmp_string_search('dabxabcabcaby', 'abcaby'), 1)

        
if __name__ == '__main__':
    unittest.main()