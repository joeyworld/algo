def solve(k, s1, s2):
    n = len(s1)
    substr_tbl = [[0] * (n + 1) for _ in range(n + 1)]
    k_tbl = [[0] * (n + 1) for _ in range(n + 1)]
    max_len = 0

    for i in range(n):
        for j in range(n):
            if s1[i] == s2[j]:
                new_len = substr_tbl[i][j] + 1
                substr_tbl[i + 1][j + 1] = new_len
                if max_len < new_len:
                    max_len = new_len
            elif k_tbl[i][j] <= k:
                pass
    return max_len


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k, s1, s2 = input().split()
        print(solve(int(k), s1, s2))
