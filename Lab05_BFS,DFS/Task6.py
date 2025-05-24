from collections import deque

delta_row = [0, 0, 1, -1]
delta_col = [1, -1, 0, 0]

def bfs(grid, visited_cells, start_row, start_col, num_rows, num_cols):
    if start_row < 0 or start_row >= num_rows or start_col < 0 or start_col >= num_cols or grid[start_row][start_col] == '#' or visited_cells[start_row][start_col]:
        return 0

    d_count = 0
    search_queue = deque([(start_row, start_col)])
    visited_cells[start_row][start_col] = True
    if grid[start_row][start_col] == 'D':
        d_count += 1

    while search_queue:
        current_row, current_col = search_queue.popleft()

        for i in range(4):
            next_row = current_row + delta_row[i]
            next_col = current_col + delta_col[i]

            if 0 <= next_row < num_rows and 0 <= next_col < num_cols and grid[next_row][next_col] != '#' and not visited_cells[next_row][next_col]:
                visited_cells[next_row][next_col] = True
                search_queue.append((next_row, next_col))
                if grid[next_row][next_col] == 'D':
                    d_count += 1
    return d_count

def find_max_count():
    num_rows, num_cols = map(int, input().split())
    grid = []
    for i in range(num_rows):
        grid.append(input().strip())  

    max_d = 0
    visited = [[False for i in range(num_cols)] for i in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            max_d = max(max_d, bfs(grid, visited, i, j, num_rows, num_cols))
    print(max_d)

find_max_count()

























