from collections import deque
def solution(arr, processes):
    answer = []
    pro_list = []
    cur_time = 0
    work_time = 0
    now_queue = []

    # 전처리 : R/W 숫자로 / read에 마지막 조건
    for process in processes:
        temp = process.split()
        if temp[0] == "read":
            temp[0] = 1
            temp.append(0);
        else:
            temp[0] = 0
        for i in range(1, len(temp)):
            temp[i] = int(temp[i])
        pro_list.append(temp)

    pstart = 0
    while True:
        for i in range(pstart, len(processes)):
            if pro_list[i][1] <= cur_time:
                now_queue.append(pro_list[i])
                pstart+=1
            else:
                break

        if len(now_queue) == 0: #비었으면
            cur_time = pro_list[0][1]
            continue

        # 안비었으면 큐 정리
        now_queue = sorted(now_queue, key = lambda x : (x[0], x[1]))
        now_queue = deque(now_queue)
        work = now_queue.popleft()

        if work[0] == 0: # write해야 하는 경우
            _, starttime, duringtime, idxstart, idxfin, subtle = work
            cur_time += duringtime
            for i in range(idxstart, idxfin+1):
                arr[i] = subtle
        else: # 끝나기 전까지 read가 들어올건지 확인해준다
            work_list = [work] # 동시에 수행할 read들
            while now_queue:
                if now_queue[0][0] == 1:
                    work_list.append(now_queue.popleft())
                else:
                    break

            read_max_time = 0
            for readwork in work_list:
                _, starttime, duringtime, idxstart, idxfin, subtle = readwork
                answer.append(''.join(arr[idxstart:idxfin+1]))
                if duringtime>=read_max_time:
                    read_max_time = duringtime

            cur_time = read_max_time

    return answer

print(solution(
["1","2","4","3","3","4","1","5"],
["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
)
)