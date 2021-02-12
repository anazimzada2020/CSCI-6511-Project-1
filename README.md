# CSCI-6511-Project-1

For this project, we were required to find shortest path in a graph consist of vertices and undirected edges.
Program reads 2 input file “v.txt” and “e.txt” vertices and edges accordingly. It reads data, cleanse them and generate graph.
Other 4 arguments are n (number of vertices), s (start node), f (finish/goal node), and m (‘I’ for informed search, ‘U for uninformed search’).

My algorithm choice for uninformed search is Uniform Cost Search, and for informed search is A*.
Both algorithms behaves exactly the same way with 1 difference. A* search has heuristic function.
I used Euclidean distance as a heuristic between a particular node and goal node.
Euclidean distance is calculated between the middle points of those nodes’ located squares.

Firstly, I have implemented A* with heuristic for informed search. When I run uninformed search, I turn all heuristics values to 0 so that A* becomes UCS.

When I test a program for both Uninformed search and Informed search, it is clearly seen that A* outperforms UCS.
From perspective of time, A* performs little bit faster than UCS as out input is not that much large.
In addition, A* explores significantly less nodes as it has knowledge of direction. It is worth to mention that both algorithms are optimal.
In other words, they found same shortest path with same cost. Difference is performance.
