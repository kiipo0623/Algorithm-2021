def solution(board, moves):
    answer = 0
    length = len(board)
    stack = [0]

    for move in moves:
        move -= 1
        for i in range(0, length):
            if board[i][move] != 0:
                if board[i][move] == stack[-1]:
                    stack.pop()
                    answer += 1
                else:
                    stack.append(board[i][move])
                board[i][move] = 0
                break

    return answer

print(solution(
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
[1,5,3,5,1,2,1,4]
))