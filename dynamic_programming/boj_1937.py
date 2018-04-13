def solve(forest, dimension):
    visited = [False] * (dimension ** 2)
    max_path_length = -1

    i = 0
    j = 0

    while True:
        if dimension * (i + 1) + j + 1 == dimension ** 2:
            break
        if visited[i * dimension + j] is False:
            path_from_spot = dfs(forest, visited, dimension, i, j)
            max_length = lis(path_from_spot)
            if lis(path_from_spot) > max_path_length:
                max_path_length = max_length

        visited[i * dimension + j] = True
        j += 1
        if j % dimension == 0:
            j = 0
            i += 1
    return max_path_length


def dfs(forest, visited, dimension, row, col):
    visited[row * dimension + col] = True
    current = forest[row][col]
    result = [current]
    # search up
    if is_out_of_bounds(dimension, row - 1, col) is False and forest[row - 1][col] > current:
        result.append(dfs(forest, visited, dimension, row - 1, col))
    # search left
    if is_out_of_bounds(dimension, row, col - 1) is False and forest[row][col - 1] > current:
        result.append(dfs(forest, visited, dimension, row, col - 1))
    # search down
    if is_out_of_bounds(dimension, row + 1, col) is False and forest[row + 1][col] > current:
        result.append(dfs(forest, visited, dimension, row + 1, col))
    # search right
    if is_out_of_bounds(dimension, row, col + 1) is False and forest[row][col + 1] > current:
        result.append(dfs(forest, visited, dimension, row, col + 1))
    return result


def is_out_of_bounds(dimension, row, col):
    if row < 0 or row >= dimension:
        return True
    elif col < 0 or col >= dimension:
        return True
    else:
        return False


def lis(segment):
    n = len(segment)
    lengths = []
    if n <= 2:
        return n

    for i in range(n - 1):
        subseg_length = len(segment[i + 1])
        if subseg_length <= 2:
            lengths.append(subseg_length)
        else:
            lengths.append(lis(segment[i + 1]))
    return max(lengths) + 1


if __name__ == '__main__':
    N = int(input())
    sample_forest = [input().split(' ') for _ in range(N)]
    sample_forest = [[int(x) for x in sample_forest[i]] for i in range(N)]
    print(solve(sample_forest, N))
