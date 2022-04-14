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

# dice 초기화
dice = {}
for i in range(1, 7):
    dice[i] = 0

# dice_move 초기화
dice_move = {}
# 0 우 좌 상 하
# dice_move[1] = [0, 3, 4, 5, 2]
# dice_move[2] = [0, 3, 4, 1, 6]
# dice_move[3] = [0, 6, 1, 5, 2]
# dice_move[4] = [0, 1, 6, 5, 2]
# dice_move[5] = [0, 3, 4, 6, 1]
# dice_move[6] = [0, 3, 4, 2, 5]

dice_move[1] = [0, 4, 3, 5, 2]
dice_move[2] = [0, 4, 3, 1, 6]
dice_move[3] = [0, 1, 6, 5, 2]
dice_move[4] = [0, 6, 1, 5, 2]
dice_move[5] = [0, 4, 3, 6, 1]
dice_move[6] = [0, 4, 3, 2, 5]
D = 1 # 주사위 현재 초기화

for c in command:
    nrow = X + drow[c]
    ncol = Y + dcol[c]
    if nrow<0 or nrow >=ROW or ncol<0 or ncol>=COL: # 범위 벗어나는 경우
        continue
    X, Y = nrow, ncol
    #위
    D = dice_move[D][c]
    answer.append(dice[D])
    #아래
    if map_[X][Y] == 0:
        map_[X][Y] = dice[7-D]
    else:
        dice[7-D] = map_[X][Y]
        map_[X][Y] = 0
print(answer)