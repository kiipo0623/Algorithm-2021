import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

print(graph)

def dfs(graph, v, visited):
    stack = [v]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for n in reversed(graph[node]):
                stack.append(n)
    return visited

def dfs_rec(graph, v, visited):
    if v not in visited:
        visited.append(v)
        for node in graph[v]:
            dfs_rec(graph, node, visited)
    return visited

def bfs(graph, v, visited):
    queue = deque([v])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                queue.append(n)
    return visited

dfs_visited, bfs_visited = [], []
dfs(graph, v, dfs_visited)
# dfs_rec(graph, v, dfs_visited)
bfs(graph, v, bfs_visited)

for item in dfs_visited:
    print(item, end=' ')
print()
for item in bfs_visited:
    print(item, end=' ')
