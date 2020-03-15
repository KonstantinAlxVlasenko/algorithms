"""
Module Weighted Graph
"""

import math
import string
import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from priority_queue import Node, PriorityQueue

class WeightedGraph:
    
    def __init__(self):
        
        self.adjacency_dct = {}
        
    
    def add_vertex(self, vertex):
        """
        Method to add vertex. Acceppts a name of a vertex.
        Adds a key to adjacency list with the name of the vertex
        and sets its value to be an empty dictionary.
        """
        
        if not self.adjacency_dct.get(vertex): 
            self.adjacency_dct[vertex] = []
        
    
    def add_edge(self, vertex1, vertex2, weight):
        """
        Method accepts two vertices. It finds in the adjacency list 
        the key of vertex1 and append vertex2 to the list and 
        vice versa
        """
        
        # check if both vertexes exist 
        if vertex1 in self.adjacency_dct and vertex2 in self.adjacency_dct:
            self.adjacency_dct[vertex1].append({'node': vertex2, 'weight': weight})
            self.adjacency_dct[vertex2].append({'node': vertex1, 'weight': weight})
            
            
    def graph(self):
        """Builds a Weighted Graph """
        
        if not self.adjacency_dct:
            return None
        
        G = nx.Graph()
        G.add_nodes_from(self.adjacency_dct.keys())
        for vertex, neighbours in self.adjacency_dct.items():
            for neighbour in neighbours:
                G.add_edge(vertex, neighbour['node'], 
                            weight=neighbour['weight'])
        print("Nodes of graph: ", G.nodes())
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        print(G.edges)
        plt.show()
        
        
    def shortest_path(self, start_vertex, end_vertex):
        """
        Method accepts a starting and ending vertices.
        Returns shortest path between those vertices.
        Method implements Dijkstra algorithm.
        """
        
#         path = []
        
        # distances dict with graph vertices as keys
        # and total distance from start_vertex to the key (vertex) as values
        # initaially each key (vertex) set with a velue of infinity,
        # except for the starting vertex which should have a value of 0
        distances = dict.fromkeys(self.adjacency_dct.keys(), np.inf)
        distances[start_vertex] = 0
        # add each vertex with a priority of Infinity to the priority
        # queue, except the starting vertex, which should have a prioryty of 0
        # because thats's where we begin
        priority_queue = PriorityQueue()
        for key in self.adjacency_dct.keys():
            if key == start_vertex:
                priority = 0
            else:
                priority = np.inf
            priority_queue.enqueue(key, priority)
        # previous dict with graph vertices as keys
        # and previous vertices used to reach key vertice from start vertice
        # with the shortest distance as values
        # initially set for each key value of None
        previous = dict.fromkeys(self.adjacency_dct.keys(), None)
        # looping as long as there is anything in the priority queue
        while priority_queue.values:
            # dequeue vertx from a priority queue
            vertex = priority_queue.dequeue()
            
            # loop through the each value in the adjacency list 
            if vertex.value != end_vertex:
                for neighbour in self.adjacency_dct[vertex.value]:
                    # calculate the distance to that vertex from the starting vertex
                    neighbour_distance = distances[vertex.value] + neighbour['weight']
                    # if the distance is less than what is currently stored
                    # in our distances dict
                    if neighbour_distance < distances[neighbour['node']]:
                        # update the distances dict with new lower distance
                        distances[neighbour['node']] = neighbour_distance
                        # update the previous dict to contain that vertex
                        previous[neighbour['node']] = vertex.value
                        # enqueue  the vertex with the total distance 
                        # from the start node
                        priority_queue.enqueue(neighbour['node'], neighbour_distance)
            # if dequeued vertex is the same as the ending vertex we are done
            else:                 
                break 
        
        return previous, distances[end_vertex]
        
        
    def shortest_path_graph(self, start_vertex = None, end_vertex = None):
        """
        Builds Weighted Graph with shortest path from start vertex to
        end vertex. If no vertices passed than random vertices is chosen
        """
        
        
        if not self.adjacency_dct:
            return None
        
        # choose start and end vertices if they were not strictly defined
        if not start_vertex:
            start_vertex = random.choice(list(self.adjacency_dct.keys()))
        if not end_vertex:
            end_vertex = random.choice(list(self.adjacency_dct.keys()))
        
        previous, distance = self.shortest_path(start_vertex, end_vertex)
        
        # create graph nodes (vertices) and edges
        G = nx.Graph()
        G.add_nodes_from(self.adjacency_dct.keys())
        for vertex, neighbours in self.adjacency_dct.items():
            for neighbour in neighbours:
                G.add_edge(vertex, neighbour['node'], 
                            weight=neighbour['weight'])
        # nodes positions
        pos = nx.spring_layout(G)
        
        # check path from end vertex to start vertex (backwards)
        # edges list
        shortest_path_edges = []
        # intermedia nodes list (path vetices excluding start and end vertices)
        nodes_path_lst = []
        # check previous dct from end vertex
        vertex = end_vertex
        while vertex != start_vertex:
            # add node to the list
            nodes_path_lst.append(vertex)
            # if previus vertex exist
            if previous.get(vertex):
                # add edge from current vertex to previos vertex
                shortest_path_edges.append((previous.get(vertex), vertex))
                # move to previous vertex
                vertex = previous.get(vertex)
            # if previous vertx doesn't exist there is no path
            else:
                print('No path found')
                return None
            
        # create list of vertices which are not part of the path    
        nodes = list(G.nodes())
        for node in nodes_path_lst:
            nodes.remove(node)
        nodes.remove(start_vertex)
        if start_vertex != end_vertex:
            nodes_path_lst.remove(end_vertex)

        print("Nodes of graph: ", G.nodes())
        print(f'Start: {start_vertex}, Path: {nodes_path_lst[::-1]}, Finish: {end_vertex}, Min Distance: {distance}')
        # draw transparent vertices which are not part of the path
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, alpha = 0.5)
        # draw triangular green start vertex 
        nx.draw_networkx_nodes(G, pos, nodelist=[start_vertex], 
                               node_size=500, node_color='g', node_shape='v',linewidths = 2)
        # draw green intermedia vertices
        nx.draw_networkx_nodes(G, pos, nodelist= nodes_path_lst, node_size=400, node_color='g')
        # draw green squared end vertex
        nx.draw_networkx_nodes(G, pos, nodelist=[end_vertex], 
                               node_size=500, node_color='r', node_shape='s', linewidths = 2)
        nx.draw_networkx_labels(G, pos)

        nx.draw_networkx_edges(G, pos, style='dashed')
        nx.draw_networkx_edges(G, pos, edgelist= shortest_path_edges, width = 2, edge_color = 'r', arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
        
        
def generate_weighted_graph(n=10, p=0.2):
    """
    Function to generate rendom Weighted Graph
    """
    
    G = nx.fast_gnp_random_graph(n, p)
    mapping = dict(zip(G, string.ascii_uppercase))
    G = nx.relabel_nodes(G, mapping)
    edge_weights = [(*edge, random.randint(1, 10)) for edge in G.edges]
    vertices = list(G.nodes)
    wg = WeightedGraph()
    for vertex in vertices:
        wg.add_vertex(vertex)
    for edge in edge_weights:
        wg.add_edge(*edge)
    
    # if unconnected node present regenerate graph    
    if [] in wg.adjacency_dct.values():
        print('Regenerate graph')
        wg = generate_weighted_graph(n, p)
        
    return wg


def main():
    wg = generate_weighted_graph()
    wg.graph()
    wg.shortest_path_graph()
    

if __name__ == "__main__":
    main()