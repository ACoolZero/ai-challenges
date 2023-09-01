import random

def generate_random_maze(rows, columns):
    # Initialize maze grid with all walls
    maze = [['W' for _ in range(columns)] for _ in range(rows)]

    # Choose a random starting point
    start_row = random.randrange(rows)
    start_col = random.randrange(columns)
    maze[start_row][start_col] = 'P'  # Mark starting point as passage

    # List to store walls for Randomized Prim's Algorithm
    walls = [(start_row + dr, start_col + dc) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]]

    while walls:
        wall_row, wall_col = walls.pop(random.randrange(len(walls)))
        adjacent_cells = [(wall_row + dr, wall_col + dc) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        passage_count = sum(1 for r, c in adjacent_cells if 0 <= r < rows and 0 <= c < columns and maze[r][c] == 'P')

        if passage_count == 1:
            maze[wall_row][wall_col] = 'P'  # Make wall a passage

            for r, c in adjacent_cells:
                if 0 <= r < rows and 0 <= c < columns and maze[r][c] == 'W':
                    walls.append((r, c))

    return maze

# Generate and print a random maze
rows = 10
columns = 10
random_maze = generate_random_maze(rows, columns)
for row in random_maze:
    print(' '.join(row))
