def solve(n, grid):
    cavs = []

    # find
    for y in range(1, n - 1):
        for x in range(1, n - 1):
            curr = grid[y][x]
            east = grid[y][x + 1]
            west = grid[y][x - 1]
            south = grid[y + 1][x]
            north = grid[y - 1][x]

            if max([east, west, south, north]) < curr:
                cavs.append((y, x))

    # rep
    for cav in cavs:
        y, x = cav
        line = list(grid[y])
        line[x] = 'X'
        grid[y] = ''.join(line)

    return grid


if __name__ == '__main__':
    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = solve(n, grid)
    print(result)
