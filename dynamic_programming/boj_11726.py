prev_solution = [None] * 1001
prev_solution[0] = 1
prev_solution[1] = 2


def solve(n):
    for i in range(2, n):
        prev_solution[i] = (prev_solution[i - 1] +
                            prev_solution[i - 2]) % 10007


if __name__ == '__main__':
    n = int(input())
    solve(n)
    print(prev_solution[n - 1])
