class Danzi:
    def __init__(self, dimension):
        self.dimension = dimension
        self.map = []
        self.visited = [False] * (self.dimension ** 2)
        self.visit_count = 0

    def __str__(self):
        map_representation = ''
        i = 0
        while i < self.dimension ** 2:
            map_representation += (str(self.map[i:i + self.dimension]) + '\n')
            i += self.dimension
        explanation = 'Dimension = {}\nMap:\n{}\nvisited = {}\n'.format(
            self.dimension, map_representation, self.visited)
        return explanation

    def add_row(self, row):
        """
        Adds row to map
        :param row: row to add
        :return: void
        """
        self.map += row

    def is_already_visited(self, point):
        """
        Checks whether point is already visited
        :param point: point to check
        :return: Boolean - True if visited, False if not
        """
        return self.visited[point]

    def is_out_of_range(self, point, horizontal=False, row_num=-1):
        """
        Checks for out-of-range-exception : Used to check adjacent(left, right, up, down) points
        :param point: Point to check
        :param horizontal: Whether move is horizontal
        :param row_num: number of row
        :return: Boolean
        """
        if point < 0 or point >= self.dimension ** 2:
            return True
        elif horizontal is True and row_num != point // self.dimension:
            return True
        else:
            return False

    def search(self, start_point):
        """
        BFS
        :param start_point: start point to begin BFS
        :return: result of bfs - list. First element is number of houses, and second is maximum house number.
        """
        num_houses = 0
        max_visit_num = 0
        queue = [start_point]
        while len(queue) != 0:
            to_visit = queue[0]
            if self.map[to_visit] is '1':
                num_houses += 1
                # adding adjacent points
                self.add_adjacent_points(queue, current_point=to_visit)
            if queue[0] > max_visit_num:
                max_visit_num = queue[0]
            self.visited[queue[0]] = True
            del queue[0]
        return [num_houses, max_visit_num]

    def add_adjacent_points(self, queue, current_point):
        """
        으 핵똥코드;;
        adds adjacent points to visit queue
        :param queue: queue to enqueue
        :param current_point: current location of BFS
        :return: void
        """
        # Adjacent to right
        if self.is_out_of_range(current_point + 1, True, current_point // self.dimension) is False:
            if self.is_already_visited(current_point + 1) is False and current_point + 1 not in queue:
                queue.append(current_point + 1)
        # Adjacent to left
        if self.is_out_of_range(current_point - 1, True, current_point // self.dimension) is False:
            if self.is_already_visited(current_point - 1) is False and current_point - 1 not in queue:
                queue.append(current_point - 1)
        # Adjacent to upper
        if self.is_out_of_range(current_point + self.dimension) is False:
            if self.is_already_visited(current_point + self.dimension) is False:
                if current_point + self.dimension not in queue:
                    queue.append(current_point + self.dimension)
        # Adjacent to lower
        if self.is_out_of_range(current_point - self.dimension) is False:
            if self.is_already_visited(current_point - self.dimension) is False:
                if current_point - self.dimension not in queue:
                    queue.append(current_point - self.dimension)

    def enumerate(self):
        """
        Final enumeration function. Sets up BFS, and packs result
        :return: final, enumerated list. First element is total danzi amount, and next followings are numbers of houses
        """
        enumerated_result = list()
        point = 0
        while point != self.dimension ** 2:
            if self.visited[point] is False:
                if self.map[point] == '1':
                    search_result = self.search(point)
                    enumerated_result.append(search_result[0])
            point += 1
        enumerated_result.sort()
        return enumerated_result

    @staticmethod
    def print_result(result):
        """
        Prints final result
        :param result: Result to print
        :return: void
        """
        print(len(result))
        for element in result:
            print(element)


if __name__ == '__main__':
    n = int(input())
    test_case = Danzi(n)
    for i in range(n):
        next_row = input()
        test_case.add_row(list(next_row))

    test_result = test_case.enumerate()
    Danzi.print_result(test_result)
