import sys
input = sys.stdin.readline

N = int(input())
candy = [list(input().rstrip()) for _ in range(N)]
answer = 1

def check():
    global candy
    maxcount = 0
    for row in range(N):
        cnt = 1
        for col in range(1, N):
            if candy[row][col] == candy[row][col-1]:
                cnt += 1
            else:
                cnt = 1
        if cnt > maxcount:
            maxcount = cnt

        cnt = 1
        for col in range(1, N):
            if candy[col][row] == candy[col-1][row]:
                cnt += 1
            else:
                cnt = 1
        if cnt > maxcount:
            maxcount = cnt
    return maxcount

for row in range(N):
    for col in range(N):
        if col < N-1:
            candy[row][col], candy[row][col+1] = candy[row][col+1], candy[row][col]
            answer = max(answer, check())
            candy[row][col], candy[row][col+1] = candy[row][col+1], candy[row][col]

        if row < N-1:
            candy[row][col], candy[row+1][col] = candy[row+1][col], candy[col][row]
            answer = max(answer, check())
            candy[row][col], candy[row+1][col] = candy[row+1][col], candy[col][row]

print(answer)