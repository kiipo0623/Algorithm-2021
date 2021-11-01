# 3주차 챌린지
# 퍼즐 조각 채우기
# 1:53 -
# 씨발.. 포기 너무 많은 에러와 .. 감당하기 어려운 .. 것
from copy import deepcopy

def angle(pos):
    dgr0 = []
    dgr90 = []
    dgr180 = []
    dgr270 = []

    # [[1,1], [2,2]] 이런식으로 들어오고, 이걸 똑같이 복제해서 여러개 만들어줘야함
    # 뭔가 반복문을 한번 더 돌려줘야 함. . .
    for p in pos:
        x, y = p
        dgr0.append([x,y])
        dgr90.append([-y,x])
        dgr180.append([y, -x])
        dgr270.append([-x,-y])

    final = []
    final.append(dgr0)
    final.append(dgr90)
    final.append(dgr180)
    final.append(dgr270)

    return final

def find_table_dfs(table, row, col, final, visited):
    pos = []
    stack = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    pos.append([row, col])
    visited.append([row, col])
    stack.append([row, col])

    while stack:
        i, j = stack.pop()
        for k in range(4):
            temp_i = i+dy[k]
            temp_j = j+dx[k]
            if temp_i >= 0 and temp_i < len(table) and temp_j >= 0 and temp_j < len(table):
                if table[temp_i][temp_j] == 1 and [temp_i,temp_j] not in visited:
                    pos.append([temp_i, temp_j])
                    stack.append([temp_i, temp_j])
                    visited.append([temp_i, temp_j])

    for item in pos:
        table[item[0]][item[1]] = 0
        item[0] -= row
        item[1] -= col

    final.append(pos)
    return visited, final

def find_table(table):
    final = []
    visited = []

    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1:
                row = i
                col = j
                visited, final = find_table_dfs(table, row, col, final, visited)

    return final

def find_board_dfs(board, row, col, final, visited, original):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    pos = []
    stack = []

    pos.append([row, col])
    visited.append([row, col])
    stack.append([row, col])

    while stack:
        i, j = stack.pop()
        for k in range(4):
            temp_i = i + dy[k]
            temp_j = j + dx[k]
            if temp_i >= 0 and temp_i < len(board) and temp_j >= 0 and temp_j < len(board):
                if board[temp_i][temp_j] == 0 and [temp_i, temp_j] not in visited:
                    pos.append([temp_i, temp_j])
                    stack.append([temp_i, temp_j])
                    visited.append([temp_i, temp_j])

    original.append(pos)

    for item in pos:
        item[0] -= row
        item[1] -= col

    final.append(pos)

    return visited, final, original

#  보드 첫칸부터 뒤지다가 퍼즐이랑 똑같은 거 있으면 그만두는 역할
def find_board(board, puzzle):
    final = []
    visited = []
    original = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                row = i
                col = j
                visited, final, original = find_board_dfs(board, row, col, final, visited, original)

    for i in range(len(final)):
        if puzzle == final[i]:
            for item in original[i]:
                board[item[0]][item[1]] = 1
                print("return:", len(final[i]))
                return len(final[i])

    return 0

# 언제 새로 카운트를 시작하고
# 어느 시점을 끝난 시점으로 인식할지

def count_time(board):
    temp_board = deepcopy(board)
    count = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if temp_board[i][j] == 0:
                count += dfs(i, j, temp_board)

    return count


def dfs(row, col, t_board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    t_stack = []

    t_stack.append([row, col])

    while t_stack:
        i, j = t_stack.pop()
        for k in range(4):
            temp_i = i + dy[k]
            temp_j = j + dx[k]
            if temp_i >= 0 and temp_i < len(t_board) and temp_j >= 0 and temp_j < len(t_board):
                if t_board[temp_i][temp_j] == 0:
                    t_stack.append([temp_i, temp_j])
                    t_board[temp_i][temp_j] = 1

    return 1



def solution(game_board, table):
    answer = 0
    times = count_time(game_board)
    puzzles = find_table(table)

    for i in range(times):
        for p in puzzles:
            rotate = angle(p)
            answer += find_board(game_board, rotate[0])
            answer += find_board(game_board, rotate[1])
            answer += find_board(game_board, rotate[2])
            answer += find_board(game_board, rotate[3])

    return answer


print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))