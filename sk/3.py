from collections import deque
from itertools import permutations

def dfs(start, graph):


def solution(n, edges):
    answer = 0
    nodes = [[] for _ in range(n)]
    for a, b in edges:
        nodes[a].append(b)
        nodes[b].append(a)

    for i in range(n):
        counter = [0] * n
        res = dfs(i, nodes)
        print(res)


    return answer

print(solution(
    5, [[0,1],[0,2],[1,3],[1,4]]
))