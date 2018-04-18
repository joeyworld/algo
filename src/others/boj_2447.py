stars = [[0] * 2187 for _ in range(2187)]


def find_stars(xpos, ypos, size):
    if size == 1:
        stars[0][0] = 1
        return

    if size == 3:
        stars[ypos][xpos] = 1
        stars[ypos][xpos + 1] = 1
        stars[ypos][xpos + 2] = 1

        stars[ypos + 1][xpos] = 1
        stars[ypos + 1][xpos + 2] = 1

        stars[ypos + 2][xpos] = 1
        stars[ypos + 2][xpos + 1] = 1
        stars[ypos + 2][xpos + 2] = 1
    else:
        size //= 3
        find_stars(xpos, ypos, size)
        find_stars(xpos + (size * 1), ypos, size)
        find_stars(xpos + (size * 2), ypos, size)

        find_stars(xpos, ypos + (size * 1), size)
        find_stars(xpos + (size * 2), ypos + (size * 1), size)

        find_stars(xpos, ypos + (size * 2), size)
        find_stars(xpos + (size * 1), ypos + (size * 2), size)
        find_stars(xpos + (size * 2), ypos + (size * 2), size)


def main():
    N = int(input())
    find_stars(0, 0, N)
    for i in range(N):
        for j in range(N):
            print('*', end='') if stars[i][j] == 1 else print(' ', end='')
        print()


if __name__ == '__main__':
    main()
