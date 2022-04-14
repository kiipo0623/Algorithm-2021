def dfs(graph, v, visited):
    if v not in visited:
        visited.append(v)
        for node in graph[v]:
            dfs(graph, node, visited)
    return visited

from collections import deque
def bfs(graph, v, visited):
    queue = deque([v])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                queue.append(n)
    return visited

import sys
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

dfsvisited = []
bfsvisited = []
dfs(graph, v, dfsvisited)
bfs(graph, v, bfsvisited)

for d in dfsvisited:
    print(d, end=' ')
print()
for b in bfsvisited:
    print(b, end=' ')

