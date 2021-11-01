def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance)
    # left, right 기준 : 제거된 돌의 개수
    # 이분탐색 : 거리를 기준으로
    start, end = 0, distance

    while start <= end:
        mid = (start + end) // 2
        current = 0
        min_distance = float('inf')
        remove_rock = 0

        for rock in rocks:
            if rock - current < mid:
                remove_rock += 1
            else:
                min_distance = min(min_distance, rock - current)
                current = rock

        if remove_rock > n:
            end = mid - 1
        else:
            answer = min_distance
            start = mid + 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))