def solve(obstacles, num_obs, num_roads):
    top_down = obstacles[0::2]
    bottom_up = obstacles[1::2]
    top_down.sort()
    bottom_up.sort()

    print(top_down)
    print(bottom_up)
    return (-1, -1)


if __name__ == '__main__':
    N, H = input().split(' ')
    N = int(N)
    H = int(N)
    obs_list = [int(input()) for _ in range(N)]
    answer = solve(obs_list, N, H)
    print('{} {}'.format(answer[0], answer[1]))
