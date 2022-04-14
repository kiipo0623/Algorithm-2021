from collections import defaultdict
from math import trunc
def solution(str1, str2):
    answer = 0
    dic1, dic2 = defaultdict(int), defaultdict(int)
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            dic1[str1[i:i+2].lower()] += 1

    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            dic2[str2[i:i+2].lower()] += 1

    if len(dic1) == len(dic2) == 0:
        return 65536

    set1 = set(dic1.keys())
    set2 = set(dic2.keys())

    setunion = set1.union(set2)
    setintersect = set1.intersection(set2)
    print("setunion", setunion)
    print("setintersect", setintersect)

    mom, son = 0, 0

    for u in setunion:
        mom += max(dic1[u], dic2[u])
    for i in setintersect:
        son += min(dic1[i], dic2[i])
    print("mom", mom, "son", son)
    answer = son/mom

    return trunc(answer * 65536)

print(solution("FRANCH", "french"))
print(solution("aa1+aa2", "AAAA12"))