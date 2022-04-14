from collections import deque
def solution(arr, processes):
    answer = []
    pro_list = []
    work_time = 0

    for process in processes:
        temp = process.split()
        if temp[0] == "read":
            temp.append(0);

        for i in range(1, len(temp)):
            temp[i] = int(temp[i])
        temp.append(False)
        pro_list.append(temp)
    print(pro_list)

    cur_time = 0
    while True:
        write_idx = -1
        fin_idx = -1
        wait_list = []

        # 다 확인 / process를 삭제
        for i in range(0, len(pro_list)):
            if pro_list[i][1] <= cur_time:
                wait_list.append(pro_list[i])
                fin_idx = i
                if pro_list[i][0] == 'write':
                    write_idx = i
                    break
            else:
                break

        if len(wait_list) == 0: # 나중에 구현 : 빈 경우
            if pro_list:
                cur_time = pro_list[0][1]
                continue
            else:
                break

        if write_idx != -1:
            RW, t1, t2, A, B, C, flag = pro_list[write_idx]
            cur_time += t2
            for i in range(A, B+1):
                arr[i] = str(C)
            pro_list.remove([RW, t1, t2, A, B, C, flag])
            work_time += t2

        else: # 읽기 하는 경우
            # 범위를 늘려서 뒤에 있는지 확인
            _, t1, t2, A, B, C, _ = wait_list[0]

            for i in range(fin_idx+1, len(pro_list)):
                if pro_list[i][1] < cur_time + t2:
                    if pro_list[i][0] == 'write':
                        break
                    wait_list.append(pro_list[i])
                else:
                    break

            max_time = cur_time+t2
            for work in wait_list:
                RW, t1, t2, A, B, C, flag = work
                answer.append(''.join(arr[A:B+1]))
                max_time = max(max_time, max(t1, cur_time)+t2)
                pro_list.remove([RW, t1, t2, A, B, C, flag])
            print("max", max_time, "cur", cur_time)
            work_time += max_time - cur_time
            cur_time = max_time



    answer.append(str(work_time))
    return answer

print(solution(
["1","2","4","3","3","4","1","5"],
["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
)
)

print(solution(
["1","1","1","1","1","1","1"],
["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]
))