previous_solutions = [None] * 1000
previous_solutions[0] = 1
previous_solutions[1] = 3


def solve(n):
    for i in range(2, n):
        previous_solutions[i] = (
            previous_solutions[i - 1] + 2 * previous_solutions[i - 2]) % 10007


if __name__ == '__main__':
    n = int(input())
    solve(n)
    print(previous_solutions[n - 1])
