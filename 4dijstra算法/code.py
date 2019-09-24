from collections import defaultdict
from heapq import *


def dijkstra_raw(edges, from_node, to_node):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen = [(0, from_node, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == to_node:
                return cost, path
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))
    return float("inf"), []


def dijkstra(edges, from_node, to_node):
    len_shortest_path = -1
    ret_path = []
    length, path_queue = dijkstra_raw(edges, from_node, to_node)
    if len(path_queue) > 0:
        len_shortest_path = length  ## 1. Get the length firstly;
        ## 2. Decompose the path_queue, to get the passing nodes in the shortest path.
        left = path_queue[0]
        ret_path.append(left)  ## 2.1 Record the destination node firstly;
        right = path_queue[1]
        while len(right) > 0:
            left = right[0]
            ret_path.append(left)  ## 2.2 Record other nodes, till the source-node.
            right = right[1]
        ret_path.reverse()  ## 3. Reverse the list finally, to make it be normal sequence.
    return len_shortest_path,ret_path


### ==================== Given a list of nodes in the topology shown in Fig. 1.
list_nodes_id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
### ==================== Given constants matrix of topology.
M = 99999  # This represents a large distance. It means that there is no link.
### M_topo is the 2-dimensional adjacent matrix used to represent a topology.
M_topo = [
    [M, 1, 1, M, 1, M, 1, 1, 1, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, M, 1, M, M, 1, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, 1, M, 1, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M],
    [M, M, 1, M, 1, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, M, M, 1, M, M, M, M, M, 1, 1, 1, M, M, M, M, M, M, M, M, M],
    [M, 1, M, M, M, M, 1, M, M, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, M, M, M, M, 1, M, 1, M, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, M, M, M, M, M, 1, M, 1, M, M, M, M, M, M, M, M, M, M, M, M],
    [1, M, M, M, M, M, M, 1, M, 1, M, M, 1, M, M, M, M, M, M, M, M],
    [M, M, M, M, 1, M, M, M, 1, M, M, 1, M, M, M, M, M, M, M, M, M],
    [M, M, M, M, 1, M, M, M, M, M, M, 1, M, 1, M, M, M, M, M, M, M],
    [M, M, M, M, 1, M, M, M, M, 1, 1, M, M, 1, 1, M, M, M, M, M, M],
    [M, M, M, M, M, M, M, M, 1, M, M, M, M, M, 1, M, M, M, M, M, M],
    [M, M, M, M, M, M, M, M, M, M, 1, 1, M, M, 1, M, M, 1, 1, M, M],
    [M, M, M, M, M, M, M, M, M, M, M, 1, 1, 1, M, 1, 1, M, M, M, M],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, M, 1, M, 1, M, 1, 1, M],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, M, 1, 1, M, M, M, M, 1],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, 1, M, M, M, M, 1, M, M],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, 1, M, 1, M, 1, M, 1, M],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, 1, M, M, 1, M, 1],
    [M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, M, 1, M, M, 1, M]
]

### --- Read the topology, and generate all edges in the given topology.
edges = []
for i in range(len(M_topo)):
    for j in range(len(M_topo[0])):
        if i != j and M_topo[i][j] != M:
            edges.append((i, j, M_topo[i][j]))  ### (i,j) is a link; M_topo[i][j] here is 1, the length of link (i,j).



print("=== Dijkstra ===")
length,Shortest_path = dijkstra(edges, 3, 2)
print(length)
print(Shortest_path)
