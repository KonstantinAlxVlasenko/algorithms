"""Function which accepts an list with integers and counts unique values in the array"""

import unittest

def count_unique_values(lst):

    # check if all elements of the list are integers
    if not all([isinstance(element, int) for element in lst]):
        return 'List has to contain integers only'

    # sorting list
    lst = sorted(lst)
    # list with unique values
    unique_lst = []
    # add elements to unique list if original list is not empty
    if len(lst) > 0:
        # i is the last founded unique element index in original list
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


class CountUniqueValues(unittest.TestCase):

    def test_unique_values(self):
        self.assertEqual(count_unique_values([1,1,1,1,1,2]), 2)
        self.assertEqual(count_unique_values([1,2,3,4,4,4,7,7,12,12,13]), 7)
        self.assertEqual(count_unique_values([]), 0)
        self.assertEqual(count_unique_values([-2,-1,-1,0,1]), 4)
        self.assertEqual(count_unique_values(['1', '2']), 'List has to contain integers only')
        self.assertEqual(count_unique_values([13, 12, 12, 7, 7, 4, 4, 4, 3, 2, 1]), 7)

if __name__ == '__main__':
    unittest.main()
