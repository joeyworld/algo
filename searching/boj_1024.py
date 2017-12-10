def solve(total, length):
    while length < 101:
            base = total // length
            flag = [False, False]
            while True:
                seq = [(base + i) for i in range(length)]
                sum_of_seq = sum(seq)
                if sum_of_seq == total:
                    return seq
                elif sum_of_seq > total:
                    base -= 1
                    flag[1] = True
                    if base < 0:
                        break
                else:
                    base += 1
                    flag[0] = True
                if flag == [True, True]:
                    break
            length += 1
    return None


if __name__ == '__main__':
    N, L = input().split(' ')
    seq = solve(int(N), int(L))

    if seq is None:
        print(-1)
    else:
        for num in seq:
            print(num, end=' ')
        print()
