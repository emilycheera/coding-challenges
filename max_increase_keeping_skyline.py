def max_increase_keeping_skyline(grid):

    max_increase = 0

    # Visit each building in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            # Get the max building height in the row
            max_row = max(grid[i])

            # Get the max building height in the column
            max_col = max([grid[k][j] for k in range(len(grid))])

            # The building can grow the min of the max_row and max_col
            # Add how much the building can grow to max_increase
            max_increase += min(max_row, max_col) - grid[i][j]

    return max_increase


def max_increase_keeping_skyline_faster(grid):

    max_increase = 0

    # Get the max building height in each row
    max_rows = [max(grid[i]) for i in range(len(grid))]

    # Get the max building height in each column
    max_cols = [
        max([grid[k][j] for k in range(len(grid))]) for j in range(len(grid[0]))
    ]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_increase += min(max_rows[i], max_cols[j]) - grid[i][j]

    return max_increase
