def solution(food_times, k):
    sorting = sorted(food_times)
    length = len(food_times)

    for s in set(sorting): # 최솟값 하나씩 카운팅해서 한번에 빼기
        if s*length < k: # 아직 범위 내인 경우
            k -= s*length
            huddle = s
            length -= food_times.count(s)

        else: # 범위 밖인 경우 : 직접 확인
            huddle -= 1
            while True:
                huddle += 1
                for i in range(len(food_times)): # 0번째부터 확인
                    if k == 0: # 종료 조건
                        if i != len(food_times):
                            return i+1
                        else:
                            for j in range(len(food_times)):
                                if j > huddle:
                                    return j + 1
                    if food_times[i] <= huddle: # 이미 없는 음식
                        continue
                    else: #있는 음식 : 1 빼줌
                        k -= 1

    return -1

print(solution([2, 3,1,4,6], 10))