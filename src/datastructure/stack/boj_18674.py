def main():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    operations = ['+']
    stack = [1]
    top = 0

    next_push_number = 2
    index = 0

    while True:
        need = numbers[index]

        if need == next_push_number:
            next_push_number += 1
            index += 1
            operations.append('+')
            operations.append('-')
        elif need > next_push_number:
            stack.append(next_push_number)
            next_push_number += 1
            top += 1
            operations.append('+')
            pass
        else:
            element = stack[top]
            if element != need:
                print('NO')
                return
            else:
                del stack[top]
                top -= 1
                operations.append('-')
                index += 1

        if index == n and top == -1:
            break

    [print(operation) for operation in operations]


if __name__ == '__main__':
    main()
