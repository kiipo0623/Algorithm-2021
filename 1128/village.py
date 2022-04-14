import heapq
def solution(N, road, K):
    count = 0
    INF = int(1e9)
    distance = [INF for _ in range(N + 1)]

    village = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

    for a, b, c in road:
        village[a][b] = min(c, village[a][b])
        village[b][a] = min(c, village[b][a])

    # 다익스트라 사용
    q = []
    # 거리, 노드
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in range(1, N + 1):
            # cost = 기준부터 종점까지 + 나부터 기준까지
            cost = dist + village[now][i]
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    print(distance)

    for a in distance:
        if a <= K:
            count += 1

    return count

print(solution(
6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4
))

# ㄷㅏ익스트라 : 그래프에서 특정 시작점에서 각 노드까지 최단 거리 구하기 위해
# visited와 distance를 사용할 수 있고
# min heap을 사용할 수 있다
# 반복문을 돌면서 그 지점을 통해서 가는게 더 가까우면 distance를 갱신하는 방