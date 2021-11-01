import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    if scoville[0] >= K:
        return answer

    while len(scoville) >= 2:
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)

        hot = food1 + (food2 * 2)
        heapq.heappush(scoville, hot)

        answer += 1

        if scoville[0] >= K:
            return answer

    return -1

print(solution([12, 10, 9, 3, 2, 1], 7))