import math


def solve(coordinates):
    """
    알고리즘 풀이 함수 : 두 점의 최단거리를 구해주는 함수
    :param coordinates: 좌표들
    :return: 두 점의 최단거리
    """
    n = len(coordinates)
    x_coordinates = [coordinate[0] for coordinate in coordinates]
    y_coordinates = [coordinate[1] for coordinate in coordinates]
    middle_point = (sum_of_list(x_coordinates) / n,
                    sum_of_list(y_coordinates) / n)
    # print(middle_point)  # test

    distances = [distance(middle_point, point) for point in coordinates]
    # print(distances)  # test
    distance_difference = list()

    for i in range(n - 1):
        coordinate_info = {
            'indices': (i, i + 1),
            'difference': math.fabs(distances[i] - distances[i + 1])
        }
        distance_difference.append(coordinate_info)
    # print(distance_difference)  # test

    indices = get_indices(distance_difference)
    return distance(coordinates[indices[0]], coordinates[indices[1]])


def get_indices(distance_information):
    distance_information.sort(key=lambda x: x['difference'])
    return distance_information[0]['indices']


def sum_of_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        mid = len(num_list) // 2
        return sum_of_list(num_list[:mid]) + sum_of_list(num_list[mid:])


def distance(point1, point2):
    """
    두 점의 거리를 구해주는 함수
    :param point1: 점 1 좌표
    :param point2: 점 2 좌표
    :return: 두 점의 거리
    """
    return ((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2)


if __name__ == '__main__':
    n = int(input())
    coordinates = list()
    for _ in range(n):
        coordinate = input().split(' ')
        coordinate = (int(coordinate[0]), int(coordinate[1]))
        coordinates.append(coordinate)
    # print(coordinates)
    print(solve(coordinates))
