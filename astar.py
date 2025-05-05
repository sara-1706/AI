import heapq

# Define the directions for moving the blank space (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_row, target_col = divmod(value - 1, 3)
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

# Function to find the possible moves for the blank space (0)
def get_successors(state):
    successors = []
    blank_pos = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    x, y = blank_pos
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Swap blank space with adjacent tile
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            successors.append(new_state)
    return successors

# A* algorithm
def a_star(initial_state, goal_state):
    # Priority queue for open states, stores (f(n), g(n), state, path)
    open_list = []
    # Set to store visited states to avoid loops
    closed_list = set()
    
    # The starting state has g(n) = 0 and h(n) = Manhattan distance to goal
    g = 0
    h = manhattan_distance(initial_state)
    f = g + h
    
    # Push initial state into the priority queue
    heapq.heappush(open_list, (f, g, initial_state, []))
    iteration = 0
    
    while open_list:
        # Pop the state with the lowest f(n)
        f, g, current_state, path = heapq.heappop(open_list)
        
        # Calculate the heuristic value (Manhattan distance) for the current state
        h = manhattan_distance(current_state)
        iteration += 1
        
        # Print iteration, current state, and heuristic value (h)
        print(f"Iteration {iteration}:")
        print(f"Current state (h={h}):")
        for row in current_state:
            print(" ".join(['_' if val == 0 else str(val) for val in row]))
        print()
        
        # If we reach the goal, return the solution path
        if current_state == goal_state:
            print("Goal state reached!")
            return path + [current_state]
        
        # If the current state has been visited, skip it
        state_tuple = tuple(map(tuple, current_state))
        if state_tuple in closed_list:
            continue
        closed_list.add(state_tuple)
        
        # Generate successors (neighboring states)
        for successor in get_successors(current_state):
            if tuple(map(tuple, successor)) not in closed_list:
                new_g = g + 1
                new_h = manhattan_distance(successor)
                new_f = new_g + new_h
                heapq.heappush(open_list, (new_f, new_g, successor, path + [current_state]))
    
    return None  # No solution found

# Function to take input from the user for the state, interpreting "_" as blank space
def get_state_input(prompt):
    print(prompt)
    state = []
    for i in range(3):
        row = input(f"Enter row {i+1} (space-separated): ").split()
        # Convert "_" to 0
        row = [0 if x == "_" else int(x) for x in row]
        if len(row) != 3 or any(val < 0 or val > 8 for val in row):
            print("Invalid input! Each row must contain 3 numbers between 0 and 8, with _ representing the blank space.")
            return None
        state.append(row)
    return state

# Main function to drive the program
def main():
    # Take initial and goal states from the user
    initial_state = get_state_input("Enter the initial state:")
    if initial_state is None:
        return
    
    goal_state = get_state_input("Enter the goal state:")
    if goal_state is None:
        return
    
    print("Searching for a solution...\n")
    
    # Run A* algorithm to find the solution
    solution = a_star(initial_state, goal_state)

    if solution:
        print("Solution found:")
        for step in solution:
            for row in step:
                print(" ".join(['_' if val == 0 else str(val) for val in row]))
            print()
    else:
        print("No solution found.")

# Run the program
if __name__ == "__main__":
    main()

