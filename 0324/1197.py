import sys
input = sys.stdin.readline

V, E = map(int, input().split())
# 프림(정점기준) 크루스칼(간선기준)
graph = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c


def prim(start):
    answer = 0
    visit = [start]
    unvisit = []
    for i in range(1, V+1):
        if i != start:
            unvisit.append(i)

    for k in range(V-1):
        min_cost = int(1e9)
        min_uv = 0
        for vis in visit:
            for unv in unvisit:
                if graph[vis][unv] != 1000001 and graph[vis][unv] < min_cost:
                    min_cost = graph[vis][unv]
                    min_uv = unv
        answer += min_cost
        visit.append(min_uv)
        unvisit.remove(min_uv)

    return answer


print(prim(1))