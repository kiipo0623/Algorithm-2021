def rotation(arr):
    n = len(arr)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j]
    return ret

# startX startY expend에서 key의 머리 위치, start end expend에서 Lock의 위치
def check(startX, startY, key, lock, expendSize, start, end):
    expendList = [[0] * expendSize for _ in range(expendSize)]

    # expendList에 key 추가
    for i in range(len(key)): # 맨 첫번째 칸부터
        for j in range(len(key)):
            expendList[startX + i][startY + j] += key[i][j]

    # expendList에 lock 추가하면서 기존 값이랑 더하기
    for i in range(start, end):
        for j in range(start, end):
            expendList[i][j] += lock[i - start][j - start]
            if expendList[i][j] != 1:
                return False

    return True

def solution(key, lock):
    start = len(key) - 1 # expendedList에서 lock의 시작 지점
    end = start + len(lock) # expendedList에서 lock이 끝나는 지점
    expendSize = len(lock) + start * 2

    # lock은 고정이고 key 가 움직이는 거
    for a in range(0, 4):
        for i in range(end): # 0부터 lock이 끝나는 지점까지 key의 머리가 이동 [가로]
            for j in range(end): # [세로]
                if check(i, j, key, lock, expendSize, start, end): #i, j = key의 머리 위치 start, end = lock의 시점
                    return True
        key = rotation(key)

    return False