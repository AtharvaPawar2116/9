import heapq

# Directions for moving on the grid (left, right, up, down)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    """Calculate Manhattan Distance heuristic"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, grid):
    """A* algorithm to find the shortest path"""
    open_list = []
    closed_list = set()
    came_from = {}

    # f, g, and h scores for each node
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    # Push the start node to the open list
    heapq.heappush(open_list, (f_score[start], start))

    while open_list:
        _, current = heapq.heappop(open_list)
        
        # If we've reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        closed_list.add(current)

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            # Check if the neighbor is within the grid and not blocked
            if (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and 
                grid[neighbor[0]][neighbor[1]] == 1 and neighbor not in closed_list):
                
                tentative_g_score = g_score[current] + 1  # Assuming all moves cost 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # Return None if no path is found

# Function to take grid input from the user
def take_grid_input():
    rows = int(input("Enter the number of rows in the grid: "))
    cols = int(input("Enter the number of columns in the grid: "))
    grid = []

    print("Enter the grid row by row, use 1 for walkable and 0 for blocked:")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        grid.append(row)

    return grid

# Function to take start and goal node input from the user
def take_start_goal_input():
    start = tuple(map(int, input("Enter the start node (row, column): ").split()))
    goal = tuple(map(int, input("Enter the goal node (row, column): ").split()))
    return start, goal

# Main function
def main():
    # Take grid, start, and goal input from the user
    grid = take_grid_input()
    start, goal = take_start_goal_input()

    # Call the A* algorithm with the user inputs
    path = a_star(start, goal, grid)

    # Output the result
    if path:
        print("Path found:", path)
    else:
        print("No path found.")

# Run the program
main()
