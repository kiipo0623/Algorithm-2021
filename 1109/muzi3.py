def solution(food_times, k):
    while True:
        for i in range(len(food_times)):
            if k == -1: # 만약에 i가 마지막 번째인 경우
                return i

            if set(food_times) == {0}: #k가 0이 아닌데 음식을 다 먹은 경우
                return -1

            if food_times[i] > 0:
                food_times[i] -= 1
                k -= 1

print(solution([1,1,1],3))