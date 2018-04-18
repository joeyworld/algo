def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    n, r = input().split(' ')
    n = int(n)
    r = int(r)

    print(factorial(n) // (factorial(r) * factorial(n - r)))


if __name__ == '__main__':
    main()
