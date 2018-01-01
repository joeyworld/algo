previous_answers = [[0] * 100000 for _ in range(3)]

# 첫번째 : 위에 고를때
# 두번째 : 아래 고를떄
# 3번째 : 안고를때


def solve(arr, n, total):
    if n == total:
        previous_answers[0][n - 1] = arr[0][total - 1]
        previous_answers[1][n - 1] = arr[1][total - 1]
    else:
        previous_answers[0][n - 1] = arr[0][n - 1] + \
            max(previous_answers[1][n], previous_answers[2][n])
        previous_answers[1][n - 1] = arr[1][n - 1] + \
            max(previous_answers[0][n], previous_answers[2][n])
        previous_answers[2][n - 1] = max(previous_answers[0]
                                         [n], previous_answers[1][n], previous_answers[2][n])


if __name__ == '__main__':
    testcase = int(input())
    answers = list()

    for _ in range(testcase):
        num_stickers = int(input())
        stickers = [list(map(int, input().split(' '))) for _ in range(2)]
        for i in range(0, num_stickers):
            solve(stickers, (num_stickers - i), num_stickers)

        answers.append(
            max(previous_answers[0][0], previous_answers[1][0], previous_answers[2][0]))

        previous_answers = [[0] * 100000 for _ in range(3)]


    for answer in answers:
        print(answer)
