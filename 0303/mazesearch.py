dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

from collections import deque

def bfs(x, y):
    defx, defy = x-1, y-1
    posx, posy = 0, 0
    count = 0
    queue = deque([(posx, posy)])

    while queue:
        x, y = queue.popleft()

        if 0<=x<n and 0<=y<m and visited[x][y] == 0 and graph[x][y] == 1 :
            visited[x][y] = 1
            count += 1

            if x == defx and y == defy:
                return count

            for i in range(4):
                newx = x + dx[i]
                newy = y + dy[i]
                queue.append((newx, newy))


import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[0]*m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs(n, m))

