Repository contains Python scripts for Algorithms and Data structures training

1. File searching_algorithms.py. Searching algorithms patterns

Function linear_search accepts a list and a value, 
and returns the index at which the value exists. 
If the value does not exist in the list, return -1.
O(n)

Function binary_search accepts a sorted list and a value 
and returns the index at which the value exists. 
Otherwise, return -1. O(log n)    

Function naive_string_search takes two strings and 
checks how many times repeats smaller inside the bigger.
O(n^2)
         
Function kmp_string_search takes two strings and checks 
how many times repeats smaller inside the bigger. 
Knuth–Morris–Pratt(KMP) Pattern Matching(Substring search) 
algorithm applied. O(n)
https://www.youtube.com/watch?v=GTJr8OvyEVQ


2. File sorting_algorithms.py. List sorting algorithms patterns

Optimized Bubble sort algorithm implentation.
Function bubble_sort compares adjacent elements and swaps them if they 
are in the wrong order. Algorithm stops if after iteration 
no numbers have been swapped. O(n)

Selection sort algorithm implementation.
List is divided into two parts, the sorted part at the left end 
and the unsorted part at the right end. Initially, the sorted part 
is empty and the unsorted part is the entire list. 
The smallest element is selected from the unsorted array and swapped 
with the leftmost element, and that element becomes a part of the sorted array. 
This process continues moving unsorted array boundary by one element to the right. O(n)

Insert sorting algorithm implementation.
Function selection_sort.
Insertion sort is the sorting mechanism where the sorted array is built 
having one item at a time. The array elements are compared with each other 
sequentially and then arranged simultaneously in some particular order. O(n)

Merge sorting algorithm implementation.
Function merge_sort.
It works on the principle of Divide and Conquer. Merge sort repeatedly breaks down 
a list into several sublists until each sublist consists of a single element 
and merging those sublists in a manner that results into a sorted list.
Merge sort approach is the methodology which uses recursion mechanism. O(nlogn)

Quick sorting algorithm implementation.
Function quick_sort.
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot 
and partitions the given array around the picked pivot. Function takes list
as parameter only. Then call _quick_sort function with additional left and right
indexes parameters. At first call left and right indexes are first and last
list indexes. O(nlogn)

Radix sorting algorithm implementation.
Function radix_sort.
Radix sort is a non-comparative sorting algorithm. 
It avoids comparison by creating and distributing elements into buckets 
according to their radix. For elements with more than one significant digit, 
this bucketing process is repeated for each digit, while preserving the ordering 
of the prior step, until all digits have been considered.
Function takes list of pisitive numbers as a parameter and returns sorted list. O(n*k)
n - length of the list, k - number of digits in the largest num