def is_palindrome(word):
    n = len(word)
    for i in range(n // 2):
        if word[i] != word[n - i - 1]:
            return 0
    return 1


if __name__ == '__main__':
    string = input()
    print(is_palindrome(string))
