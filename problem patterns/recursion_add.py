"""Module Additional Recursion pattern"""

import unittest


def reverse(string):
    """Function accepts a string and returns a new string in reverse."""
    if len(string) == 1:
        return string[0]
    return string[-1] + reverse(string[:-1])


def palindrome(string):
    """Recursive function returns true if the string passed to it is a palindrome 
    (reads the same forward and backward). Otherwise it returns false.
    """
    
    # first and last chars 
    # of the polyndrom has to be equal
    if string[0] != string[-1]:
        return False
    # string with 0 or 1 char is polyndrome
    elif len(string) < 2:
        return True
    # cut equal first and last chars and call fn again
    # until differences in first and last chars found
    # or one char or no char left
    else:
        return palindrome(string[1:-1])
    
    
def flatten(lst):
    """Function accepts a list of lists and 
    returns a new list with all values flattened.
    """
    
    # list where single element appended
    # other flat lists exteneded
    flat_lst = []
    for element in lst:
        # if element of the list is nested list
        if isinstance(element, list):
            # call flatten with nested list as parameter
            # after new flat_lst is filled with single elements
            # it returned and previous flat_lst extended
            flat_lst.extend(flatten(element))
        #  if element of the list is single element
        else:
            flat_lst.append(element)
        
    return flat_lst
    

def capitalize_first(lst):
    """Given an array of strings. 
    Capitalize the first letter of each string in the array.
    """
    
    if len(lst) == 1:
        return [lst[0].capitalize()]
    # call fn with passed lst minus last element
    res = capitalize_first(lst[0:-1])
    # add current last lst element to returned capitalized list
    res.append(lst[-1].capitalize())

    return res


def nested_even_sum(dct):
    """Function returns the sum of all even numbers in a dictionary which may contain nested dictionaries."""
    
    sum = 0
    for value in dct.values():
        # if value is dictionary
        if isinstance(value, dict):
            # calls fn on nested dictionary
            # after fn returns sum value adds it to
            # sum of even values calculated before
            sum += nested_even_sum(value)
        else:
            # if value is even integer number
            if isinstance(value, int) and value%2 == 0:
                # add value to the previously calculated sum
                sum += value

    return sum


def nums_to_string(dct):
    """Function takes in a dictionary and finds all of the values 
    which are numbers and converts them to strings
    """
    
    # dictionary with converted integers 
    # to string on current recursion step
    str_dct = {}
    
    for key, value in dct.items():
        # if value is dict call fn with sub dict passed
        # when fn returns converted dict add it to the
        # str_dct of higher recursive fn call  
        if isinstance(value, dict):
            str_dct[key] = nums_to_string(value)
        # for all other types
        else:
            if isinstance(value, bool):
                str_dct[key] = value
            elif isinstance(value, int):
                str_dct[key] = str(value)
            else:
                str_dct[key] = value
    
    return str_dct


def collect_strings(dct):
    """Function accepts a dictionary and returns 
    a list of all the values in the dictionary that have a type of string
    """
    # list with strings on
    # current fn recursion call
    str_lst = []
    
    for value in dct.values():
        # if value is dict call fn with sub dict passed
        # when fn returns string list add it to the
        # list of higher recursive fn call  
        if isinstance(value, dict):
            str_lst.extend(collect_strings(value))
        else:
            # if value is string add it to the list
            if isinstance(value, str):
                str_lst.append(value)
                
    return str_lst    
            
    
class TestRecursion(unittest.TestCase):
    
    def test_reverse(self):
        self.assertEqual(reverse('awesome'), 'emosewa')
        self.assertEqual(reverse('rithmschool'), 'loohcsmhtir')
        
    def test_palinndrome(self):
        self.assertFalse(palindrome('awesome'))
        self.assertFalse(palindrome('foobar'))
        self.assertTrue(palindrome('tacocat'))
        self.assertTrue(palindrome('amanaplanacanalpanama'))
        self.assertFalse(palindrome('amanaplanacanalpandemonium'))
    
    def test_flatten(self):
        self.assertEqual(flatten([1, 2, 3, [4, 5] ]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([1, [2, [3, 4], [[5]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([[1],[2],[3]]), [1,2,3])
        self.assertEqual(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]), [1,2,3])
        
    def test_capitalize(self):
        self.assertEqual(capitalize_first(['car','taco','banana']), ['Car','Taco','Banana'])
        
    def test_nested_even_sum(self):
        
        dct1 = {'outer': 2, 
                'dct': {
                    'inner': 2, 
                    'otherdct': {
                        'superInner': 2, 
                        'notANumber': True, 
                        'alsoNotANumber': "yup"
                        }
                    }
                }

        dct2 = {
            'a': 2,
            'b': {'b': 2, 'bb': {'b': 3, 'bb': {'b': 2}}},
            'c': {'c': {'c': 2}, 'cc': 'ball', 'ccc': 5},
            'd': 1,
            'e': {'e': {'e': 2}, 'ee': 'car'}
            }

        self.assertEqual(nested_even_sum(dct1), 6)
        self.assertEqual(nested_even_sum(dct2), 10)
        
    def test_num_tu_string(self):
        
        dct_int = {
            'num': 1, 
            'test': [], 
            'data': {
                'val': 4, 
                'info': {
                    'isRight': True, 
                    'random': 66}
                }
            }


        dct_str = {
            'num': '1', 
            'test': [], 
            'data': {
                'val': "4", 
                'info': {
                    'isRight': True, 
                    'random': '66'}
                }
            }
        
        self.assertEqual(nums_to_string(dct_int), dct_str)
        
    def test_collect_strings(self):
        str_dct = {'stuff': "foo", 
                'data': {
                    'val': {
                        'thing': {
                            'info': "bar", 
                            'moreInfo': {
                                'evenMoreInfo': {
                                    'weMadeIt': "baz"
                                    }
                                }
                            }
                        }
                    }
                }
        
        self.assertEqual(collect_strings(str_dct), ["foo", "bar", "baz"])    

if __name__ == '__main__':
    unittest.main()
    