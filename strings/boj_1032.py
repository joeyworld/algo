def find_pattern(given):
    total = len(given)
    pattern = given[0]
    to_compare = len(pattern)
    for i in range(1, total):
        for j in range(to_compare):
            if given[i][j] != pattern[j]:
                pattern = pattern[:j] + '?' + pattern[j + 1:]
    return pattern


if __name__ == '__main__':
    n = int(input())
    test_case = [input() for _ in range(n)]
    # print(test_case)
    print(find_pattern(test_case))
