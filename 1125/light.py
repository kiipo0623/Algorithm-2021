def solution(grid):
    global visited, dx, dy, col, row
    answer = []
    col = len(grid)
    row = len(grid[0])
    # 상 우 하 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[[False] * len(dx) for _ in range(row)] for _ in range(col)]

    for x in range(col):
        for y in range(row):
            for d in range(4):
                if visited[x][y][d] != True:  # 방문하지 않은 곳이라면 dfs 수행
                    cycle = dfs(x, y, d, grid)
                    # dfs : 끝까지 계속 그 방향으로 가는 것.. visited였던 곳 만날 때까지
                    if cycle != 0:
                        answer.append(cycle)

    answer.sort()
    return answer


def dfs(sx, sy, sd, grid):
    # 이미 들어온 상태 첫 칸을 시작하는 중
    global visited, dx, dy
    x, y, d = sx, sy, sd
    visited[x][y][d] = True
    cnt = 0

    while True:
        x = (x + dx[d]) % col
        y = (y + dy[d]) % row
        cnt += 1

        if grid[x][y] == 'S':
            d = d
        elif grid[x][y] == 'L':
            d -= 1
            if d == -1:
                d = 3
        elif grid[x][y] == 'R':
            d += 1
            if d == 4:
                d = 0

        if visited[x][y][d] == True:
            if (x, y, d) == (sx, sy, sd):
                return cnt
            else:
                return 0
        visited[x][y][d] = True

print(solution(
["R","R"]
))