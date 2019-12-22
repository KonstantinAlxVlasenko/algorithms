Repository contains Python scripts for Algorithms and Data structures training

1. File frequency_counter.py. Frequency counter pattern.
Function valid_anagram to determine if two given strings are anagram. O(n)
Anagram is a word, phrase, or name formed by rearranging the letters of another.
Second string is anagram to the first one (such as cinema and iceman).
Output is true or false.

Function same_frequency to check if given two positive integers have the same frequency of digits. O(n)


2. File unique_values.py. Multiple pointers pattern.
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


3. File max_sum.py. Sliding window pattern. O(n)
Function max_sum to calculate the maximum sum of n consecutive elements in the list
Function accepts list of integers and number of required consecutive elements

Function min_sublist_sum accepts two parameters - an array of positive integers and a positive integer. 
This function returns the minimal length of a contiguous subarray 
of which the sum is greater than or equal to the integer passed to the function. 
If there isn't one, returns 0 instead. O(n)