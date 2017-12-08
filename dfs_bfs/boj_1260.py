class Graph:
    """
    Class Graph : Graph data structure implemented by python
    """

    def __init__(self, num_vertex, num_edge):
        self.graph = dict()
        self.num_vertex = num_vertex
        self.num_edge = num_edge

    def add_vertex(self):
        """
        Adds vertices of graph
        :return: void
        """
        for i in range(self.num_vertex):
            self.graph[i + 1] = list()

    def add_edge(self, vertex1, vertex2):
        """
        Adds edges of graph with vertex1 and vertex2 as end vertices.
        :param vertex1: One end vertex
        :param vertex2: Another end vertex
        :return: True if succeeds, False if fails
        """
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
        if vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)

    def print_graph(self):
        """
        Prints graph
        """
        print(self.graph)

    def __recursive_dfs(self, next_vertex, visited):
        """
        Recursively depth-first searches the graph
        :param next_vertex: next vertex number to visit
        :param visited: whether each vertex has been visited
        :return: none
        """
        visited[next_vertex - 1] = True
        print(next_vertex, end=' ')
        for v in self.graph[next_vertex]:
            if visited[v - 1] is False:
                self.__recursive_dfs(v, visited)

    def dfs(self, start_vertex):
        """
        Sets up recursive dfs
        :param start_vertex: Vertex to start depth-first search
        :return: none
        """
        for vertex in self.graph:
            self.graph[vertex].sort()
        visited = [False] * self.num_vertex
        self.__recursive_dfs(start_vertex, visited)

    def bfs(self, start_vertex):
        """
        Prints result of BFS of graph
        """
        for vertex in self.graph:
            self.graph[vertex].sort()
        visited = [False] * self.num_vertex

        queue = list()
        queue.append(start_vertex)
        while len(queue) is not 0:
            previous_visit = queue[0]
            print(previous_visit, end=' ')
            del queue[0]
            visited[previous_visit - 1] = True
            queue += [v for v in self.graph[previous_visit]
                      if v not in queue and visited[v - 1] is False]


if __name__ == '__main__':
    N, M, V = input().split(" ")
    N = int(N)
    M = int(M)
    V = int(V)

    g = Graph(N, M)
    g.add_vertex()

    for i in range(M):
        v1, v2 = input().split(" ")
        g.add_edge(int(v1), int(v2))

    g.dfs(V)
    print()
    g.bfs(V)
    print()
