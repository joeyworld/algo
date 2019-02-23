from fractions import Fraction


def make_graph(n, edges):
    graph = {i + 1: [] for i in range(n)}
    for edge in edges:
        dep, dest = edge
        graph[dep].append(dest)
        graph[dest].append(dep)
    return graph


def bfs(n, graph):
    q = []
    rel = []
    visited = [False] * n
    visited[0] = True
    for child in graph[1]:
        rel.append((1, child))
        q.append(child)
    while q:
        nxt = q[0]
        visited[nxt - 1] = True
        del q[0]
        for child in graph[nxt]:
            if not visited[child - 1]:
                rel.append((nxt, child))
                q.append(child)
    return rel


def solve(n, graph, g, k, guesses):
    # 최초 한 번 bfs로 parent-child 쌍 만들고 예측하기
    win_count = 0
    relationships = bfs(n, graph)
    guesses = sorted(guesses, key=lambda x: x[1])
    correct = sorted(
        list(set(relationships) & set(guesses)),
        key=lambda x: x[1]
    )
    wrong = sorted(list(set(guesses) - set(relationships)))
    n_correct = len(correct)
    n_wrong = g - n_correct
    if n_correct >= k:
        win_count += 1

    correct_idx = 0
    wrong_idx = 0
    dp_correct_to_wrong = [0] * (n + 1)
    dp_wrong_to_correct = [0] * (n + 1)

    for i in range(n - 1):
        rel = relationships[i]
        correct_to_wrong = 0
        wrong_to_correct = 0

        # 기존 예측이 틀려짐
        if correct_idx < n_correct and rel == correct[correct_idx]:
            correct_idx += 1
            correct_to_wrong += 1

        # 기존 틀린 예측이 맞아짐
        while wrong_idx < n_wrong and rel[1] == wrong[wrong_idx][0]:
            if rel[0] == wrong[wrong_idx][1]:
                wrong_idx += 1
                wrong_to_correct += 1
            else:
                wrong_idx += 1

        correct_to_wrong += dp_correct_to_wrong[rel[1] - 1]
        wrong_to_correct += dp_wrong_to_correct[rel[1] - 1]

        dp_correct_to_wrong[rel[1]] = correct_to_wrong
        dp_wrong_to_correct[rel[1]] = wrong_to_correct

        curr_correct = n_correct - correct_to_wrong + wrong_to_correct
        if curr_correct >= k:
            win_count += 1

    # 분수로 만들고 약분하기
    return str(Fraction(win_count, n))


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
        graph = make_graph(n, edges)
        g, k = map(int, input().split())
        guesses = [tuple(map(int, input().split())) for _ in range(g)]
        res = solve(n, graph, g, k, guesses)
        if res == '0' or res == '1':
            print('{}/1'.format(res))
        else:
            print(res)
