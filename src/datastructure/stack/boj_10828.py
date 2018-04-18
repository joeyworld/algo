stack = []
top = -1


def push(element):
    global stack
    global top
    stack.append(element)
    top += 1


def pop():
    global stack
    global top
    if top == -1:
        return top
    else:
        element = stack[top]
        del stack[top]
        top -= 1
        return element


def operate(command):
    global stack
    global top

    action = command[0]

    if action == 'push':
        value = int(command[1])
        push(value)
    elif action == 'pop':
        print(pop())
    elif action == 'top':
        print(-1 if top == -1 else stack[top])
    elif action == 'size':
        print(top + 1)
    elif action == 'empty':
        print(1 if top == -1 else 0)


def main():
    N = int(input())
    for _ in range(N):
        command = input().split(' ')
        operate(command)


if __name__ == '__main__':
    main()
