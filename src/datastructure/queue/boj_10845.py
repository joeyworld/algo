import sys

queue = {
    'front': 0,
    'back': 0
}


def push(X):
    queue[queue['back']] = X
    queue['back'] += 1


def pop():
    if size() == 0:
        return -1
    element = queue[queue['front']]
    del queue[queue['front']]
    queue['front'] += 1
    return element


def size():
    return queue['back'] - queue['front']


def empty():
    return 1 if size() == 0 else 0


def front():
    if size() == 0:
        return - 1
    return queue[queue['front']]


def back():
    if size() == 0:
        return - 1
    return queue[queue['back'] - 1]


def operate(command):
    action = command[0]

    if action == 'push':
        push(int(command[1]))
    elif action == 'pop':
        print(pop())
    elif action == 'size':
        print(size())
    elif action == 'empty':
        print(empty())
    elif action == 'front':
        print(front())
    elif action == 'back':
        print(back())


def main():
    N = int(sys.stdin.readline())
    for _ in range(N):
        command = sys.stdin.readline().rstrip().split(' ')
        operate(command)


if __name__ == '__main__':
    main()
