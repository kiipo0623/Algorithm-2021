from collections import deque
def solution(priorities, location):
    answer = 0

    # flag 넣어서 몇번째인지 카운트
    # 그냥 규칙대로 진행

    sortpriority = sorted(priorities, reverse=True)

    queue = deque()

    for i in range(len(priorities)):
        if i == location:
            temp = [priorities[i], True]
        else:
            temp = [priorities[i], False]
        queue.append(temp)

    while True:
        if queue[0][1] == True and sortpriority[0] == queue[0][0]:
            answer += 1
            break
        if sortpriority[0] == queue[0][0]:
            answer += 1
            queue.popleft()
            sortpriority = sortpriority[1:]
        else:
            a = queue.popleft()
            queue.append(a)

    return answer

print(solution([1,1,9,1,8,1], 1))