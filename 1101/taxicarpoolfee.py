import heapq
def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라로 했는데 플로이드로 했어야함 .. 모든 정점 -> 모든 정점
def solution(n, s, a, b, fares):
    answer = 0
    global graph
    graph = [[] for i in range(n+1)]
    global distance
    distance = [100001] * (n+1)

    for start, end, fee in fares:
        graph[start].append((end, fee))
        graph[end].append((start, fee))

    dijkstra(s)
    # 지금 distance를 이제 아는 상태
    answer = distance[a] + distance[b]
    for i in range(1, n+1):
        temp = distance[i]

    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
               ))