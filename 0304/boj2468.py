from copy import deepcopy
def dfs(array, x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    stack = [(x, y)]
    array[x][y] = 0

    while stack:
        nowx, nowy = stack.pop()
        for i in range(4):
            posx = nowx + dx[i]
            posy = nowy + dy[i]

            if posx < 0 or posx >= n or posy < 0 or posy >= n:
                continue

            if array[posx][posy] != 0 and array[posx][posy] > k:
                array[posx][posy] = 0
                stack.append((posx, posy))

n = int(input())
arr = []
maximum = 0
for i in range(n):
    temp = list(map(int, input().split()))
    if max(temp) > maximum:
        maximum = max(temp)
    arr.append(temp)

safe = 1
for k in range(1, maximum):
    count = 0
    temparray = deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if temparray[i][j] != 0 and temparray[i][j] > k: # 이걸 확인하는 것만으로 safe place가 한자리는 획득하는
                dfs(temparray, i, j)
                count += 1
    if count > safe:
        safe = count
print(safe)