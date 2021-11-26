# 10:47
# bfs 사용해서 한칸씩 이동하면서 메모
from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    mymap = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if maps[i][j] == 0:
                mymap[i][j] = -1

    mymap[0][0] = 1
    mymap[row - 1][col - 1] = 0

    queue = deque([(0, 0)])

    drow = [1, -1, 0, 0]
    dcol = [0, 0, -1, 1]

    # bfs니까 queue에 넣어서 사방향 이동
    while queue:
        r, c = queue.popleft()

        now = mymap[r][c]
        for i in range(4):
            dr = r + drow[i]
            dc = c + dcol[i]

            if dr >= row or dc >= col or dr < 0 or dc < 0:
                continue

            if mymap[dr][dc] == 0: # 어차피 처음에 하는게 최단이라서 메모 업데이트 할 필요 없다
                queue.append((dr, dc))
                mymap[dr][dc] = now + 1

    if mymap[row - 1][col - 1] == 0:
        return -1
    else:
        return mymap[row - 1][col - 1]

print(solution(
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
))