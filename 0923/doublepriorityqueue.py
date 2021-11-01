import heapq
def solution(operations):
    pqueue = []
    heapq.heapify(pqueue)

    for operation in operations:
        if operation[0] == "I":
            num = int(operation[2:])
            heapq.heappush(pqueue, [num, True])
        elif operation == "D 1":
            i = -1
            while pqueue[i][1] == False:
                i -= 1
            pqueue[i][1] = False
        else: # D -1일떄 맨 앞에 가장 작은 수 삭제
            j = 0
            while pqueue[j][1] == False:
                j += 1
            pqueue[j][1] = False

    #두 개 만들엇다 치면 어떻게 합칠건지 ??

    maxnum = 0
    minnum = 0

    for i in range(len(pqueue)-1, -1, -1):
        if pqueue[i][1] == True:
            maxnum = pqueue[i][0]
            break

    for i in range(len(pqueue)):
        if pqueue[i][1] == True:
            minnum = pqueue[i][0]
            break

    return [maxnum, minnum]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))