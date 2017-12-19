def solve(coordinates):
    """
    정렬된 좌표를 리턴
    """
    # sort by x coord
    coordinates.sort(key=lambda x: x[0])

    # sort by y coord if x-coord equal
    start = 0
    end = 1
    n = len(coordinates)
    while True:
        if coordinates[start][0] == coordinates[end][0]:
            end += 1
        else:
            coordinates[start:end] = sorted(
                coordinates[start:end], key=lambda x: x[1])
            start = end

        if end == n:
            coordinates[start:end] = sorted(
                coordinates[start:end], key=lambda x: x[1])
            break

    return coordinates


if __name__ == '__main__':
    N = int(input())
    coordinates = list()
    for _ in range(N):
        x_cor, y_cor = input().split(' ')
        x_cor = int(x_cor)
        y_cor = int(y_cor)
        coordinates.append((x_cor, y_cor))

    coordinates = solve(coordinates)
    for coordinate in coordinates:
        print('{} {}'.format(coordinate[0], coordinate[1]))
