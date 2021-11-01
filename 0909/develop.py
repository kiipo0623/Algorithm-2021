#기능 개발
def solution(progresses, speeds):
    count = []
    answer = []

    for i in range(len(progresses)):
        temp = (100-progresses[i])
        if temp % speeds[i] == 0:
            count.append(temp // speeds[i])
        else:
            count.append(temp // speeds[i] + 1)

    for i in range(1, len(count)):
        if count[i] < count[i-1]:
            count[i] = count[i-1]

    # 똑같은 값끼리 세면 되는데..
    temp = 1
    for i in range(0, len(count)-1):
        if count[i] == count[i+1]:
            temp += 1
        else:
            answer.append(temp)
            temp = 1

    answer.append(temp)

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))