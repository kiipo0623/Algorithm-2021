def solution(board):
    n = len(board)
    newboard = [[-1 for _ in range(n)] for _ in range(n)]
    move = [(1, 0), (0, 1)]
    newboard[0][0] = board[0][0]
    for i in range(n):
        for j in range(n):
            for k in range(2):
                movex = i + move[k][0]
                movey = j + move[k][1]
                if movex >= n or movey >= n:
                    continue

                if board[movex][movey] == 0 and newboard[i][j] < 0:
                    change = -newboard[i][j]
                else:
                    change = newboard[i][j] + board[movex][movey]


                if newboard[movex][movey] == -1:
                    newboard[movex][movey] = change
                else:
                    newboard[movex][movey] = max(newboard[movex][movey], change)

    print(newboard)
    return newboard[-1][-1]

print(solution([[-10, 20, 30],[-10, 0, 10],[-20, 40, 1]]))