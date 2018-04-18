previous_solution = [None] * (10 ** 6)
previous_solution[0] = 0
previous_solution[1] = 1
previous_solution[2] = 1


def solve(n):
    if n < 4:
        return
    for i in range(4, n + 1):
        answer = list()
        if i % 3 == 0:
            answer.append(1 + previous_solution[i // 3 - 1])
        if i % 2 == 0:
            answer.append(1 + previous_solution[i // 2 - 1])
        answer.append(1 + previous_solution[i - 2])
        previous_solution[i - 1] = min(answer)
    return


if __name__ == '__main__':
    N = int(input())
    solve(N)
    print(previous_solution[N - 1])
