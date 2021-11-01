import copy
def solution(n, info):
    answer = [0] * 11
    # backup deepcopy

    # 첫 판에 어떻게 할지 초기 모델
    arrow = n
    score = 0
    startpoint = 0
    while arrow:
        for i in range(0, 11):
            if arrow > info[i]:
                answer[i] = info[i] + 1
                arrow -= info[i] + 1
                score += 10 - i
                startpoint = i
            if arrow == 0:
                break
    print(answer)
    print(score)

    # 맨위에서 빼오기
    while True:
        arrow = max(answer)
        idx = answer.index(arrow)
        newscore = score - (10-idx)
        print("arrow", arrow)
        print("idx", idx)
        print("newscore", newscore)
        # startpoint 맨 앞 점수 못따는 구간
        print("start", startpoint)
        while arrow:
            for i in range(startpoint+1, 11):
                if arrow > info[i]:
                    answer[i] = info[i] + 1
                    arrow -= info[i] + 1
                    newscore += i
                if arrow == 0:
                    break

        if newscore >= score:
            score = newscore
            backup = copy.deepcopy(answer)
        else:
            break



    return answer



n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))