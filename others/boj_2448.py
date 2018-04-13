import sys

stars = [[0] * 6143 for _ in range(3072)]


def find_star(x, y, size):
    if size <= 3:
        stars[y][x] = 1

        stars[y + 1][x - 1] = 1
        stars[y + 1][x + 1] = 1

        stars[y + 2][x + 2] = 1
        stars[y + 2][x + 1] = 1
        stars[y + 2][x] = 1
        stars[y + 2][x - 1] = 1
        stars[y + 2][x - 2] = 1
    else:
        size //= 2
        find_star(x, y, size)
        find_star(x - size, y + size, size)
        find_star(x + size, y + size, size)


def print_star(n):
    vertical = n
    horizontal = 2 * n - 1

    for i in range(vertical):
        for j in range(horizontal):
            if stars[i][j] == 1:
                sys.stdout.write('*')
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')


if __name__ == '__main__':
    N = int(input())
    find_star(N - 1, 0, N)
    print_star(N)
