"""
Module Priority Queue
Based Min Binary Heap
A data structure where each element has a priority. 
Elements with a higher priorities are served before elements with lower prioritirs
"""

import math
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class Node:
    """PiorityQueue Node"""
    
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        

class PiorityQueue:
    
    def __init__(self):
        self.values = []
        
        
    def enqueue(self, value, priority):
        """
        Enqueue method accepts a value and priority, makes a new node,
        and puts in the right spot based off of its priority
        """
        
        new_node = Node(value, priority)
        # append the value into the values property on the heap
        self.values.append(new_node)
        self.bubble_up()
        

    def bubble_up(self):
        """
        Method to 'bubble up' last node in values list
        to the correct spot
        """
        idx = len(self.values)-1
        element = self.values[idx]
        parent_idx = int((idx-1)/2)
        parent = self.values[parent_idx]
        
        # keep looping as long as the values element at the parent_index
        # is less than the values element at the child index
        while idx > 0 and element.priority < parent.priority:
            # swap the value of the values element at the parent_index
            # with the value of the element property at the child index
            self.values[parent_idx], self.values[idx] =  self.values[idx], self.values[parent_idx]
            # set the index to be parent_index, and start over
            idx = parent_idx
            parent_idx = int((idx-1)/2)
            parent = self.values[parent_idx]
            
        return self
        
        
    def dequeue(self):
        """
        Romoves root from the heap. Rearrange values in heap.
        Returns old root
        """
        if not self.values:
            return None
        # swap the first value in values property with the last one
        last_index = len(self.values) - 1 
        self.values[0], self.values[last_index] = self.values[last_index], self.values[0]
        # pop from the values property to return the value at the end
        ex_root = self.values.pop()
        # call sink_down function to place 'new root' to correct spot
        if self.values:
            self.sink_down()
        
        return ex_root
        
    
    def sink_down(self):
        """Function to 'sink-down' root to the correct spot"""
        
        # parent index starts at 0
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            # left child index
            left_child_idx = 2 * idx + 1
            # right child index
            right_child_idx = 2 * idx + 2
            # index of element to swap with
            swap = None
            
            # need to swap parent element with the largest child
            # if child is greater than parent
            
            # if left child exist
            if left_child_idx < length:
                left_child = self.values[left_child_idx]
                # and left child is greater than element to 'sink-down'
                if left_child.priority < element.priority:
                    # swap index is left child index
                    swap = left_child_idx
            # if right child exist
            if right_child_idx < length:
                right_child = self.values[right_child_idx]
                # if swap index was not found before (left child is less than element)
                # and right child is greater than element
                # or if swap index was found before (lift child is greater than element)
                # but right child is greater than left child
                if (not swap and right_child.priority < element.priority) or \
                    (swap and right_child.priority < left_child.priority):
                        # swap index is right child index
                        swap = right_child_idx
            # if left and right children is less then element
            # then parent element is in correct spot
            if not swap:
                break
            # if swap index was found swap parent with one of children
            self.values[idx], self.values[swap] = self.values[swap], self.values[idx]
            # index of parent element after swap
            idx = swap
            
            
    def graph(self):
        """
        Builds Piority Queue graph with node tree level, 
        priority and value labels
        """
        
        nodes = self.values
        # string representation of nodes
        nodes_str = []
        
        if not len(nodes):
            return None
        max_graph = nx.Graph()
        root_node = nodes[0]
        # string representation of root node
        root_node_str = f'ROOT(P: {root_node.priority}, V: {root_node.value})' 
        nodes_str.append(root_node_str)
        # add root node on graph
        max_graph.add_node(root_node_str)
        for i in range(len(nodes)):
            # left and right children indexes of the current parent element
            left_child_idx = 2*i + 1
            right_child_idx = 2*i + 2
            # binary tree level of parent element
            parent_level = int(math.log2(i+1))
            # if left child exist
            if len(nodes) > left_child_idx:
                left_child = nodes[left_child_idx]
                # string representation of left child
                left_child_str = f'{parent_level+1}L(P: {left_child.priority}, V: {left_child.value})'
                nodes_str.append(left_child_str)
                # add left child on graph and draw connection with parent
                max_graph.add_node(left_child_str)
                max_graph.add_edge(nodes_str[i], left_child_str)
            # if right child exist
            if len(nodes) > right_child_idx:
                right_child = nodes[right_child_idx]
                # string representation of right child
                right_child_str = f'{parent_level+1}R(P: {right_child.priority}, V: {right_child.value})'
                nodes_str.append(right_child_str)
                # add right child on graph and draw connection with parent
                max_graph.add_node(right_child_str)
                max_graph.add_edge(nodes_str[i], right_child_str)
        
        print("Nodes of graph: ", max_graph.nodes())
        nx.draw(max_graph, with_labels = True)
        plt.show()
        
        
er = PiorityQueue()
queue_lst = [('common cold', 5), ('gunshot wound', 1), ('high fever', 4), ('broken arm', 2), ('glass in foot', 3)]
for value, priority in queue_lst:
    er.enqueue(value, priority)
er.graph()

