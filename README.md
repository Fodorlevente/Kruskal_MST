# Kruskal_MST
Use Kruskal algorithm for generating MST.

## Run the script:
```sh
python graph.py
```
## Usage

```python
number_of_vertices = 4
g = Graph(number_of_vertices)
g.read_from_file("\\input\\test.txt")
g.Kruskal()
```

## Description:

There is a given undirected and weighted graph which represents a city.
Each node is represent a number of school aged children in that area.
The weights of the edges are represents the distance between two two node.
The goal is create an MST(Minimum Spanning Tree) to determine where to build
the school in order for the children to travel the least.

Use Kruskal algorithm for generating MST.
Kruskal's algorithm can be shown to run in O(E log E) time, or equivalently, O(E log V) time, 
where E is the number of edges in the graph and V is the number of vertices, all with simple data structures.

## Test Input:

```python
0,1,10
0,2,6
0,3,5
1,3,15
2,3,4
```
## Test Output:

```python
New edge added: u:0, v:1, w:10
New edge added: u:0, v:2, w:6
New edge added: u:0, v:3, w:5
New edge added: u:1, v:3, w:15
New edge added: u:2, v:3, w:4
Constructed Minimum Spanning Tree:
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
The School has to be built in zone 3
```

![Kruskal algorithm](kruskal.JPG)