""" 
Module Stack and Queue.

Stack is a LIFO (Last In First Out) data structure.
Queue is a FIFO (First In First Out) data structure
"""

class Node:
    """Class to create Node of the Stack or Queue"""
    
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    """Class to create Stack"""
    
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

        
    def print_list(self):
        """
        Shows Stack elements values
        """
        lst = []
        current = self.first
        while current:
            if not current.next:
                lst.append((current.value, None))
            else:   
                lst.append((current.value, current.next.value))
            current = current.next
        print(lst)      
        
    
    def push(self, value):
        """
        Adds a value to the top of the stack.
        Returns size of stack
        """
        
        # create a new node using the value passed to the function
        new_node = Node(value)
        # if there are no nodes in the stack, set the first and
        # last property to be the newly created node
        if not self.first:
            self.first = new_node
            self.last = self.first
        # if there is at least one node
        else:
            # create a variable that stores the current first
            # property on the stack
            ex_first = self.first
            # reset the first property to be the newly created node
            self.first = new_node
            # set the next property on the node to be previously 
            # created variable
            new_node.next = ex_first
        
        # increment length of the list by 1
        self.size += 1
        
        return self.size
    
    
    def pop(self):
        """
        Removes node from the top of the Stack.
        Returns removed value
        """
        # if there are no nodes, return None
        if not self.first:
            return None
        # store the current first property in variable
        old_first = self.first
        # if there is only 1 node
        if self.size == 1:
            # set the first and last property to be None
            self.first = None
            self.last = None
        # if there is more than one node
        else:
            # set the first property to be the next property
            # on the current first
            self.first = old_first.next
        
        # decrement length by 1
        self.size -= 1
        old_first.next = None    
        
        return old_first.value
    
    
class Queue:
    """Class to create Queue"""
    
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

        
    def print_list(self):
        """
        Shows Queue elements values
        """
        lst = []
        current = self.first
        while current:
            if not current.next:
                lst.append((current.value, None))
            else:   
                lst.append((current.value, current.next.value))
            current = current.next
        print(lst)
        
        
    def enqueue(self, value):
        """
        Adds a new node to the end of the Queue. 
        Takes value of new Node as an argument. 
        Returns updated size of queue
        """
        # create a new node using value passed to the function
        new_node = Node(value)
        # if there are no nodes in the queue
        if self.size == 0:
            # set this node to be the first and last property of the queue
            self.first = new_node
            self.last = new_node
        # otherwise
        else:
            # set the next property on the current last to be that node
            self.last.next = new_node
            # and then set the last property of the queue to be that node
            self.last = new_node
        # increment the size of the queue by 1
        self.size += 1
        return self.size
    
    
    def dequeue(self):
        """
        Removes node from the top of the Queue.
        Returns removed node value
        """
        # if there are no nodes, return None
        if not self.first:
            return None
        # store the current first property in variable
        old_first = self.first
        # if there is only 1 node (if the first is the same as last)
        if self.first == self.last:
            # set the first and last property to be None
            self.first = None
            self.last = None
        # if there is more than one node
        else:
            # set the first property to be the next property
            # on the current first
            self.first = old_first.next
        
        # decrement length by 1
        self.size -= 1
        old_first.next = None    
        
        return old_first.value