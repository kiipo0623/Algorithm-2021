# 입력
import sys
input = sys.stdin.readline
ROW, COL, X, Y, K = map(int, input().split())
map_ = []
for _ in range(ROW):
    map_.append(list(map(int, input().split())))
command = list(map(int, input().split()))
answer = []
# 우 좌 상 하
drow = [0, 0, 0, -1, 1]
dcol = [0, 1, -1, 0, 0]

# dice  상  북 동  서 남  하
dice = [0, 0, 0, 0, 0, 0]

def move(dir):
    if dir == 1: # 북 남 제외
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 2: # 북 남 제외
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 3: # 동 서 제외
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif dir == 4: # 동 서 제외
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

for c in command:
    dx = X + drow[c]
    dy = Y + dcol[c]
    if dx<0 or dx>=ROW or dy<0 or dy>=COL:
        continue
    X = dx
    Y = dy
    move(c)
    answer.append(dice[0])
    if map_[X][Y] == 0:
        map_[X][Y] = dice[5]
    else:
        dice[5] = map_[X][Y]
        map_[X][Y] = 0

for s in answer:
    print(s)