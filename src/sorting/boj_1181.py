def solve(words_list):
    words_list = list(sorted(set(words_list), key=lambda x: len(x)))

    n = len(words_list)
    temp_index = 0
    num_equal_words = 0

    start = 0
    end = 1
    while True:
        if end == n:
            words_list[start:end] = sorted(words_list[start:end])
            break
        elif len(words_list[start]) != len(words_list[end]):
            words_list[start:end] = sorted(words_list[start:end])
            start = end
        end += 1

    for word in words_list:
        print(word)


if __name__ == '__main__':
    num_words = int(input())
    words = [input() for _ in range(num_words)]
    solve(words)
