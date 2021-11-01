def solution(research, n, k):
    answer = ''
    # dict에 정리
    dictionary = dict()

    j = 1
    for search in research:
        tempdict = dict()

        for i in range(len(search)): # 매일의 검색어 조사
            if search[i] not in tempdict:
                tempdict[search[i]] = 1
            else:
                tempdict[search[i]] += 1

        for alpha in tempdict:
            if alpha not in dictionary:
                dictionary[alpha] = {}
                dictionary[alpha][j] = tempdict[alpha]
            else:
                dictionary[alpha][j] = tempdict[alpha]
        j += 1

    # 매 검색어에 대해 조건 여부 확인

    hotresearch = dict()
    for alpha in dictionary:
        hotcount = 0
        for day in dictionary[alpha].keys():
            checkcontinuity = [i for i in range(day, day+n)]
            s1 = set(checkcontinuity)
            s2 = set(dictionary[alpha].keys())

            if s1 == s1.intersection(s2): # 연속 확인 완료
                condition1 = True
                condition2 = 0
                for today in checkcontinuity:
                    if dictionary[alpha][today] < k:
                        condition1 = False
                    else:
                        condition2 += dictionary[alpha][today]

                if condition1 and condition2 >= 2*n*k:
                    hotcount += 1

        hotresearch[alpha] = hotcount

    if not any(hotresearch.values()):
        return "None"
    else:
        final = sorted(hotresearch.items(), key = lambda x : (-x[1], x[0]))
        return final[0][0]

# 선착순 구현안
print(solution(["yxxy","xxyyy"], 2, 1))