def main():
    N = int(input())
    i = 0
    while True:
        max = 3 * i * (i + 1)
        if N - 1 <= max:
            print(i + 1)
            return
        i += 1


if __name__ == '__main__':
    main()
