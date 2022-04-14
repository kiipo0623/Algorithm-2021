import sys
input = sys.stdin.readline

N, K = map(int, input().split())
use_list = list(map(int, input().split()))

plug = [0]*N
count = 0
res = swap = num = max_I = 0

for i in range(len(use_list)):
    if use_list[i] in plug:
        pass

    elif 0 in plug: # 빈칸이 존재하는 경우
        plug[plug.index(0)] = use_list[i]

    else: # 빈칸이 존재하지 않는 경우 : 1) 앞으로 등장하지 않는 것 삭제 2) 모두 등장한다면 가장 늦게 등장하는 것 삭제
        for j in plug:
            if j not in use_list[num:]:
                swap = j
                break
            elif use_list[num:].index(j) > max_I:
                max_I = use_list[num:].index(j)
                swap = j
        plug[plug.index(swap)] = i
        max_I = swap = 0
        res += 1
    num += 1
print(res)