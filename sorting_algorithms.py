"""Module Sorting algorithms"""

import unittest

def bubble_sort(lst):
    """
    Optimized Bubble sort algorithm implentation.
    Function compares adjacent elements and swaps them if they 
    are in the wrong order. Algorithm stops if after iteration 
    no numbers have been swapped 
    """
    
    # iterate backwards from last index to first
    # to reduce number of comparisions on each iteration
    # largest element found on last iteration is always at the end
    for i in range(len(lst) - 1, -1, -1):
        no_swaps = True
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # if swap occured change no_swap to False
                no_swaps = False
        # if no_swap left unchanged then all numbers
        # are sorted. no need to continue
        if no_swaps:
            break
                
    return lst


def selection_sort(lst):
    """
    Selection sort algorithm implementation.
    List is divided into two parts, the sorted part at the left end 
    and the unsorted part at the right end. Initially, the sorted part 
    is empty and the unsorted part is the entire list. 
    The smallest element is selected from the unsorted array and swapped 
    with the leftmost element, and that element becomes a part of the sorted array. 
    This process continues moving unsorted array boundary by one element to the right.
    """
    
    # no need to iterate till last index
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            # if element at index j is less
            # than element at min index 
            if lst[j] < lst[min_index]:
                min_index = j
        # if min_index has been changed
        # then swap elements
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
        
    return lst


def insert_sort(lst):
    """
    Insert sorting algorithm implementation.
    Insertion sort is the sorting mechanism where the sorted array is built 
    having one item at a time. The array elements are compared with each other 
    sequentially and then arranged simultaneously in some particular order.
    """
    # first element considered to be sorted
    for i in range (1, len(lst)):
        # if current element is less then element
        # with index 0 insert it before one
        if lst[i] <= lst[0]:
            lst.insert(0, lst.pop(i))       
        else:
            # iterate over already sorted part of list backwards
            for j in range(i-1, 0, -1):
                # if current element is greater or equal
                # to last element of already sorted part of list
                # do nothing and stop iteration
                if lst[i] >= lst[j]:
                    break
                # if current element is between two elements of
                # already sorted part of the list
                # insert it between and stop iteration  
                elif lst[j-1] <= lst[i] < lst[j]:
                    lst.insert(j, lst.pop(i))
                    break
    
    return(lst)
                 

def merge(lst1, lst2):
    """
    Auxiliary function for Merge sorting algorithm.
    Function takes two ascending sorted lists and merge them
    into one sorted list.
    """
    
    # merges list
    lst = []
    i, j = (0, 0)
    # iterate over 2 lists
    while i<len(lst1) and j<len(lst2):
        # print(f'lst1[{i}]:', lst1[i], '<>', f'lst2[{j}]:', lst2[j])
        
        # if 'i'th element of the first list is less or equal to the
        # 'j'th element of the second list than add first list 'i'th element
        # to the merged list and move 'i' index to next element
        if lst1[i] <= lst2[j]:
            lst.append(lst1[i])
            i += 1
        # if 'i'th element of the first list is greater than the
        # 'j'th element of the second list than add second list 'j'th element
        # to the merged list and move 'j' index to next element       
        else:
            lst.append(lst2[j])
            j += 1
    
    # when last element of the list has been added to the merged list
    # and while loop stops index of the 'exhausted' list gonna be eqaul to
    # len(lst) (list index increased by 1 after its element is added)
    
    # if list index after while loop stopped at the last element of the list
    # or less it means all elements of other list has been added to the merged list
    # and leftovers of the first sorted list ned to be added to the merged list 
    if i <= len(lst1) - 1:
        lst.extend(lst1[i:])
    elif j <= len(lst2) - 1:
        lst.extend(lst2[j:])       
            
    return lst


def merge_sort(lst):
    """
    Merge sorting algorithm implementation.
    It works on the principle of Divide and Conquer. Merge sort repeatedly breaks down 
    a list into several sublists until each sublist consists of a single element 
    and merging those sublists in a manner that results into a sorted list.
    Merge sort approach is the methodology which uses recursion mechanism. 
    """

    # if list consist of 0 or 1 elements no need to break down further
    # 0 or 1 element list is considered to be sorted
    if len(lst) <= 1:
        return lst
    
    # break point index
    middle = len(lst)//2
    # 'cut' right part of the list until reach list with 0 or 1 element
    # which considered to be sorted
    left = merge_sort(lst[:middle])
    # 'cut' left part of the list until reach list with 0 or 1 element
    # which considered to be sorted    
    right = merge_sort(lst[middle:])
    
    # call stack returns merged left and right sorted lists
    return merge(left, right)


def pivot(lst, start, end):
    """
    Auxiliary function for _quick_sort function. It takes list of nums, start and end
    indexes as arguments. Function puts pivot element with index defined by start parameter
    and puts it on the correct position in the list between start and end indexes.
    All nums less then pivot element moved to the left side from pivot element and 
    all nums greater than pivot element moved to right side from pivot element.
    Function returns updated pivot_index
    """
    
    # pivot_index reflects how many elemnts in the list
    # in the index range from start to end is less the pivot element
    pivot_index = start    
    pivot = lst[start]
    
    for i in range(start + 1, end + 1):
        # if current element is less then pivot
        if lst[i] < pivot:
            pivot_index += 1
            # exchange positions of current element less than pivot 
            # and first element greater than pivot
            lst[i], lst[pivot_index] = lst[pivot_index], lst[i]

    # after all elelemnts from start to the end indexes have been checked 
    # and all elements less then pivot was moved to the positions after
    # pivot than pivot element and last element less then pivot exchange positions
    # thus pivot element takes correct pisition 
    lst[start], lst[pivot_index] = lst[pivot_index], lst[start]

    return pivot_index

def _quick_sort(lst, left, right):
    """
    Quck sort algorithm function for recursive call with left and right parameters
    show which part of list is checked 
    """
    print('\n')
    if left < right:
        # calculate pivot_index of left element in the list 
        pivot_index = pivot(lst, left, right)
        # recursively call _quick_sort function but to check list elements
        # are on the left from pivit-index
        _quick_sort(lst, left, pivot_index - 1)
        # recursively call _quick_sort function but to check list elements
        # are on the right from pivit-index
        _quick_sort(lst, pivot_index + 1, right)
    return lst


def quick_sort(lst):
    """
    QuickSort is a Divide and Conquer algorithm. It picks an element as pivot 
    and partitions the given array around the picked pivot. Function takes list
    as parameter only. Then call _quick_sort function with additional left and right
    indexes parameters. At first call left and right indexes are first and last
    list indexes   
    """
    return _quick_sort(lst, 0, len(lst) - 1)


class TestSortingAlgorithms(unittest.TestCase):
    
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([45, 67, 23, 78, 32, 31, 69]), [23, 31, 32, 45, 67, 69, 78])
        self.assertEqual(bubble_sort([5,4,3,2,1,0]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort([-5,4,-3,2,-1,0]), [-5, -3, -1, 0, 2, 4])
        
    def test_selection_sort(self):
        self.assertEqual(selection_sort([45, 67, 23, 78, 32, 31, 69]), [23, 31, 32, 45, 67, 69, 78])
        self.assertEqual(selection_sort([5,4,3,2,1,0]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(selection_sort([-5,4,-3,2,-1,0]), [-5, -3, -1, 0, 2, 4])
        
    def test_insert_sort(self):
        self.assertEqual(insert_sort([45, 67, 23, 78, 32, 31, 69]), [23, 31, 32, 45, 67, 69, 78])
        self.assertEqual(insert_sort([5,4,3,2,1,0]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(insert_sort([-5,4,-3,2,-1,0]), [-5, -3, -1, 0, 2, 4])
        self.assertEqual(insert_sort([5,4,5,3,2,2,1,0]), [0, 1, 2, 2,3, 4, 5, 5])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([45, 67, 23, 78, 32, 31, 69]), [23, 31, 32, 45, 67, 69, 78])
        self.assertEqual(merge_sort([5,4,3,2,1,0]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([-5,4,-3,2,-1,0]), [-5, -3, -1, 0, 2, 4])
        self.assertEqual(merge_sort([5,4,5,3,2,2,1,0]), [0, 1, 2, 2,3, 4, 5, 5])

    def test_quick_sort(self):
        self.assertEqual(quick_sort([45, 67, 23, 78, 32, 31, 69]), [23, 31, 32, 45, 67, 69, 78])
        self.assertEqual(quick_sort([5,4,3,2,1,0]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(quick_sort([-5,4,-3,2,-1,0]), [-5, -3, -1, 0, 2, 4])
        self.assertEqual(quick_sort([5,4,5,3,2,2,1,0]), [0, 1, 2, 2,3, 4, 5, 5])

if __name__ == '__main__':
    unittest.main()