import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    row-=1
    col-=1
    board[row][col] = 2

L = int(input())
movesnake = deque([])
for _ in range(L):
    sec, dir = input().split()
    sec = int(sec)
    if dir == 'L': dir = -1
    else: dir = 1
    movesnake.append([sec, dir])

board[0][0] = 1
time = 0
direction = 0
head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
# 오른쪽 아래쪽 왼쪽 위쪽
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

changetaildir = deque([])
taildirection = direction
appleFlag = False
while True:
    time += 1

    n_head_x, n_head_y = head_x+dx[direction%4], head_y+dy[direction%4]
    if n_head_x<0 or n_head_x>=N or n_head_y<0 or n_head_y>=N or board[n_head_x][n_head_y] == 1:
        break

    if board[n_head_x][n_head_y] == 0: # 사과 없으면
        board[tail_x][tail_y] = 0 # 문제 발생 예상 지점
    else:
        appleFlag = True

    board[n_head_x][n_head_y] = 1
    head_x, head_y = n_head_x, n_head_y

    # 시간에 따라 방향 전환 : head
    if movesnake and time == movesnake[0][0]:
        direction += movesnake[0][1]
        changetaildir.append([head_x, head_y, direction%4])
        movesnake.popleft()

    # 시간에 따라 방향 전환 : tail
    if changetaildir and changetaildir[0][0] == tail_x and changetaildir[0][1] == tail_y: # 방향 전환 시
        taildirection = changetaildir[0][2]
        changetaildir.popleft()
    # 이 타이밍에서 방향을 변경해도 되는가
    # 사과 먹으면 안움직이는데 ..
    if appleFlag == False:
        tail_x, tail_y = tail_x + dx[taildirection%4], tail_y + dy[taildirection%4]
    else:
        appleFlag = False

print(time)