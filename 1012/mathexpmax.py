# 수식 최대화 재도전
# 11:04 -

# 한 숫자로만 이루어져 있지 않은 경우 : 루틴을 수행해야 하는 경우
# queue 에 넣고 (전체 과정)
# stack에 일부씩 넣어서 ? 진행하는 방법이 하나 있고
# str자체로 수행하는 방법이 하나

from itertools import permutations
from collections import deque
from copy import deepcopy

def evaluation(op, exp):
    queue1 = deque()
    queue2 = deque()
    temp = ''
    for i in range(len(exp)):
        if exp[i] in op:
            queue1.append(temp)
            queue1.append(exp[i])
            temp = ''
        else:
            temp += exp[i]
    queue1.append(temp)
    print(queue1)

    for o in op:
        stack = []
        while queue1:
            now = queue1.popleft()
            if now == o:
                before = stack.pop()
                after = queue1.popleft()
                temp = before+now+after
                stack.append(str(eval(temp)))
            else:
                if stack:
                    queue2.append(stack.pop())

                if now in op:
                    queue2.append(now)
                else:
                    stack.append(now)

        if stack:
            queue2.append(stack.pop())

        queue1 = deepcopy(queue2)
        queue2.clear()

    return int(queue1[0])

def solution(expression):
    answer = 0
    ops = ["*", "+", "-"]
    operators = list(permutations(ops, 3))

    for op in operators:
        sol = abs(evaluation(op, expression))
        if sol > answer:
            answer = sol

    return answer

print(solution("100-200*300-500+20"))