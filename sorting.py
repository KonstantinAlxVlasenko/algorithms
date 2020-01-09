# def merge(lst1, lst2):
#     """
#     Auxiliary function for Merge sorting algorithm.
#     Function takes two ascending sorted lists and merge them
#     into one sorted list.
#     """
    
#     print(f'merging {lst1} and {lst2}')
#     # merges list
#     lst = []
#     i, j = (0, 0)
#     # iterate over 2 lists
#     while i<len(lst1) and j<len(lst2):
#         # print(f'lst1[{i}]:', lst1[i], '<>', f'lst2[{j}]:', lst2[j])
        
#         # if 'i'th element of the first list is less or equal to the
#         # 'j'th element of the second list than add first list 'i'th element
#         # to the merged list and move 'i' index to next element
#         if lst1[i] <= lst2[j]:
#             lst.append(lst1[i])
#             i += 1
#         # if 'i'th element of the first list is greater than the
#         # 'j'th element of the second list than add second list 'j'th element
#         # to the merged list and move 'j' index to next element       
#         else:
#             lst.append(lst2[j])
#             j += 1
        
#         # print(lst)
    
#     # print(i,j)
    
#     # when last element of the list has been added to the merged list
#     # and while loop stops index of the 'exhausted' list gonna be eqaul to
#     # len(lst) (list index increased by 1 after its element is added)
    
#     # if list index after while loop stopped at the last element of the list
#     # or less it means all elements of other list has been added to the merged list
#     # and leftovers of the first sorted list ned to be added to the merged list 
#     if i <= len(lst1) - 1:
#         lst.extend(lst1[i:])
#     elif j <= len(lst2) - 1:
#         lst.extend(lst2[j:])
        
#     print('merged_lst:', lst)        
            
#     return lst

# def merge_sort(lst):
#     """
#     Merge sorting algorithm implementation.
#     It works on the principle of Divide and Conquer. Merge sort repeatedly breaks down 
#     a list into several sublists until each sublist consists of a single element 
#     and merging those sublists in a manner that results into a sorted list.
#     Merge sort approach is the methodology which uses recursion mechanism. 
#     """
#     print('called merge_sort lst on:', lst)
#     # if list consist of 0 or 1 elements no need to break down further
#     # 0 or 1 element list is considered to be sorted
#     if len(lst) <= 1:
#         return lst
    
#     # break point index
#     middle = len(lst)//2
#     # 'cut' right part of the list until reach list with 0 or 1 element
#     # which considered to be sorted
#     left = merge_sort(lst[:middle])
#     print('return left:', left)
#     # 'cut' left part of the list until reach list with 0 or 1 element
#     # which considered to be sorted    
#     right = merge_sort(lst[middle:])
#     print('return right:', right)
    
#     # call stack returns merged left and right sorted lists
#     return merge(left, right)
        
# print(merge_sort([45, 67, 1, 3,89, 65, 92, 101, 8]))

def pivot(lst, start, end):
    # print(lst)
    
    pivot_index = start
    
    pivot = lst[start]
    
    for i in range(start + 1, end + 1):
        # print('i:', i, end=' ')
        if lst[i] < pivot:
            pivot_index += 1
            lst[i], lst[pivot_index] = lst[pivot_index], lst[i]
            # print(lst, pivot_index)
        # else:
            # print('')
            
    lst[start], lst[pivot_index] = lst[pivot_index], lst[start]
    
    # print(lst)
    
    return pivot_index

def _quick_sort(lst, left, right):
    print(lst, 'left:', left, 'right:', right, 'number', lst[left])
    if left < right:
        
        pivot_index = pivot(lst, left, right)
        print('pivot_index:', pivot_index)
        print('call left:', lst, left, pivot_index - 1)
        _quick_sort(lst, left, pivot_index - 1)
        print('recursive left return:', lst)
        print('call right:', lst, pivot_index + 1, right)
        _quick_sort(lst, pivot_index + 1, right)
        print('recursive right return:', lst)
    return lst


def quick_sort(lst):
    return _quick_sort(lst, 0, len(lst) - 1)    

# def partition(xs, start, end):
#     follower = leader = start
#     while leader < end:
#         if xs[leader] <= xs[end]:
#             xs[follower], xs[leader] = xs[leader], xs[follower]
#             follower += 1
#         leader += 1
#     xs[follower], xs[end] = xs[end], xs[follower]
#     return follower

# def _quicksort(xs, start, end):
#     if start >= end:
#         return xs
#     p = partition(xs, start, end)
#     _quicksort(xs, start, p-1)
#     _quicksort(xs, p+1, end)
    
# def quicksort(xs):
#     return _quicksort(xs, 0, len(xs)-1)


# print(pivot([28,41,4,11,16,1,40,14,36,37,42,18]))
print(quick_sort([4,8,2,1,5,7,6,3]))
# print(pivot([4,8,2,1,5,7,6,3], 0, 7))