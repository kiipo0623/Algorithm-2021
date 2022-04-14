dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def prim(start, counter, boundary):
    visited_set = set()
    visited_set.add(start)
    distance = 0

    for _ in range(counter-1):
        min_dist, next_node = 10000, -1

        for node in visited_set:
            for j in range(1, counter+1):
                if j not in visited_set and boundary[node][j] < min_dist:
                    min_dist = boundary[node][j]
                    next_node = j
        distance += min_dist
        visited_set.add(next_node)
    return distance

def dfs(x, y, checker, counter, height, land):
    n = len(checker)

    stack = [(x, y)]

    while stack:

        ax, ay = stack.pop()
        if checker[ax][ay] == 0: # 방문 안했으면
            checker[ax][ay] = counter

            for i in range(4):
                nx = ax + dx[i]
                ny = ay + dy[i]
                if 0<=nx<n and 0<=ny<n and abs(land[nx][ny]-land[ax][ay])<=height:
                    stack.append((nx,ny))
    return


def solution(land, height):
    answer = 0
    n = len(land)
    max = 10000
    checker = [[0]*(n) for _ in range(n)];

    # 색 칠하기
    counter = 1
    for i in range(0, n):
        for j in range(0, n):
            if checker[i][j] == 0:
                dfs(i, j, checker, counter, height, land)
                counter += 1

    # 국경 넘어가는 최소값 구하기
    counter -= 1
    boundary = [[max]*(counter+1) for _ in range(counter+1)]

    for i in range(0, n):
        for j in range(0, n):

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0<=nx<n and 0<=ny<n:
                    bf_color = checker[i][j]
                    at_color = checker[nx][ny]

                    if bf_color != at_color:
                        boundary[bf_color][at_color] = min(boundary[bf_color][at_color], abs(land[i][j] - land[nx][ny]))
                        boundary[at_color][bf_color] = boundary[bf_color][at_color]

    # MST로 최단 거리 구하기


    return prim(1, counter, boundary)

print(solution(
[[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3
))