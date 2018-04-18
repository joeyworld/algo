def solve(start, dest):
    answer = 0
    dist = dest - start

    index = 0
    while True:
        if answer >= dist:
            return index
        else:
            index += 1
            answer += ((index - 1) // 2 + 1)


def main():
    start, dest = input().split(' ')
    start = int(start)
    dest = int(dest)

    print(solve(start, dest))


if __name__ == '__main__':
    [main() for _ in range(int(input()))]
