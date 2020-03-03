"""
Module Hash Tables

Hash tables are collection of key-value pairs
Hash tables can find values quickly given a key
Hash tables store data in a large array, and work by hashing the keys
A good hash should be fast, distribute keys uniformly, and be determenistic
Separate chaining and linear probing are two strategies used to deal with two keys keys that hash to the same index

Big O (average case)
Insertion - O(1), Deletion - O(1), Access O(1)
"""


class HashTable:
    
    
    def __init__(self, size=53):
        
        self.key_map = [None] * size
        
        
    def _hash(self, key: str):
        """
        Hash function used to transform string key into integer
        """
        total = 0
        # prime num usage allows reducing integer collisions
        # and spread data in the list as much as possible
        prime_num = 31
        for i, char in enumerate(key):
            # check only 100 symbols of a string
            if i > 100:
                break
            value = ord(char) - 96
            total = (total*prime_num + value) % len(self.key_map)
        return total
    
    
    def set_pair(self, key, value):
        """
        Method puts key, value pair in hash table.
        If key is already exist value is overwritten.
        """
        
        # get key index of hash table
        idx = self._hash(key)
        key_exist = False
        # if no data were written to hashtable with idx index
        if not self.key_map[idx]:
            self.key_map[idx] = []
        i = 0
        # iterate over key, value pairs with idx index to check
        # if key is already exist
        for k, _ in self.key_map[idx]:
            if k == key:
                # overwrite value for existing key
                self.key_map[idx][i][1] = value
                key_exist = True
                break
            i += 1
        if not key_exist:        
            self.key_map[idx].append([key, value])
        
        
    def get_value(self, search_key):
        """Method to get value of the given key"""
        
        # get key index of hash table
        idx = self._hash(search_key)
        # if data exist in hash table in idx index
        if self.key_map[idx]:
            # check if there is a required key
            for key, value in self.key_map[idx]:
                if key == search_key:
                    return value
        return None
    
    
    def keys(self):
        """Method returns hash table keys"""
        
        keys = []
        for element in self.key_map:
            if element:
                for key, _ in element:
                    keys.append(key)
        return keys
        
    
    def values(self):
        """Method returns hash table unique values"""
        
        values = set()
        for element in self.key_map:
            if element:
                for _, value in element:
                    values.add(value)
        return list(values)
    
    
    def items(self):
        """Method returns hash table key, value pairs"""
        
        items = []
        for element in self.key_map:
            if element:
                for item in element:
                    items.append(tuple(item))
        return items
    
    
ht = HashTable(20)
colors_codes = [
    ('white', '#FFFFFF'), ('silver', '#C0C0C0'), ('gray', '#808080'), 
    ('black', '#000000'), ('red', '#FF0000'), ('maroon', '#800000'), 
    ('yellow', '#FFFF00'), ('olive', '#808000'), ('lime', '#00FF00'), 
    ('green', '#008000'), ('aqua', '#00FFFF'), ('teal', '#008080'), 
    ('blue', '#0000FF'), ('navy', '#000080'), ('fuchsia', '#FF00FF'), 
    ('purple', '#800080')
    ]
for color, code in colors_codes:
    ht.set_pair(color, code)
print(ht.keys())
print(ht.values())
print(ht.items())
print(ht.get_value('maroon'))


