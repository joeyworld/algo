def append_and_delete(s, t, k):
    len_s = len(s)
    len_t = len(t)

    if k >= len(s) + len(t):
        return 'Yes'

    min_op = 0
    minlen = min([len_s, len_t])

    cnt = 0
    for i in range(minlen):
        if s[i] == t[i]:
            cnt += 1
        else:
            break

    min_op = len_s + len_t - (2 * cnt)

    if k < min_op:
        return 'No'
    return 'Yes' if (k - min_op) % 2 == 0 else 'No'


if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input().strip())
    print(append_and_delete(s, t, k))
