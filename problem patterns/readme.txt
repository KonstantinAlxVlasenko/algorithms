Repository contains Python scripts for Algorithms and Data structures training


1. File frequency_counter.py. Frequency counter pattern.

Function valid_anagram to determine if two given strings are anagram. O(n)
Anagram is a word, phrase, or name formed by rearranging the letters of another.
Second string is anagram to the first one (such as cinema and iceman).
Output is true or false.

Function same_frequency to check if given two positive integers have the same frequency of digits. O(n)


2. File multiple_pointers.py. Multiple pointers pattern.

Function unique_values which accepts an list with integers and counts unique values in the array. O(n)

Function average_pair determines if there is a pair of values in the list of integers 
where the average of the pair equals the target average. 
There may be more than one pair that matches the average target.
Given a sorted array of integers and a target average as parameters.
Algorithm looking for the required average by approaching from left and right sides
of the sorted list until left index smaller than right index.
Return True or False. O(n)

Function is_subsequent takes two strings and checks whether the characters in the first string 
form a subsequence of the characters in the second string.
Subsequent of second string may include chars which not present in the first string.
Only order matters (sing, isting).
In other words, the function checks whether the characters in the first string 
appear somewhere in the second string without their order changing. 0(n)


3. File sliding_window.py. Sliding window pattern. 

Function max_sum to calculate the maximum sum of n consecutive elements in the list
Function accepts list of integers and number of required consecutive elements. O(n)

Function min_sublist_sum accepts two parameters - an array of positive integers and a positive integer. 
This function returns the minimal length of a contiguous subarray 
of which the sum is greater than or equal to the integer passed to the function. 
If there isn't one, returns 0 instead. O(n)

Function find_longest_substring accepts a string and returns the length of the longest 
substring with all distinct characters. O(n)


4. File recursion.py. Recursion pattern.

Functions factorial returns num factorial

Function filter_odd takes list of integers and returns list of odd numbers

Function power accepts a base and an exponent. 
The function returns the power of the base to the exponent.

Function list_product takes list of numbers and returns the product of them all.

Function recursive_range accepts a number and adds up all the numbers 
from 0 to the number passed to the function

Functions fib accepts a number and returns the number in the Fibonacci sequence. 
Recall that the Fibonacci sequence is the sequence of whole numbers 0, 1, 1, 2, 3, 5, 8, ... 
which starts with 1 and 1, and where every number thereafter is equal to the sum of the previous two numbers.


5. File recursion_add.py. Additional recursion pattern.

Function reverse accepts a string and returns a new string in reverse

Recursive function palindrome returns true if the string passed to it is a palindrome 
(reads the same forward and backward). Otherwise it returns false.

Function flatten accepts a list of lists and returns a new list with all values flattened.

Given an array of strings. Function capitalize_first capitalizes the first letter 
of each string in the array.

Function nested_even_sum returns the sum of all even numbers in a dictionary 
which may contain nested dictionaries.
    

Function nums_to_string takes in a dictionary and finds all of the values 
which are numbers and converts them to strings

Function collect_strings accepts a dictionary and returns a list of all the values 
in the dictionary that have a type of string


6. File divide_and_conquer.py. Problem patterns solved by applying Divide and Conquer approach.
Time complexity O(logN)

Function count_zeroes. Given list of 1s and 0s which has all 1s first followed by all 0s.
Function returns the number of zeroes in the list. 

Function sorted_freq. Given a sorted list and number.
Function counts the occurreneces of the number in the list.
If number is not found returns -1.

Function find_rotated_index. Function accepts a rotated list of sorted numbers and an integer.
Function returns the index of the integer in the list.
If the value is not found return -1.


7. File dynamic_programmimg.py. Problem patterns solved by applying Dynamic Programming

Function coin_change_number accepts two parameters: list of denominations and value.
Function returns the number of ways you can obtain the value from given collection of denominations.
Figures out the number of ways to make change for a given value from supply of coins.
Algorithm explanation https://www.youtube.com/watch?v=DJ4a7cmjZY0.

Function min_coin_change accepts list of coins of different denominations and a total amount of money amount. 
Function computes the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
https://www.youtube.com/watch?v=jgiZlGzXMBw