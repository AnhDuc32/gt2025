import numpy as np
from collections import defaultdict

# Contruct adjacent Matrix for graph G
num_nodes = 8

adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

edges = [
    (1, 2), (2, 6), (2, 5), (5, 7),
    (1, 3), (3, 4), (4, 8)
]

for u, v in edges:
    adj_matrix[u - 1][v - 1] = 1 

print("Adjacency Matrix:\n", adj_matrix)
print("----------")

# Inorder algo to exploit tree G
class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
    
    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
    
    def inorder_subtree(self, start_node):
        visited = set()
        result = []
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            
            children = self.adjacency_list[node]
            mid = len(children) // 2
            
            for i in range(mid):
                dfs(children[i])
            
            result.append(node)
            
            for i in range(mid, len(children)):
                dfs(children[i])
        
        dfs(start_node)
        return result

graph = Graph()

for u, v in edges:
    graph.add_edge(u, v)

x = int(input("Enter x value: "))
print("Inorder Subtree Traversal:", graph.inorder_subtree(x))

