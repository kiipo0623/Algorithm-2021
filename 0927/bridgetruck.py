from collections import deque
def solution(bridge_length, weight, truck_weights):
    onbridgetruck = deque()
    beforebridgetruck = deque()
    afterbridgetruck = deque()

    for tw in truck_weights:
        temp = [tw, 0]
        beforebridgetruck.append(temp)

    totalweight = 0
    totalnum = 0
    time = 1
# 1초에 하나만 진입 할 수 있고 하나만 나갈 수 있다는 점을 코딩하지 않았다..
# 이걸 반복문을 if로 바꾸면 bridge 앞에 하나 안에 하나만 계산이 된다 ..

    while onbridgetruck or beforebridgetruck:
        templist = 0
        for truck in onbridgetruck:
            if truck[1] >= bridge_length:
                templist += 1
            truck[1] += 1

        if templist:
            truck = onbridgetruck.popleft()
            afterbridgetruck.append(truck)
            totalweight -= truck[0]
            totalnum -= 1

        if beforebridgetruck: # 하나만 받아줘야
            truck = beforebridgetruck[0]
            if totalweight + truck[0] <= weight and totalnum < bridge_length:
                truck[1] = 1
                onbridgetruck.append(truck)
                totalweight += truck[0]
                totalnum += 1
                beforebridgetruck.popleft()


        if len(afterbridgetruck) == len(truck_weights): # 다음 타임으로 더해주는 것 방지
            break

        time += 1

    return time

print(solution(	2, 10, [7, 4, 5, 6]))