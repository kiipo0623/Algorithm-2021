from collections import defaultdict
def solution(id_list, k):
    answer = 0
    customer = defaultdict(int)
    for day in id_list:
        today = set(day.split())
        for t in today:
            customer[t] += 1
    for c in customer:
        if customer[c] >= k:
            answer += k
        else:
            answer += customer[c]
    return answer