previous_scores = [0] * 301


def solve(num_stairs, points):
    if num_stairs < 3:
        print(previous_scores[num_stairs])
        return
    else:
        return points[num_stairs - 1] + solve(num_stairs - 1)


if __name__ == '__main__':
    num_stairs = int(input())
    points = [int(input()) for _ in range(num_stairs)]

    previous_scores[1] = points[0]
    if num_stairs > 1:
        previous_scores[2] = points[0] + points[1]

    print()
    print(points)
    solve(num_stairs, points)
