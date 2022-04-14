def block(m, n, temp):
    remove = set()

    for i in range(m-1):
        for j in range(n-1):
            if temp[i][j] != 0:
                if temp[i][j] == temp[i+1][j] and temp[i][j] == temp[i][j+1] and temp[i][j] == temp[i+1][j+1]:
                    remove.add((i, j))
                    remove.add((i+1, j))
                    remove.add((i, j+1))
                    remove.add((i+1, j+1))

    if len(remove) == 0:
        return (False, temp)

    for r in list(remove):
        x, y = r
        temp[x][y] = 0

    for i in range(m-1):
        for j in range(0, n-1):
            if temp[i][j] == 0:
                temp[i][j] = temp[i-1][j]
                temp[i-1][j] = 0

    print("*")
    print(temp)

    return (True, temp)

def solution(m, n, board):
    answer = 0
    temp = []
    check = True

    for x in board:
        temp.append(list(x))

    while check == True:
        check, temp = block(m, n, temp)

    for tm in temp:
        answer += tm.count(0)

    return answer

print(solution(
    4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
))