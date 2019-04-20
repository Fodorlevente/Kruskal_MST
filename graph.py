# Author: Levente Fodor
# Date: 2019.04.20
# Language: Python 3

# Description:
'''
There is a given undirected and weighted graph which represents a city.
Each node is represent a number of school aged children in that area.
The weights of the edges are represents the distance between two two node.
The goal is create an MST(Minimum Spanning Tree) to determine where to build
the school in order for the children to travel the least.

Use Kruskal algorithm for generating MST.
Kruskal's algorithm can be shown to run in O(E log E) time, or equivalently, O(E log V) time, 
where E is the number of edges in the graph and V is the number of vertices, all with simple data structures.

The representation of the graph with vertices for example:
    n = 4
    edge_1 = (0, 1, 10)
    edge_2 = (0, 2, 6)
    edge_3 = (1, 3, 15)
    edge_4 = (2, 3, 4)

    n : number of edges in the graph
    edge: (
            first node: number of childrens in the first node, 
            second node: number of childrens in the second node, 
            the weight of edge between the two nodes
           ) '''

from edge import Edge

class Graph:

    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = []

    # use with Edge object
    def addEdge(self,edge):
        self.graph.append(edge)
        edge.print_edges()
    
    def read_from_file(self,filename):
        with open(filename, 'r') as f:
            for line in f:
                y = line.split(",")
                tmp_edge = Edge(y[0],y[1],y[2])
                self.addEdge(tmp_edge)
                
g = Graph(1213)
g.read_from_file("./input/test.txt")