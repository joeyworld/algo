def is_cyclic(word1, word2):
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        new_word = word1[i:] + word1[:i]
        if new_word == word2:
            return True
    return False


def find_different_words(words):
    n = len(words)
    for i in range(n):
        j = i + 1
        while j < n:
            if is_cyclic(words[i], words[j]) is True:
                del words[j]
                n -= 1
            else:
                j += 1
    return len(words)


if __name__ == '__main__':
    num_words = int(input())
    sample = [input() for _ in range(num_words)]
    print(find_different_words(sample))
