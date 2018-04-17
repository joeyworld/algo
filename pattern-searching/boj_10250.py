def main():
    H, W, N = input().split(' ')
    H = int(H)
    W = int(W)
    N = int(N)

    floor = H if N % H == 0 else N % H
    room = (N - 1) // H + 1

    print(floor * 100 + room)


if __name__ == '__main__':
    [main() for _ in range(int(input()))]
