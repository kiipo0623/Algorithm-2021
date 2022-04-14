import sys
from collections import deque

def bfs():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque([(0, 0)])
    global graph

    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            pos_x = now_x + dx[i]
            pos_y = now_y + dy[i]

            if pos_x >= n or pos_x < 0 or pos_y >= m or pos_y < 0:
                continue
            if graph[pos_x][pos_y] == 0:
                continue
            if graph[pos_x][pos_y] == 1:
                graph[pos_x][pos_y] = graph[now_x][now_y] + 1
                queue.append((pos_x, pos_y))


n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

bfs()
print(graph[n-1][m-1])

