from collections import deque
def solution(n, times):
    immigration = []

    for time in times:
        temp = [time, time]
        immigration.append(temp)

    immigration.sort()

    immigration = deque(immigration)

    for i in range(n-1):
        mintime = immigration.popleft()
        which = binarysearch(immigration, mintime[0]+mintime[1])
        immigration.insert([mintime[0]+mintime[1], mintime[1]], which)

    return immigration[0][0]

def binarysearch(thelist, target):
    start = 0
    end = len(thelist) - 1
    while True:
        mid = (start + end) // 2
        if target < thelist[mid][0]:
            end = mid - 1
        elif target > thelist[mid][0]:
            start = mid + 1
        elif target == thelist[mid][0]:
            return mid
    return -1

print(solution(6, [7, 10]))