from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
stu = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    stu[a].append(b)
    indegree[b] += 1


def topology():
    result = []
    queue = deque([])
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for next in stu[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)
    return result

res = topology()
print(' '.join(map(str, res)))
