# 자물쇠와 열쇠
# 2:14 -

def turn(key):
    turned = []
    turned.append(key)

    temp90 = []
    temp180 = []
    temp270 = []

    for i in range(0, 3, 1):
        temp_row = []
        for j in range(2, -1, -1):
            temp_row.append(key[j][i])
        temp90.append(temp_row)

    for i in range(2, -1, -1):
        temp_row = []
        for j in range(2, -1, -1):
            temp_row.append(key[i][j])
        temp180.append(temp_row)

    for i in range(2, -1, -1):
        temp_row = []
        for j in range(0, 3, 1):
            temp_row.append(key[j][i])
        temp270.append(temp_row)

    turned.append(temp90)
    turned.append(temp180)
    turned.append(temp270)

    return turned

def solution(key, lock):
    length_lock = len(lock)
    length_key = len(key)
    answer = True
    keys = turn(key)
    sumarr = [[0 for i in range(length_lock)] for _ in range(length_lock)]

    # 삼중 for문은 대체로 안되는 경향이 있다
    for k in keys:
        for i in range(length_lock):
            for j in range(length_lock):
                if k[i][j] + lock[i][j] != 1:
                    flag = False
                    continue
            

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))