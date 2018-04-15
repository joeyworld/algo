croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


def main():
    word = input()
    size = len(word)
    croatian_size = size
    index = 0

    while index < size:
        if word[index:index + 3] == 'dz=':
            croatian_size -= 2
            index += 3
        elif word[index:index + 2] in croatian_alphabet:
            croatian_size -= 1
            index += 2
        else:
            index += 1

    print(croatian_size)


if __name__ == '__main__':
    main()
