

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
        

if __name__ == '__main__':
    unittest.main()
