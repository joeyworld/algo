nodes, edges = map(int, input().split())

graph = {i + 1: [] for i in range(nodes)}
for _ in range(edges):
    dep, dest, val = map(int, input().split())
    graph[dep].append((dest, val))
    graph[dest].append((dep, val))

start, end = map(int, input().split())

dsts = []
q = []

for edge in graph[start]:
    nxt, dist = edge
    q.append((nxt, dist, [start]))

while q:
    curr_nxt, curr_dst, curr_went = q[0]
    del q[0]
    if curr_nxt == end:
        dsts.append(curr_dst)
        continue
    for edge in graph[curr_nxt]:
        nxt, dst = edge
        if nxt not in curr_went:
            q.append((nxt, curr_dst | dst, curr_went + [curr_nxt]))

print(min(dsts) if dsts else -1)
