def solve(board):
    # (0,0) 은 흰색
    # 짝수줄 : 0246
    # 홀수줄 : 1357
    total = 0

    # 짝수줄 먼저
    for i in range(4):
        for j in range(4):
            # print('({}, {}) : {}'.format(2 * i, 2 * j, board[2 * i][2 * j]))
            if board[2 * i][2 * j] is 'F':
                total += 1

    # 홀수줄은 나중에
    for i in range(4):
        for j in range(4):
            # print('({}, {}) : {}'.format(2 * i + 1, 2 * j + 1, board[2 * i + 1][2 * j + 1]))
            if board[2 * i + 1][2 * j + 1] is 'F':
                total += 1

    return total


if __name__ == '__main__':
    board = [input() for _ in range(8)]
    # print(board)
    print(solve(board))
