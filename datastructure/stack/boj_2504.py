def solve(sentence)
    stack = []
    top = 0
    value = 0
    for word in sentence:
        if word == '(':
            stack.append(2)
            top += 1
        if word == '[':
            stack.append(3)
            top += 1
        if word == ')':
            if stack[top] == 2:
                top -= 1
                pass
            else:
                return 0
        if word == ']':
            if stack[top] == 3:
                top -= 1
                pass
            else:
                return 0

    if top != 0:
        return 0
    return value


def main():
    sentence = input()
    print(solve(sentence))


if __name__ == '__main__':
    main()
