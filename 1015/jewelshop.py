def solution(gems):
    answer = [0, len(gems)]

    kinds = len(set(gems))
    start, end = 0, 0
    jewel = dict()
    jewel[gems[0]] = 1

    while (start < len(gems)) and (end < len(gems)):
        if len(jewel) == kinds:  # 완성 된 경우
            if end - start < answer[1] - answer[0]: # 최단거리인 경우
                answer = [start, end]

            if jewel[gems[start]] == 1:
                del jewel[gems[start]]
            else:
                jewel[gems[start]] -= 1

            start += 1
        else:
            end += 1
            if end >= len(gems):
                break
            if gems[end] in jewel:
                jewel[gems[end]] += 1
            else:
                jewel[gems[end]] = 1

    answer[0] += 1
    answer[1] += 1
    return answer

print(solution(["AA", "AB", "AC", "AA", "AC"]))