from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
board = [list(stdin.readline().strip()) for _ in range(n)]
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

visit[rx][ry][bx][by] = True

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def move(x, y, dx, dy):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def dfs():
    queue = deque([])
    queue.append([rx, ry, bx, by, 1])

    while queue:
        arx, ary, abx, aby, count = queue.popleft()

        if count > 10:
            print(-1)
            return

        for i in range(4):
            nrx, nry, rcnt = move(arx, ary, dx[i], dy[i])
            nbx, nby, bcnt = move(abx, aby, dx[i], dy[i])

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                print(count)
                return

            if nrx == nbx and nry == nby:
                if rcnt > bcnt: # red가 더 많이 이동 = 양보
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if visit[nrx][nry][nbx][nby] == False:
                visit[nrx][nry][nbx][nby] = True
                queue.append([nrx, nry, nbx, nby, count + 1])
    
    print(-1)

dfs()
