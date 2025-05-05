import heapq

# Heuristic function: Manhattan distance
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Get neighbors (adjacent nodes) in the grid
def get_neighbors(node, grid):
    neighbors = []
    x, y = node
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1:
            neighbors.append((nx, ny))
    
    return neighbors

# A* algorithm
def a_star(grid, start, goal):
    open_list = []
    closed_list = set()
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    parent = {start: None}
    
    heapq.heappush(open_list, (f_score[start], start))

    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        closed_list.add(current)

        for neighbor in get_neighbors(current, grid):
            if neighbor in closed_list:
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                parent[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # No path found

# Main function to get input from the user
def main():
    # Get grid dimensions
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # Create the grid
    grid = []
    print("Enter the grid row by row (0 for empty, 1 for obstacle):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        grid.append(row)

    # Get start and goal positions
    start_x, start_y = map(int, input("Enter start node coordinates (x y): ").split())
    goal_x, goal_y = map(int, input("Enter goal node coordinates (x y): ").split())

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    # Run A* algorithm
    path = a_star(grid, start, goal)
    
    if path:
        print("Path found:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()

