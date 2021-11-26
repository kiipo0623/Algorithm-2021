# 백준 구슬탈출 2
# 삼성
# 7:18 -
# 오답 이유 : 한 번에 한 칸만 : 동시에 있을 수는 없다는 조건 구현 안함
# 즉 예제를 완전히 다 시뮬레이션 안해보고 대충해봐서 틀린
# 이 부분 구현하려면 그 방향 쪽에서 더 앞에있는 구슬을 찾고(그 방향 한정 한 라인에 있다면) 그것부터 시행
# 자꾸 일부만 맞추는 이유 : 특정 부분을 구현하지 않음(빼먹는 부분이 있음)
# 이 문제에서 킥 : 미리 어떤 조건을 줘서 케이스를 나눠서 두 구슬이 한 곳에 있게 되면 누구를 땡기는게 아니라 더 많이 이동한 쪽을 한칸 빠꾸시키면 된
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    temp = []
    string = sys.stdin.readline().strip()
    for j in range(m):
        if string[j] == 'R':
            redplace = [i,j]
        elif string[j] == 'B':
            blueplace = [i, j]
        elif string[j] == 'O':
            holeplace = [i, j]
        temp.append(string[j])
    arr.append(temp)

#U D L R
move_y = [-1, 1, 0, 0]
move_x = [0, 0, -1, 1]

def check(node, dir):
    y, x = node
    # dir에 맞춰서 for문으로 U/L는 0이 될때까지 D/R는 n/m이 될때까지 확인해서 .이 있는 마지막 위치를 반환
    count = 0
    if dir == 0:
        for k in range(y-1, -1, -1):
            if arr[k][x] == 'O':
                return 100
            elif arr[k][x] == '#':
                return count
            else:
                count += 1
    if dir == 1:
        for k in range(y+1, n, 1):
            if arr[k][x] == 'O':
                return 100
            elif arr[k][x] == '#':
                return count
            else:
                count += 1
    if dir == 2:
        for k in range(x-1, -1, -1):
            if arr[y][k] == 'O':
                return 100
            elif arr[y][k] == '#':
                return count
            else:
                count += 1
    if dir == 3:
        for k in range(x+1, m, 1):
            if arr[y][k] == 'O':
                return 100
            if arr[y][k] == '#':
                return count
            else:
                count += 1

# 최단 거리를 찾아야 하니까 .. bfs로 이동 ?
def bfs(red, blue): # 시작 좌표 (Red와 Blue의)
    visited = []
    queue = deque([])
    queue.append([red, blue, 1])

    while queue:
        rednode, bluenode, depth = queue.popleft()

        if depth >= 11:
            return -1

        if [rednode, bluenode] not in visited:
            visited.append([rednode, bluenode])
            flag = False

            for i in range(4):
                # 여기서 만약에 안막혀있으면 쭉 이동해야 : 새로운 함수에서 movecount 몇 칸 움직일지 체크
                redmove = check(rednode, i)
                bluemove = check(bluenode, i)

                if bluemove == 100:
                    continue
                elif redmove == 100:
                    return depth
                else:
                    new_red_y = rednode[0] + redmove * move_y[i]
                    new_red_x = rednode[1] + redmove * move_x[i]
                    new_blue_y = bluenode[0] + bluemove * move_y[i]
                    new_blue_x = bluenode[1] + bluemove * move_x[i]

                    if new_red_y == new_blue_y and new_red_x == new_blue_x:
                        if redmove > bluemove: # 더 작은 값은 한 칸 덜 움직여야 한다
                            new_red_y -= move_y[i]
                            new_red_x -= move_x[i]
                        elif redmove < bluemove:
                            new_blue_y -= move_y[i]
                            new_blue_x -= move_x[i]
                    queue.append([[new_red_y, new_red_x],[new_blue_y,new_blue_x], depth+1])

    return -1

print(bfs(redplace, blueplace))

