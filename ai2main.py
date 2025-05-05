goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # 0 represents the blank space

# Define the possible moves for the empty space
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
DIRECTIONS = ['Up', 'Down', 'Left', 'Right']  # Corresponding directions for each move

# Function to compute Manhattan Distance heuristic
def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(9):
        if state[i] == 0:
            continue
        target_pos = goal_state.index(state[i])
        target_row, target_col = target_pos // 3, target_pos % 3
        current_row, current_col = i // 3, i % 3
        distance += abs(current_row - target_row) + abs(current_col - target_col)
    return distance

# Function to get the neighbors of the current state, along with the direction of movement
def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)
    zero_row, zero_col = zero_pos // 3, zero_pos % 3

    for idx, (dr, dc) in enumerate(MOVES):
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_pos = new_row * 3 + new_col
            new_state = list(state)
            # Swap the zero with the adjacent tile
            new_state[zero_pos], new_state[new_zero_pos] = new_state[new_zero_pos], new_state[zero_pos]
            neighbors.append((tuple(new_state), DIRECTIONS[idx]))  # Add direction along with new state
    
    return neighbors

# Function to print a state in 3x3 matrix format
def print_state(state):
    for i in range(0, 9, 3):
        print(' '.join('_' if state[j] == 0 else str(state[j]) for j in range(i, i + 3)))
    print()

# A* search algorithm using simple data structures
def a_star_search(start_state, goal_state):
    open_list = []
    closed_list = set()
    open_list.append((start_state, [], manhattan_distance(start_state, goal_state)))

    iteration = 0

    while open_list:
        iteration += 1
        # Sort by the heuristic + path length (f = g + h)
        open_list.sort(key=lambda x: len(x[1]) + x[2])  # f = g + h

        current_state, path, h_value = open_list.pop(0)

        # Print current possibilities
        print(f"ITERATION {iteration} POSSIBILITIES:")

        neighbors_with_h = []
        for neighbor, direction in get_neighbors(current_state):
            h = manhattan_distance(neighbor, goal_state)
            neighbors_with_h.append((neighbor, direction, h))

        # Sort neighbors by their h values
        neighbors_with_h.sort(key=lambda x: x[2])

        for neighbor, direction, h in neighbors_with_h:
            print_state(neighbor)
            print(f"Move: {direction}, h={h}\n")

        # Select the state with the minimum h value
        best_neighbor = neighbors_with_h[0][0]
        print(f"Since minimum h value is {neighbors_with_h[0][2]}, matrix selected:")
        print_state(best_neighbor)

        # If the goal state is reached, return the solution path
        if best_neighbor == goal_state:
            print("HENCE FINAL MATRIX REACHED:")
            print_state(best_neighbor)
            return path + [current_state]

        if best_neighbor in closed_list:
            continue
        closed_list.add(best_neighbor)

        # Add the best neighbor to the open list with the updated path and h value
        open_list.append((best_neighbor, path + [current_state], manhattan_distance(best_neighbor, goal_state)))

    return None  # No solution found

# Helper function to input the state as a 3x3 matrix
def input_state(name):
    print(f"Enter the {name} state (3x3 matrix with numbers 1-8 and _ for blank space):")
    state = []
    for i in range(3):
        row = input(f"Enter row {i+1}: ").split()
        # Convert _ to 0 for blank space
        state.extend([0 if x == '_' else int(x) for x in row])
    return tuple(state)

# Main code to take user input and run the algorithm
def main():
    # Input initial and goal states
    initial_state = input_state("initial")
    goal_state = input_state("goal")
    
    # Run A* search
    print("\nRunning A* search...\n")
    solution = a_star_search(initial_state, goal_state)

    if solution:
        print("\nSolution found:")
        for step in solution:
            print_state(step)
    else:
        print("No solution found.")

# Run the main function
if __name__ == "__main__":
    main()

