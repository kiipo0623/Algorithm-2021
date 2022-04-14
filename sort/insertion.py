list = [1, 9 ,3, 2, 2, 4, 3]

for i in range(1, len(list)):
    # 매번 한칸씩 밀어야 한다
    for j in range(i, 0, -1):
        if list[j-1] > list[j]: # 비교 대상이 더 크면
            list[j-1], list[j] = list[j], list[j-1]

print(list)



