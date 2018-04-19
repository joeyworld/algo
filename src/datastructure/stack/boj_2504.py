def solve(sentence):
    stack = []
    top = -1
    depth = 0
    total = []

    for element in sentence:
        if element == '(':
            stack.append(2)
            top += 1
        elif element == '[':
            stack.append(3)
            top += 1
        else:
            if top == -1:
                return 0
            if element == ')' and stack[top] != 2:
                return 0
            if element == ']' and stack[top] != 3:
                return 0
            else:
                pair = stack[top]
                del stack[top]
                top -= 1

                # TODO multiplication or addition ?
                current_depth = top + 1

                if current_depth >= depth:
                    product = 1
                    for i in range(current_depth):
                        product *= stack[i]
                    # print(pair, product)
                    total.append(pair * product)
                depth = current_depth

        # print(stack, total, top, depth)

    if top != -1:
        return 0
    else:
        return sum(total)


def main():
    sentence = input()
    print(solve(sentence))


if __name__ == '__main__':
    main()
