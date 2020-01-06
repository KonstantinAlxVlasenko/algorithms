def merge(lst1, lst2):
    """
    Auxiliary function for Merge sorting algorithm.
    Function takes two ascending sorted lists and merge them
    into one sorted list.
    """
    
    print(f'merging {lst1} and {lst2}')
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
        
        # print(lst)
    
    # print(i,j)
    
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
        
    print('merged_lst:', lst)        
            
    return lst

def merge_sort(lst):
    print('called merge_sort lst on:', lst)
    if len(lst) <= 1:
        return lst
    
    middle = len(lst)//2
    
    left = merge_sort(lst[:middle])
    print('return left:', left)
    right = merge_sort(lst[middle:])
    print('return right:', right)
    
    return merge(left, right)
        
print(merge_sort([45, 67, 1, 3,89, 65, 92, 101, 8]))