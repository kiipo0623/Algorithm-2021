import sys
sys.setrecursionlimit(10000)

def dfs(start):
    visited[start] = True
    next = tcase[start]
    if not visited[next]:
        dfs(next)

for _ in range(int(input())):
    N = int(input())
    answer = 0
    tcase = list(map(int, sys.stdin.readline().split()))
    tcase = [0] + tcase
    visited = [True] + [False]*N

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            answer += 1
    print(answer)