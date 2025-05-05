from collections import deque

def dfs(graph , vertex  , visited = None):
    if visited is None: 
        visited= set()
    visited.add(vertex) 
    print(vertex, end= " ")   
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph , start):
    visited= set()
    queue = deque ([start]) 
    visited.add(start)    
    print(start, end= " ")
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add[neighbor] 
                print(neighbor,end=" ")      

def create_graph():
    num_vertices = int(input("enter the number of vertices: ")) 
    graph ={ i: [] for i in range (num_vertices)}
    num_edges= int(input("Enter the number of edges: "))
    print("enter the edges (each edge as a pair of vertices )")
    for _ in range (num_edges):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph

def main():
    graph = create_graph()
    print("/Adjacency list : ")
    for vertex in graph:
        print(f"{vertex} :{graph[vertex]}")
    start_vertex = int (input("Enter the starting vertex for traversal: "))
    print ("\n DFS traversal (resursive ) ")
    dfs(graph, start_vertex)

    print("\nBFS traversal (recursive) ")
    bfs(graph, start_vertex)

main()


