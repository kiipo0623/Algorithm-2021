def solution(arr, processes):
    answer = []
    pro_list = []

    for process in processes:
        temp = process.split()
        if temp[0] == "read":
            temp.append(0);

        for i in range(1, len(temp)):
            temp[i] = int(temp[i])
        temp.append(False)
        pro_list.append(temp)

    print(pro_list)

    now = "nothing"
    fin_time = 0
    for cur_time in range(0, 1100):
        candidate = []
        # 현재 시간에 할일 대기중인것 다 가져
        idx = 0
        while idx<len(pro_list):
            if pro_list[idx][1] <= cur_time and pro_list[idx][-1] == False:
                candidate.append(pro_list[idx])
                idx+=1
            else:
                break

        print(cur_time, candidate)

        # if len(candidate) == 0: # 일이 없으면 타임 워프
        #     cur_time = pro_list[0][1]
        #
        # if now == "nothing":
        #     for pro in candidate:
        #         work, t1, t2, A, B, C, flag = pro
        #         if work == 'write': # write가 있으면
        #             now = "writing"
        #
        #         elif pro == 'read': # read 할 차례면
        #             now = "reading"
        #             fin_time = cur_time + pro[2]
        # elif now == "reading":
        #     # 시간 내의 상황이면 그냥 둠
        #     # 새로운 read가 들어올 수 있음
        #     if cur_time
        #
        # elif now == "writing":
        #     # 다른 일을 할 수 없음


    return answer


print(solution(
["1","2","4","3","3","4","1","5"],
["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
)
)