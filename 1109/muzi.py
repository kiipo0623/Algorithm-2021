# 무지의 먹방 라이브
# 3:44 -

def solution(food_times, k):
    length = len(food_times)
    huddle = 0

    while True:
        minimum_time = min(food_times)
        count = 0

        if minimum_time * length < k:
            k -= minimum_time * length


        elif minimum_time * length == k:
            return 1
        else: # minimum_time * length > k:
            # 돌면서 1씩 빼줌
            for i in range(1, minimum_time):
                print("temp")

        length -= count

    return answer

print(solution([3, 1, 2], 5))