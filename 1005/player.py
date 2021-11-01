from collections import deque
def solution(n, results):
    answer = 0
    player = dict()
    indegree = [0] * (n+1)

    for i in range(1, n+1):
        player[i] = []

    for r in results:
        player[r[0]].append(r[1])
        indegree[r[1]] += 1

    def topology_sort():
        global result
        result = []
        q = deque()

        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            now = q.popleft()
            result.append(now)

            for i in player[now]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    q.append(i)

    for i in result:
        if result


    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))