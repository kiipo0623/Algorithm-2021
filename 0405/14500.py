dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def dfs(s_x, s_y, depth, result):
    global answer, max_val, graph
    if result + (4-depth)*max_val <= answer:
        return

    if depth == 4:
        answer = max(answer, result)

    for i in range(4):
        n_x = s_x + dx[i]
        n_y = s_y + dy[i]
        if 0<=n_x<N and 0<=n_y<M and not visited[n_x][n_y]:
            if depth == 2:
                visited[n_x][n_y] = True
                dfs(s_x, s_y, depth+1, result + graph[n_x][n_y])
                visited[n_x][n_y] = False

            visited[n_x][n_y] = True
            dfs(n_x, n_y, depth+1, result + graph[n_x][n_y])
            visited[n_x][n_y] = False

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [[False]*M for _ in range(N)]

max_val = max(map(max, graph))

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False

print(answer)