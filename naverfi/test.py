def snail(n):
    arr = [[0 for j in range(n)] for i in range(n)]
    row = 0
    col = -1
    cnt = 1
    trans = 1
    while n > 0:
        for i in range(n):
            col += trans
            arr[row][col] = cnt
            cnt += 1
        n -= 1
        for j in range(n):
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1
    return arr


def solution(n, jump):
    answer = []
    pan = []
    arr = snail(n)
    for i in range(0, n * n):
        temp = [i, False]
        pan.append(temp)

    # 0번째는 미리 세팅 해주고
    count = 0
    pan[0][1] = True
    ptr = 0
    truecount = 1

    while True:
        ptr += 1
        count += 1

        if ptr == n * n:
            ptr = 0

        if pan[ptr][1] == True:
            count -= 1

        if count == jump:
            pan[ptr][1] = True
            truecount += 1
            count = 0

        if truecount == n * n - 1:
            print("ptr", ptr)
            break

    for i, check in pan:
        if check == False:
            last = i
            print("last", last)
            break

    for i in range(n):
        for j in range(n):
            if arr[i][j] == last + 1:
                return [i + 1, j + 1]

print(solution(5, 3))