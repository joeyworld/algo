def solve(num_words, words):
    check_result = [word for word in words if check_group(word) is True]
    return len(check_result)


def check_group(word):
    n = len(word)
    prev = [word[0]]
    for i in range(n - 1):
        if word[i] != word[i + 1]:
            if word[i + 1] in prev:
                return False
            prev.append(word[i + 1])
    return True


if __name__ == '__main__':
    num_words = int(input())
    words = [input() for _ in range(num_words)]
    print(solve(num_words, words))
