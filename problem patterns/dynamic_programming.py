"""Module Dynamic Programming"""

import unittest
import numpy as np


def coin_change_number(coins, value):
    """
    Function accepts two parameters: list of denominations and value.
    Function returns the number of ways you can obtain the value from given collection of denominations.
    Figures out the number of ways to make change for a given value from supply of coins.
    Algorithm explanation https://www.youtube.com/watch?v=DJ4a7cmjZY0
    """
    
    # table of total combinations number for denominations and values
    # each row represents set of denominations. 
    # starts from empty coins list [] appending each row a coin from coins list until last denomination
    # columns represent values starting from 0 till required value
    # initialize table with zeroes  
    total_combinations = np.zeros([len(coins)+1, value+1], dtype = int)
    # first columns (value 0) is filled with 1 since if value is 0 the only one way to make change
    # is do nothing
    total_combinations[:, 0] = 1
    
    # check each row starting from row with index 1 (first denomination from coins list) 
    for i in range(1, len(coins)+1):
        # for each row (coins set) check each value starting from 1 till required value 
        for j in range(1, value+1):
            # if checked denomination in a coins set of the row (last coin of current set) is less or equal to checked value 
            if coins[i-1] <= j:
                # then use number of ways to give change for the previous row (current value but denomination set without current coin)
                # plus number of ways to give change for the current denomination set bot for value minus current coin value
                # table[row][value] = table[row-1][value] + table[row][value - current_coin]
                total_combinations[i, j] = total_combinations[i-1, j] + total_combinations[i, j-coins[i-1]]
            # if checked denomination in a coins set of the row (last coin of current set) is greater than checked value
            else:
                # then we can use only previous rows coins set without current row denomination to give change for the value
                # table[row][value] = table[row-1][value]
                total_combinations[i, j] = total_combinations[i-1, j]
    
    return total_combinations[-1, -1]


def min_coin_change(coins, value):
    """
    Function accepts list of coins of different denominations and a total amount of money amount. 
    Function computes the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.
    Algorithm explanation https://www.youtube.com/watch?v=jgiZlGzXMBw
    """
    
    # list with minimum coins number for the value (index)
    # starting from value 0 till required value
    min_coins_num = [np.inf] * (value +1)
    # the only way to get 0 value is to give no coins (0 coins)
    min_coins_num[0] = 0
    
    # for each value (amount) in list
    for i in range(1, len(min_coins_num)):
        # for each coin in denomination list
        for coin in coins:
            # if coin is less then current value
            if coin <= i:
                # substract current coin from current value
                # find the minimum coins number for the rest value and add one (coin which was substracted in prev step)
                # check if obtained result is less then result for that value but with other coins
                min_coins_num[i] = min(min_coins_num[i-coin] + 1, min_coins_num[i])
    
    if min_coins_num[-1] < np.inf:
        return min_coins_num[-1]
    else:
        return -1
    

def min_coins_top_btm(coins, value, cache = []):
    if not cache:
        cache = [1 if i in coins else 0 for i in range(value+1)] 
    min_coins = np.inf
    if cache[value]:
        return cache[value]
    else:
        for i in [coin for coin in coins if coin <= value]:
            num_coins = 1 + min_coins_top_btm(coins, value - i, cache)
            if num_coins < min_coins:
                min_coins =  num_coins
                cache[value] = min_coins
    
    return min_coins


class DynamicProgramming(unittest.TestCase):
    
    def test_coin_change_number(self):
        self.assertEqual(coin_change_number([1,5,10,25], 1), 1)
        self.assertEqual(coin_change_number([1,5,10,25], 2), 1)
        self.assertEqual(coin_change_number([1,5,10,25], 5), 2)
        self.assertEqual(coin_change_number([1,5,10,25], 10), 4)
        self.assertEqual(coin_change_number([1,5,10,25], 25), 13)
        self.assertEqual(coin_change_number([1,5,10,25], 45), 39)
        self.assertEqual(coin_change_number([1,5,10,25], 100), 242)
        self.assertEqual(coin_change_number([1,5,10,25], 145), 622)
        self.assertEqual(coin_change_number([1,5,10,25], 1451), 425663)
        self.assertEqual(coin_change_number([1,5,10,25], 14511), 409222339)
        
        
    def test_min_coin_change(self):
        self.assertEqual(min_coin_change([1,2,5], 11), 3)
        self.assertEqual(min_coin_change([1,2,5,10], 46), 6)
        
        
    def test_min_coins_top_btm(self):
        self.assertEqual(min_coins_top_btm([1,2,5], 11), 3)
        self.assertEqual(min_coins_top_btm([1,2,5,10], 46), 6)
        

if __name__ == '__main__':
    unittest.main()