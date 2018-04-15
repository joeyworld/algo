import sys
from collections import deque


def insert(value):
    pass


def delete(value):
    pass


queue = dict()
function_table = {'I': insert, 'D': delete}


def print_result():
    pass


def main():
    k = int(sys.stdin.readline())
    for _ in range(k):
        operation, value = sys.stdin.readline().split(' ')
        value = int(value)
        function_table[operation](value)
    print_result()
    queue.clear()


if __name__ == '__main__':
    # 삽입 O(1)
    # 삭제 O(1)
    # 찾기 O(N)
    [main() for _ in range(int(sys.stdin.readline()))]
