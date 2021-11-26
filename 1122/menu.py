from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        candidate = defaultdict(int)

        for order in orders:
            order = sorted(list(order))
            if len(order) >= c:
                combi = list(combinations(order, c))
                for com in combi:
                    print(com)
                    candidate[com] += 1

        # value값이 max인 key값 찾기
        if len(candidate.items()) != 0:
            max_count = max(candidate.values())
            key_max = []
            if max_count < 2:
                continue
            for c in candidate:
                if candidate[c] == max_count:
                    answer.append(''.join(c))

    return sorted(answer)