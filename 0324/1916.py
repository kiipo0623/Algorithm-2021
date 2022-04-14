import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append([b,c])

start, end = map(int, input().split())
distance = [INF]*(N+1)

def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue

        for node in edges[now]:
            cost = dist + node[1]
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(heap, [cost, node[0]])


dijkstra(start)
print(distance[end])
