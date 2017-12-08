def solve(num_people, times):
    solution = 0
    prev = 0
    for i in range(num_people):
        times[i] = int(times[i])

    times.sort()
    for time in times:
        prev += time
        solution += prev
    return solution


if __name__ == '__main__':
    n = int(input())
    p = input().split(' ')
    print(solve(n, p))
