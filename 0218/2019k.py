def solution(N, stages):
    answer = []
    stages.sort()
    failpoint = []

    for i in range(1, N+1): # 단계
        for j in range(len(stages)): # 인덱스
            if stages[j] >= i:
                mom = len(stages) - j
                break
        son = stages.count(i)
        failpoint.append((son / mom, i))

    failpoint.sort(key=lambda x: (-x[0], x[1]))
    print(failpoint)
    return answer

print(solution(
    5, [2, 1, 2, 6, 2, 4, 3, 3]
))