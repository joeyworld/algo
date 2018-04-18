previous_answers = [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
next_answers = [1] * 10


def solve(n):
    if n == 1:
        return
    elif n == 2:
        next_answers[:] = previous_answers
        return

    for i in range(3, n + 1):
        next_answers[0] = (previous_answers[1]) % 1000000000

        for j in range(1, 9):
            next_answers[j] = (((previous_answers[j - 1]) % 1000000000) +
                               (previous_answers[j + 1] % 1000000000)) % 1000000000

        next_answers[9] = (previous_answers[8]) % 1000000000
        previous_answers[:] = next_answers


if __name__ == '__main__':
    N = int(input())
    solve(N)
    print(sum(next_answers[1:]) % 1000000000)
