previous_answers = [None] * 12
previous_answers[0] = 1
previous_answers[1] = 1
previous_answers[2] = 2


def solve(n):
    for i in range(3, n + 1):
        previous_answers[i] = previous_answers[i - 1] + \
            previous_answers[i - 2] + previous_answers[i - 3]


if __name__ == '__main__':
    input_case = int(input())
    inputs = [int(input()) for _ in range(input_case)]
    [solve(single_input) for single_input in inputs]
    for single_input in inputs:
        print(previous_answers[single_input])
