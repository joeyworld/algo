def solve(x, y):
    # base case
    x = int(x)
    y = int(y)
    if x < 2 and y < 2:
        return 2 * x + y

    e = 2
    while True:
        if x // e == 0 and y // e == 0:
            e /= 2
            break
        else:
            e *= 2
    return int(2 * e * e * (x // e) + e * e * (y // e)) + (solve(x % e, y % e))


if __name__ == '__main__':
    N, r, c = input().split(' ')
    print(solve(r, c))
