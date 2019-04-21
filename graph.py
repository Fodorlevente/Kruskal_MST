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
import os

class Graph:

    def __init__(self,vertices):
        self.vertices = vertices # Number of vertices n = 4
        self.graph = []

    # use with Edge object
    def addEdge(self,edge):
        self.graph.append(edge)
        edge.print_edges()
    
    def read_from_file(self,filename):
        with open(self.generate_filename_path(filename), 'r') as f:
            for line in f:
                y = line.split(",")
                tmp_edge = Edge(y[0],y[1],y[2])
                self.addEdge(tmp_edge)

    def get_folder_path(self):
        return (os.path.dirname(os.path.realpath(__file__)))

    def generate_filename_path(self,filename):
        return (self.get_folder_path() + filename)

    def max_of_weights(self):
        pass

	# A utility function to find set of an element i 
	# (uses path compression technique)
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i])

	# A function that does union of two sets of x and y 
	# (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
        
		# Attach smaller rank tree under root of 
		# high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

		# If ranks are same, then make one as root and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
    
    def Kruskal(self): 
        result =[] #This will store the resultant MST 
        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 

        # Step 1: Sort all the edges in non-decreasing order of their weight. 
        # If we are not allowed to change the given graph, we can create a copy of graph 
        self.graph = sorted(self.graph,key=lambda item: item[2]) 

        parent = [] # List for storing parents (nodes example: [0,1,2,3])
        rank = []  # List for storing ranks

        # Create V subsets with single elements 
        for node in range(self.vertices): 
            parent.append(node) 
            rank.append(0) # At first all rank is 0
	
        
        # Number of edges to be taken is equal to vertices-1 
        while e < self.vertices -1 : 

        # Step 2: Pick the smallest edge and increment the index for next iteration 
            u,v,w = self.graph[i] 
            i = i + 1
            x = self.find(parent, int(u)) 
            y = self.find(parent ,int(v)) 

            # If including this edge does not cause cycle, 
            # include it in result and increment the index 
            # of result for next edge 
            if x != y: 
                e = e + 1	
                result.append([int(u),int(v),int(w)]) 
                self.union(parent, rank, x, y)			 
            # Else discard the edge 

		# print the contents of result[] to display the built MST 
        print("Constructed Minimum Spanning Tree:")
        for u,v,weight in result: 
            print("%s -- %s == %s" % (u,v,weight))

g = Graph(4)
g.read_from_file("\\input\\test.txt")
g.get_folder_path()
g.Kruskal()