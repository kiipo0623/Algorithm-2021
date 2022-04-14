def solution(board, skill):
    counting = 0
    row, col = len(board), len(board[0])
    tempboard = [[0 for _ in range(col+1)] for _ in range(row+1)]

    for turntype, r1, c1, r2, c2, degree in skill:
        pm = 1
        if turntype == 1: pm = -1 # 적인 경우
        degree = degree * pm

        tempboard[r1][c1] = degree
        tempboard[r1][c2+1] = (-1)*degree

        tempboard[r2+1][c1] = (-1)*degree
        tempboard[r2+1][c2+1] = degree

    # 세로로 휩쓸기
    for i in range(row+1):
        now = 0
        for j in range(col+1): # 가로로 휩쓸기
            now += tempboard[i][j]
            tempboard[i][j] = now

    # 가로로 휩쓸기
    for i in range(col+1):
        now = 0
        for j in range(row+1):
            now += tempboard[j][i]
            tempboard[j][i] = now


    for i in range(row):
        for j in range(col):
            tempboard[i][j] += board[i][j]
            if tempboard[i][j] > 0:
                counting += 1

    print(tempboard)
    return counting


