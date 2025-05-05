import heapq

# Function to implement Prim's algorithm for MST
def prims_algorithm(graph, start_vertex):
    # Initialize the MST result and a list to store visited vertices
    mst = []
    visited = set()
    min_heap = []

    # Function to add all edges of a vertex to the heap
    def add_edges(vertex):
        visited.add(vertex)
        for neighbor, weight in graph[vertex].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, vertex, neighbor))

    # Start from the starting vertex
    add_edges(start_vertex)

    # Process the graph until the min_heap is empty
    while min_heap:
        # Pop the edge with the smallest weight
        weight, u, v = heapq.heappop(min_heap)

        # If v is already visited, skip this edge
        if v in visited:
            continue

        # Add the edge (u, v) to the MST
        mst.append((u, v, weight))

        # Add all edges of vertex v to the min_heap
        add_edges(v)

    return mst

# Function to take graph input from user
def input_graph():
    graph = {}
    n = int(input("Enter the number of vertices: "))
    print("Enter the edges (vertex1 vertex2 weight) one by one:")
    
    for _ in range(n * (n - 1) // 2):  # maximum number of edges in an undirected graph
        edge_input = input("Enter edge (vertex1 vertex2 weight) or type 'done' to finish: ")
        if edge_input.lower() == "done":
            break
        vertex1, vertex2, weight = edge_input.split()
        weight = int(weight)
        
        if vertex1 not in graph:
            graph[vertex1] = {}
        if vertex2 not in graph:
            graph[vertex2] = {}
        
        graph[vertex1][vertex2] = weight
        graph[vertex2][vertex1] = weight
    
    return graph

# Input the graph from the user
graph = input_graph()

# Ask for the starting vertex
start_vertex = input("Enter the starting vertex: ")

# Run Prim's algorithm to get the MST
mst = prims_algorithm(graph, start_vertex)

# Print the Minimum Spanning Tree (MST)
print("\nMinimum Spanning Tree (MST):")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} with weight {edge[2]}")

