# Author: Levente Fodor
# Date: 2019.04.20
# Language: Python 3

'''
    u: number of children in node_1
    v: number of children in node_2
    w: weight between two nodes

    myEdge = Edge(0,1,10)
'''

class Edge:

    def __init__(self,u,v,w):
        self.verticles = [int(u),int(v),int(w)]

    def __getitem__(self,index):
        return self.verticles[index]

    def print_edges(self):
        print(f"New edge added: u:{self.verticles[0]}, v:{self.verticles[1]}, w:{self.verticles[2]}")
