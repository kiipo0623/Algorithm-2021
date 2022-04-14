from itertools import combinations_with_replacement

def solution(n, info):
    apeach = []
    for idx, pnt in enumerate(info):
        if pnt != 0:
            while pnt > 0:
                apeach.append(10 - idx)
                pnt -= 1

    point = [i for i in range(0, 11)]
    combi = list(combinations_with_replacement(point, n))

    win = False
    maxpoint = 0

    for ryan in combi:
        ryanpoint, apeachpoint = 0, 0
        ryan = list(ryan)
        print(ryan, apeach)

        for i in range(0, 11):
            if ryan.count(i) > apeach.count(i):
                ryanpoint += i
            elif apeach.count(i):
                apeachpoint += i

        print(ryanpoint - apeachpoint)
        if ryanpoint > apeachpoint:
            win = True
            if (ryanpoint - apeachpoint) > maxpoint:
                maxpoint = ryanpoint - apeachpoint
                archive = ryan

    if not win:
        return [-1]
    else:
        templist = [0] * 11
        for a in archive:
            templist[10 - a] += 1
        return templist

print(solution(
    5, [2,1,1,1,0,0,0,0,0,0,0]
))