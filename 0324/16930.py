import sys
sys.setrecursionlimit(100000000)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상 하 좌 우
def check(x, y, n, m):
    global world
    if 0<=x<n and 0<=y<m and world[x][y] != '#':
        return True
    return False

# direction : int
def dfs(start_x, start_y, end_x, end_y, visited, direction):
    global N, M
    if start_x == end_x and start_y == end_y: # 도달한 경우 : 종료 조건
        visited.append((start_x, start_y))
        return direction

    if (start_x, start_y) not in visited:
        visited.append((start_x, start_y))
        for i in range(4):
            nx, ny = start_x + dx[i], start_y+dy[i]
            if check(nx, ny, N, M):
                direction.append(i)
                dfs(nx, ny, end_x, end_y, visited, direction)


input = sys.stdin.readline

N, M, K = map(int, input().split())
world = []
for _ in range(N):
    world.append(list(input().rstrip()))
x1, y1, x2, y2 = map(int, input().split())
move = dfs(x1-1, y1-1, x2-1, y2-1, [], [])
print(move)





