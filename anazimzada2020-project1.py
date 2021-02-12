import math
import time
import heapq

# Initialization function. Takes 6 arguments
# Number of Vertices, Start node, Finish node, Mode (U for Uninformed, I for Informed), Vertices txt file, Edges txt file

def init(no_vertices, start, finish, mode, file_vertices, file_edges):
    if mode.upper() != 'U' and mode.upper() != 'I':
        print("Wrong search algorithm chosen!")
        exit()
    return no_vertices, start, finish, mode, file_vertices, file_edges

# Euclidean function for heuristic of Informed (A*) Search
# Takes 4 arguments; Vertices list, Current node, Finish node, and Mode
# If it is Uninformed Search, it simply returns 0
# If it is Informed Search, it calculates and returns Euclidean distance

def Euclidean(v, a, b, mode):
    if mode.upper() == 'U':
        return 0
    elif mode.upper() == 'I':
        x = abs(v[a][1] - v[b][1])
        y = abs(v[a][0] - v[b][0])
        return math.sqrt(pow(x, 2) + pow(y, 2)) * 100

# Function that generates graph. It reads vetices and edges txt files, split them and store them
# Dictionaty "g" is our graph that stores our nodes, their edges with edge cost and new node's cost (f(n) = g(n) + h(n))

def gen_graph():
    file1 = open(file_v, 'r')
    file2 = open(file_e, 'r')
    vertices = file1.readlines()
    edges = file2.readlines()

    v = list()
    h = list()

    for i in range(0, n):
        v.append(i)
        h.append(i)

    for line in vertices:
        if line[0] != "#":
            x = line.strip().split(",")
            v[int(x[0])] = [int(int(x[1]) / 10), int(x[1]) % 10]

    for i in range(n):
        h[i] = Euclidean(v, i, f, m)

    g = dict()

    for i in range(n):
        g[i] = []

    for line in edges:
        if line[0] != "#":
            x = line.strip().split(",")
            g[int(x[0])].append([int(x[2]) + h[int(x[1])], int(x[1]), int(x[2])])
            g[int(x[1])].append([int(x[2]) + h[int(x[0])], int(x[0]), int(x[2])])
    return g

# This function generates path. It appends finish node in path and from end to start search for parent node

def gen_path(s, f, path, parent):
    path.append(parent[f])
    if parent[f] != s:
        gen_path(s, parent[f], path, parent)

# Search algorithm. UCS and A* behaves same with only 1 difference. A* has heuristic function
# For this reason I have implemented A* algorithm with Euclidean distance heuristic.
# If we make all heuristics equal to 0, A* becomes UCS.
# Simply we add start node to our open list. Then we look for it's successors and continue with the one has least f(n)
# When we are done with node we remove it from open list and add to closed list. This continues till open list is empty
# Meanwhile, we are also storing parent nodes. If we found finish node while iterating, it means we have found shortest path
# If we couldn't find and open list becomes empty, it means there is no path

def search(s, f):
    graph = gen_graph()
    s_time = time.time()
    closed_list = []
    open_list = []
    explored = []
    path = [f]
    parent = {}
    cost = 0
    
    for i in range(n):
        closed_list.append(0)
        
    heapq.heappush(open_list, (cost, [s, cost, s]))
    
    while len(open_list) > 0:
        c_score, [c_node, c_cost, p_node] = heapq.heappop(open_list)
        
        if closed_list[c_node] == 0:
            explored.append(c_node)
            closed_list[c_node] = 1
            parent[c_node] = p_node
            
            if c_node == f:
                print("PATH FOUND!\n")
                print(f"Total Cost  of Shortest Path = {c_cost}\n")
                
                print(f"Number of Nodes Visited: {len(explored)}\n")
                print(f"Visited Nodes in Order:")
                print(explored)
                
                print("\nPath of Shortest Path from Start to Finish:")
                gen_path(s, f, path, parent)
                path.reverse()
                print(path)
                        
                f_time = time.time()
                if m.upper() == 'U':
                    print(f"\nTime taken by UCS: {f_time - s_time} sec")
                elif m.upper() == 'I':
                    print(f"\nTime taken by A*: {f_time - s_time} sec")
                    
                return
            else:
                    
                for item in graph[c_node]:
                    heapq.heappush(open_list, (item[0] + c_cost, [item[1], item[2] + c_cost, c_node]))
                        
    print("NO PATH FOUND!")

# Start node is '1' and Finish node is '99'
# It is Informed Search
# For testing, change Start/Finish nodes and Search mode

if(__name__ == "__main__"):
    n, s, f, m, file_v, file_e = init(100, 1, 99, 'I', 'v.txt', 'e.txt')
    search(s, f)