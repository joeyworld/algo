previous_answers = [0] * 90
previous_answers[0] = 1
previous_answers[1] = 1
previous_answers[2] = 2


def solve(n):
    if n < 3:
        return

    for i in range(3, n):
        previous_answers[i] = 1 + sum(previous_answers[0:i - 1])


if __name__ == '__main__':
    n = int(input())
    solve(n)
    print(previous_answers[n - 1])
