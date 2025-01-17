import numpy as np

def create_adjacency_matrix(edges, vertices):
    if not vertices:
        vertices = set()
        for s, e, _ in edges:
            vertices.add(s)
            vertices.add(e)
        vertices = sorted(list(vertices))
    
    vertex_to_idx = {vertex: idx for idx, vertex in enumerate(vertices)}
    
    n = len(vertices)
    matrix = np.full((n, n), float('inf'))
    
    np.fill_diagonal(matrix, 0)
    
    for start, end, weight in edges:
        i, j = vertex_to_idx[start], vertex_to_idx[end]
        matrix[i][j] = weight
    
    return matrix, vertices, vertex_to_idx

def dijkstra(graph, source_idx, target_idx, vertices):
    n = len(vertices)
    dist = [float('inf')] * n
    prev = [None] * n
    visited = [False] * n
    
    dist[source_idx] = 0
    
    for _ in range(n):
        min_dist = float('inf')
        min_vertex = -1
        
        for v in range(n):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_vertex = v
        
        if min_vertex == -1:
            break
            
        visited[min_vertex] = True
        
        for v in range(n):
            if (not visited[v] and 
                graph[min_vertex][v] != float('inf') and 
                dist[min_vertex] + graph[min_vertex][v] < dist[v]):
                dist[v] = dist[min_vertex] + graph[min_vertex][v]
                prev[v] = min_vertex
    
    path = []
    current = target_idx
    
    while current is not None:
        path.append(vertices[current])
        current = prev[current]
    
    path.reverse()
    
    return path, dist[target_idx]

def main():
    edges = [
        ('A','C',1), ('A','B',4), ('C','F',7), ('B','F',3),
        ('C','D',8), ('D','H',5), ('F','H',1), ('F','E',1),
        ('E','H',2), ('H','G',3), ('H','M',7), ('H','L',6),
        ('G','L',4), ('E','L',2), ('G','M',4), ('L','M',1)
    ]
    
    vertices = sorted(list(set([v for edge in edges for v in edge[:2]])))
    
    matrix, vertices, vertex_to_idx = create_adjacency_matrix(edges, vertices)
    
    source = input("Enter source vertex (A-M): ")
    target = input("Enter target vertex (A-M): ")
    
    if source not in vertices or target not in vertices:
        print("Invalid vertices!")
        return
    
    path, total_weight = dijkstra(
        matrix,
        vertex_to_idx[source],
        vertex_to_idx[target],
        vertices
    )
    
    print(f"\nShortest path from {source} to {target}:")
    print(" -> ".join(path))
    print(f"Total weight: {total_weight}")

if __name__ == "__main__":
    main()