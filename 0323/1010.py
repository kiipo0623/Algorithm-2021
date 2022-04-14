import sys
input = sys.stdin.readline

def makeboard(row, col):
    board = [[0]*(col+1) for _ in range(row+1)]
    print(board)
    for i in range(1, row+1): # 서쪽 n개
        for j in range(1, col+1): # 동쪽 m개
            if i>j:
                continue
            elif i==j:
                board[i][j] = 1
            else: # i > j
                if i == 1:
                    board[i][j] = j
                else:
                    board[i][j] = board[i-1][j-1] + board[i][j-1]
    print(board)
    return board

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    board = makeboard(N, M)
    print(board[N][M])