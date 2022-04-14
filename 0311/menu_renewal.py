from itertools import combinations
def solution(orders, course):
    answer = []
    cuisine = []

    for order in orders: # 요리 종류 리스트에 등록
        for o in list(order):
            if o not in cuisine:
                cuisine.append(o)

    for c in course: # 음식 수
        combination = list(combinations(cuisine, c))
        frequency = {}

        for combi in combination: # 음식 조합
            counter = 0
            combi = set(combi)

            for order in orders: # 내역에 포함되어 있는지 확인
                if combi.issubset(set(order)):
                    counter += 1

            frequency[''.join(sorted(list(combi)))] = counter

        maxfreq = max(frequency.values())

        if maxfreq < 2:
            continue

        for item in frequency:
            if frequency[item] == maxfreq:
                answer.append(item)

    return sorted(answer)

print(solution(
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
))