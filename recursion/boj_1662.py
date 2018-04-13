def unzip(compressed, index):
    total = 0
    length = len(compressed)

    while index < length:
        # print(compressed[index:])
        if compressed[index] == '(':
            total -= 1
            recursive_call = unzip(compressed, index + 1)
            total += int(compressed[index - 1]) * recursive_call[0]
            index = recursive_call[1] + 1

        elif compressed[index] == ')':
            # print('returning ({}, {})'.format(total, index))
            return (total, index)

        else:
            index += 1
            total += 1

    return (total, index)

if __name__ == '__main__':
    sentence = input()
    print(unzip(sentence, 0)[0])
