previous = [[0 for _ in range(10000)] for _ in range(3)]
# 다음 두개다 / 앞에꺼만 / 뒤에꺼만


def solve(wine, n, total):
    if n == total:
        previous[0][n - 1] = wine[n - 1]
        previous[1][n - 1] = wine[n - 1]
        previous[2][n - 1] = 0
        return

    if n == total - 1:
        previous[0][n - 1] = wine[n - 1] + wine[n]
        previous[1][n - 1] = wine[n - 1]
        previous[2][n - 1] = wine[n]
        return

    if n == total - 2:
        previous[0][n - 1] = wine[n - 1] + wine[n]
        previous[1][n - 1] = wine[n - 1] + wine[n + 1]
        previous[2][n - 1] = wine[n] + wine[n + 1]
        return

    previous[0][n - 1] = wine[n - 1] + wine[n] + \
        max(previous[0][n + 2], previous[1][n + 2], previous[2][n + 2])
    previous[1][n - 1] = wine[n - 1] + \
        max(previous[0][n + 1], previous[1][n + 1], previous[2][n + 1])
    previous[2][n - 1] = max(previous[0][n],
                             previous[1][n], previous[2][n])


if __name__ == '__main__':
    n = int(input())
    wine = [int(input()) for _ in range(n)]
    for i in range(n):
        solve(wine, (n - i), n)
    print(max(previous[0][0], previous[1][0], previous[2][0]))
