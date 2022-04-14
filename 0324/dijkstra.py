import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop()
        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
