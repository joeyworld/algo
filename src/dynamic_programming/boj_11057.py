previous_answer = [1] * 10
next_answer = previous_answer


def solve(n):
    if n == 1:
        return

    for _ in range(2, n + 1):
        next_answer[:] = [sum(previous_answer[j:]) % 10007 for j in range(10)]
        previous_answer[:] = next_answer


if __name__ == '__main__':
    N = int(input())
    solve(N)
    print(sum(next_answer) % 10007)
