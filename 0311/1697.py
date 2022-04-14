import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

def bfs(start, visited, end):
    queue = deque([start])
    visited[start] = -1
    while queue:
        now = queue.popleft()

        tmp = [now+1, now-1, now*2]
        for x in tmp:
            if x == end:
                visited[x] = now
                return

            if 0<=x<=100000:
                if not visited[x]:
                    queue.append(x)
                    visited[x] = now

visited = [False for _ in range(100000)]
counter = 0
bfs(n, visited,k)
print(visited)

while True:
    check = visited[k]
    if check == -1:
        break
    counter += 1
    k = check

print(counter)