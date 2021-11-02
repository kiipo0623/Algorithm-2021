# 뉴스 클러스터링
# 2:59 -
from collections import defaultdict
import math
def cutstr(str):
    strdict = defaultdict(int)
    for i in range(len(str)-1):
        temp_a = str[i]
        temp_b = str[i+1]

        if not temp_a.isalpha() or not temp_b.isalpha(): #알파벳 아니면
            continue
        else:
            if temp_a.islower():
                temp_a = temp_a.upper()
            if temp_b.islower():
                temp_b = temp_b.upper()
        temp = temp_a+temp_b
        strdict[temp] += 1
    return strdict


def solution(str1, str2):
    dictstr1 = cutstr(str1)
    dictstr2 = cutstr(str2)

    if len(dictstr1) + len(dictstr2) == 0:
        return 1 * 65536

    intersec = set(dictstr1).intersection(set(dictstr2))
    print(intersec)

    intercount = 0
    unioncount = 0

    for i in intersec:
        intercount += min(dictstr1[i], dictstr2[i])
        unioncount += max(dictstr1[i], dictstr2[i])

    for s1 in dictstr1:
        if s1 in intersec:
            continue
        else:
            unioncount += dictstr1[s1]

    for s2 in dictstr2:
        if s2 in intersec:
            continue
        else:
            unioncount += dictstr2[s2]

    return math.floor((intercount/unioncount)*65536)

print(solution("FRANCE", "french"))