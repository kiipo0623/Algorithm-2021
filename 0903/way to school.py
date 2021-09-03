from collections import deque

def solution(m, n, puddles):
    answer = 0
    way = [[1000000008 for i in range(m)] for j in range(n)]
    # 여기서는 리스트 조절 할 수가 없어서 index-1해줘야함

    for puddle in puddles:
        way[puddle[0]-1][puddle[1]-1] = -1

    queue = deque()

    if way[0][1] != -1:
        queue.append([0, 1])
        way[0][1] = 1

    if way[1][0] != -1:
        queue.append([1, 0])
        way[1][0] = 1

    while queue:
        temp = queue.popleft()
        if temp[0] + 1 <= n - 1 and temp[1] <= m - 1:
            if way[temp[0]+1][temp[1]] != -1:
                way[temp[0]+1][temp[1]] = min(way[temp[0]][temp[1]]+1, way[temp[0]+1][temp[1]])
                queue.append([temp[0]+1, temp[1]])

        if temp[0] <= n - 1 and temp[1] + 1 <= m - 1:
            if way[temp[0]][temp[1]+1] != -1:
                way[temp[0]][temp[1]+1] = min(way[temp[0]][temp[1]]+1, way[temp[0]][temp[1]+1])
                queue.append([temp[0],temp[1]+1])


    return (way[-1][-1]-1) /

# 등굣길

print(solution(4, 3, [[2,2]]))