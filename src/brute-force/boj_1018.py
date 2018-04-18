import sys

chessboard = [[0] * 50 for _ in range(50)]
lines = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]


def calculate_color_need(y_index, x_index):
    total = [0, 0]
    indices = [0, 1]

    for i in range(y_index, y_index + 8):
        line = chessboard[i][x_index:x_index + 8]
        for j in range(2):
            total[j] += sum([abs(a - b)
                             for a, b in zip(line, lines[indices[j]])])
        indices[0], indices[1] = indices[1], indices[0]

    return min(total)


def solve(vertical, horizontal):
    vertical_need = vertical - 7
    horizontal_need = horizontal - 7
    need_to_be_colored = list()

    for i in range(vertical_need):
        for j in range(horizontal_need):
            need_to_be_colored.append(calculate_color_need(i, j))

    return min(need_to_be_colored)


if __name__ == '__main__':
    vertical, horizontal = sys.stdin.readline().split(' ')
    vertical, horizontal = int(vertical), int(horizontal)

    for i in range(vertical):
        line = sys.stdin.readline()
        chessboard[i] = [0 if line[j] == 'B' else 1 for j in range(horizontal)]

    print(solve(vertical, horizontal))
