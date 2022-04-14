def check(place, i, j):
    type1 = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    type2 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    type3 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for t2 in type2:
        row = i + t2[0]
        col = j + t2[1]
        if 0 <= row < 5 and 0 <= col < 5 and place[row][col] == 'P':
            return False

    for t1 in type1:
        row = i + t1[0]
        col = j + t1[1]
        if 0 <= row < 5 and 0 <= col < 5 and place[row][col] == 'P':
            if row == i: # 행이 같은 경우 : 위아래에 사람이 있는 경우
                col -= int(t1[1]/2)
                print(t1[1]/2)
                if place[row][col] != 'X':
                    return False
            if col == j:
                row -= int(t1[0]/2)
                print(t1[0]/2)
                if place[row][col] != 'X':
                    return False

    for t3 in type3:
        row = i + t3[0]
        col = j + t3[1]
        if 0 <= row < 5 and 0 <= col < 5 and place[row][col] == 'P':
            checker1 = [i, col]
            checker2 = [row, j]
            if place[checker1[0]][checker1[1]] != 'X' or place[checker2[0]][checker2[1]] != 'X':
                return False
    return True


def solution(places):
    answer = []
    for place in places:
        flag = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not check(place, i, j):
                        flag = True
                        break
            if flag == True: break
        if flag == True: answer.append(0)
        else: answer.append(1)
    return answer

print(solution(
[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
))