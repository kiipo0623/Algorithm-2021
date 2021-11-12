def solution(rows, columns):
    answer = [[]]
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    r = 0 # 현재 행
    c = 0 # 현재 열
    now = 1
    zerocount = 0
    print(board)

    while True:
        # break조건
        if board[r][c] != 0 and board[r][c] % 2 == now % 2:
            break
        if zerocount == rows*columns:
            break

        if board[r][c] == 0:
            zerocount += 1

        board[r][c] = now
        now += 1

        if now % 2 == 0: # 짝수면 행이동
            c += 1
        else:
            r += 1

        if c == columns:
            c = 0
        if r == rows:
            r = 0


    return board

print(solution(3, 6))