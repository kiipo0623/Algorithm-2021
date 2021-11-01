from collections import defaultdict
from itertools import combinations
def solution(clothes):
    answer = len(clothes)   #1개씩 하는 경우
    items = defaultdict(list)

    for cloth in clothes:
        items[cloth[1]].append(cloth[0])

    itemkind = len(items)

    if itemkind==1:
        return answer

    for i in range(2, itemkind+1):
        combi = list(combinations(items, i))
        for category in combi:
            temp = 1
            for i in range(len(category)):
                temp *= len(items[category[i]])
            answer += temp

    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))