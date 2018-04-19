import sys

n = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(n)])
[sys.stdout.write('{}\n'.format(number)) for number in numbers]
