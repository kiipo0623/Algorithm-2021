import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [] # 우선 board를 통채로 넣는걸로 하고 만약에 시간초과 나면 그때 비트마스크로 수정
maxblock = 0
# 0 상 1 하 2 좌 3 우
def move(board, direction):
    global N
    if direction == 0 or direction == 1: # 가로 세로 변환 (계산 쉽게 하기 위해)
        board = list(map(list, zip(*board)))

    for b in board: # 행 단위로 0을 없
        while 0 in b:
            b.remove(0)

        if direction == 1 or direction == 3: # 반대방향으로 가는 경우 reverse
            b.reverse()

        for i in range(len(b)-1):
            if b[i] == b[i+1]:
                b[i] *= 2
                b[i+1] = 0

        while 0 in b:
            b.remove(0)

        b += [0]*(N-len(b))

        if direction == 1 or direction == 3: # 반대방향으로 가는 경우 원상복귀
            b.reverse()

    if direction == 0 or direction == 1: # 원상복귀
        board = list(map(list, zip(*board)))
    return board


def dfs(depth, board):
    global visit, maxblock
    if depth >= 5:
        for n in board:
            maxblock = max(maxblock, max(n))
        return

    for i in range(4):
        newboard = move(deepcopy(board), i)
        dfs(depth+1, newboard)


dfs(0, board)
print(maxblock)