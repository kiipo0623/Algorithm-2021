import sys
n, m = map(int, sys.stdin.readline().split())
group = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    group[a].append(b)
    group[b].append(a)

def dfs(start, visited, group):
    stack = [start]
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = True
            stack.extend(group[now])
    return 1

visited = [False] * (n+1)
answer = 0
for i in range(1, n+1):
    if not visited[i]:
        answer += dfs(i, visited, group)

print(answer)