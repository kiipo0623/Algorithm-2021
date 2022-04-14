from itertools import permutations
from collections import deque
from copy import deepcopy

def solution(expression):
    answer = 0
    operand = ['+','-','*']
    oprlist = list(permutations(operand, 3))

    originalqueue = deque([])
    tmp = ''
    for e in expression:
        if e.isdigit():
            tmp += e
        else:
            originalqueue.append(tmp)
            originalqueue.append(e)
            tmp = ''
    originalqueue.append(tmp)

    for opr in oprlist:
        expqueue = deepcopy(originalqueue)
        for o in opr:
            newqueue = deque([])
            while expqueue:
                now = expqueue.popleft()
                if now != o:
                    newqueue.append(now)
                else:
                    beforenum = newqueue.pop()
                    afternum = expqueue.popleft()
                    newqueue.append(str(eval(beforenum+o+afternum)))
            expqueue = deepcopy(newqueue)
        res = abs(int(newqueue[0]))
        if answer < res:
            answer = res

    return answer

print(solution("100-200*300-500+20"	))