def popfunc(board):
    counter = 0
    row, col = len(board), len(board[0])

    tmp = [i[:] for i in board]
    # 이번 턴에 변경 : 0   이전에 이미 변경 : -1
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == -1:
                continue
            if board[i][j] == board[i - 1][j] == board[i][j - 1] == board[i - 1][j - 1]:
                tmp[i][j], tmp[i - 1][j], tmp[i][j - 1], tmp[i - 1][j - 1] = 0, 0, 0, 0

    for idx, blockrow in enumerate(tmp):
        popblock = blockrow.count(0)
        counter += popblock
        new = [-1] * popblock + [i for i in blockrow if i != 0]
        board[idx] = new
    board = [i[:] for i in tmp]
    return counter


def solution(m, n, board):
    answer = 0

    b = list(map(list, zip(*board)))

    while True:
        popcnt = popfunc(b)
        if popcnt == 0: break
        answer += popcnt
    return answer

print(solution(
    4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
))
