# 네트워크

def solution(n, computers):
    cpu = [i for i in range(n)]
    # 가장 Root인 cpu 번호를 두도록
    visited = [False] * n
    # visited = [False] * n

    # false가 하나라도 있으면 반복문 계속됨
    # not all(visited)

    stack = [0]

    while not all(visited): # 이 부분이 틀림
        item = stack.pop()
        visited[item] = True

        for i in range(n):
            if computers[item][i] == 1:
                cpu[i] = cpu[item]
                if visited[i] == False:
                    stack.append(i)

        if len(stack) == 0:
            for i in range(len(visited)):
                if visited[i] == False:
                    stack.append(i)
                    break

    return len(set(cpu))

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))