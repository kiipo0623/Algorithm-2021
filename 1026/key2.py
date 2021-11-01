def rotate90(key):
    n = len(key)
    newkey = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            newkey[j][n-i-1] = key[i][j]

    return newkey

def check(startX, startY, key, lock, extendSize, start, end):
    extendlock = [[0 for _ in range(extendSize)] for _ in range(extendSize)]

    for i in range(len(key)):
        for j in range(len(key)):
            extendlock[i+startX][j+startY] += key[i][j]

    for i in range(start, end):
        for j in range(start, end):
            extendlock[i][j] += lock[i-start][j-start]
            if extendlock[i][j] != 1:
                return False

    return True

def solution(key, lock):
    start = len(key)-1
    end = start + len(lock)

    extendSize = (len(key)-1)*2+len(lock)

    for k in range(4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, extendSize, start, end):
                    return True
        key = rotate90(key)

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))