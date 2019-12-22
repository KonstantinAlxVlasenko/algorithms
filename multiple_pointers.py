
"""Module Multiple pointers pattern"""

import unittest

def count_unique_values(lst):
    """Function which accepts an list with integers and counts unique values in the array"""

    # check if all elements of the list are integers
    if not all([isinstance(element, int) for element in lst]):
        return 'List has to contain integers only'

    # sorting list
    lst = sorted(lst)
    # list with unique values
    unique_lst = []
    # add elements to unique list if original list is not empty
    if len(lst) > 0:
        # i is the index of last founded unique element index in original list
        i=0
        # element  with index 0 is first uniqie element added to unique list
        unique_lst.append(lst[i])
        # iterate over original list from element in position 1 till last element
        for j in range(1, len(lst)):
            # if element in current position is not equal to last founded unique element
            # than current index assigned to index of last founded unique element
            # and current element added to unique list 
            if lst[i] != lst[j]:
                unique_lst.append(lst[j])
                i = j

    return len(unique_lst)


def homogeneous_type(*args):
    """Auxiliary function to check if all arguments are the same type"""

    types_lst = [type(arg) for arg in args]

    return len(set(types_lst)) == 1


def duplicate_values(*args):
    """Function which accepts a variable number of arguments, 
    and checks whether there are any duplicates among the arguments passed in.
    All arguments have to be the same type"""
    
    # check if passed more than 2 arguments to compare
    if len(args) < 2:
        return False
    # check if all arguments are same type
    if not homogeneous_type(*args):
        return 'Arguments are not the same type'

    # create sorted list from passed arguments
    lst = sorted(list(args))
    # i is the index of last founded unique element in the list of sorted argumnts
    # first element is unique by default
    i=0
    # iterate over arguments list from element in position 1 till last element
    for j in range(1, len(lst)):
        # if element in current position is not equal to last founded unique element
        # than current index assigned to index of last founded unique element
        if lst[i] != lst[j]:
            i = j
        # else duplicate founded 
        else:
            return True

    return False


def average_pair(lst, target_avrg):
    """
    Function to determine if there is a pair of values in the list of integers 
    where the average of the pair equals the target average. 
    There may be more than one pair that matches the average target.
    Given a sorted array of integers and a target average as parameters.
    Algorithm looking for the required average by approaching from left and right sides
    of the sorted list until left index smaller than right index.
    Return True or False
    """
    
    # check if passed more than 2 arguments (need 1 pair at least)
    if len(lst) < 2:
        return False
    # check if all elements of the list are integers
    if not all([isinstance(element, int) for element in lst]):
        return 'List has to contain integers only'

    # sorting list
    lst = sorted(lst)
    left_index = 0
    right_index = len(lst) - 1
    # look for for average until left_index less than right_index
    while left_index < right_index:
        current_avg = (lst[right_index] + lst[left_index])/2
        # if target average found return True
        if current_avg == target_avrg:
            return True
        # if calculated average is less then target average
        # to increase current avrg need to shift left_index
        # to the right in sorted lst to get greater element
        elif current_avg < target_avrg:
            left_index += 1
        # if calculated average is greater then target average
        # to reduce current avrg need to shift right_index
        # to the left in sorted lst to get smaller element
        else:
            right_index -= 1
    # if target average not found return False 
    return False


def is_subsequence(str1, str2):
    """
    Function takes two strings and checks whether the characters in the first string 
    form a subsequence of the characters in the second string.
    Subsequent of second string may include chars which not present in the first string.
    Only order matters (sing and ising for example).
    In other words, the function checks whether the characters in the first string 
    appear somewhere in the second string without their order changing.
    """
    
    # check if both parameters are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 'Function takes two strings only'
    # return False if string1 length greater than string2 length
    # larger can't be inside smaller 
    elif len(str1) > len(str2):
        return False
    
    str1_index = 0
    for char in str2:
        if char == str1[str1_index]:
            # if founded equal char is last char in string1 return True
            if str1_index == len(str1) - 1:
                return True
            # if not than shift index right
            else:
                str1_index += 1

            
    return False     
    

# tesing functions above
class CountUniqueValues(unittest.TestCase):

    def test_unique_values(self):
        self.assertEqual(count_unique_values([1,1,1,1,1,2]), 2)
        self.assertEqual(count_unique_values([1,2,3,4,4,4,7,7,12,12,13]), 7)
        self.assertEqual(count_unique_values([]), 0)
        self.assertEqual(count_unique_values([-2,-1,-1,0,1]), 4)
        self.assertEqual(count_unique_values(['1', '2']), 'List has to contain integers only')
        self.assertEqual(count_unique_values([13, 12, 12, 7, 7, 4, 4, 4, 3, 2, 1]), 7)

    def test_duplicate_values(self):
        self.assertFalse(duplicate_values(1, 2, 3))
        self.assertTrue(duplicate_values(1, 2, 2))
        self.assertTrue(duplicate_values('a', 'b', 'c', 'a'))
        self.assertFalse(duplicate_values(4))
        self.assertEqual(duplicate_values(1, 'a'), 'Arguments are not the same type')
        
    def test_average_pair(self):
        self.assertTrue(average_pair([1,2,3], 2.5))
        self.assertTrue(average_pair([1,3,3,5,6,7,10,12,19], 8))
        self.assertFalse(average_pair([-1,0,3,4,5,6], 4.1))
        self.assertFalse(average_pair([], 4))
        self.assertFalse(average_pair([1], 2))
        self.assertEqual(average_pair(['d', 3], 2), 'List has to contain integers only')
        
    def test_is_subsequence(self):
        self.assertTrue(is_subsequence('hello', 'hello world'))
        self.assertTrue(is_subsequence('sing', 'sting'))
        self.assertTrue(is_subsequence('abc', 'abracadabra'))
        self.assertFalse(is_subsequence('abc', 'acb'))
        self.assertFalse(is_subsequence('abce', 'abc'))
        self.assertEqual(is_subsequence(56, 'rfd'), 'Function takes two strings only')

    
if __name__ == '__main__':
    unittest.main()
