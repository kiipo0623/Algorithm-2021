import heapq
def solution(n, edge):
    answer = 0
    global INF
    INF = int(1e9)
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)

    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 다른 노드 확인
            for j in graph[now]:
                cost = dist + 1
                if cost < distance[j]:
                    distance[j] = cost
                    heapq.heappush(q, (cost, j))

    dijkstra(1)

    maximum = max(distance[1:])
    for i in range(1, n+1):
        if distance[i] == maximum:
            answer += 1

    print(distance)

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

