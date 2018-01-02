def hanoi(n, origin, temp, target):
    if n == 1:
        print('{} {}'.format(origin, target))
        return
    else:
        hanoi(n - 1, origin, target, temp)
        print('{} {}'.format(origin, target))
        hanoi(n - 1, temp, origin, target)


if __name__ == '__main__':
    n = int(input())
    print(2 ** n - 1)
    if n <= 20:
        hanoi(n, 1, 2, 3)
