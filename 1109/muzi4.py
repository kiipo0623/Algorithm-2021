import heapq

def solution(food_times, k):
    answer = -1 # default
    h = []
    n = len(food_times)
    p = 0

    for i in range(n):
        heapq.heappush(h, (food_times[i], i+1)) #이떄 i가 아닌 i+1부터 삽입하면 문제 조건에 맞출 수 있다

    while h:
        t = (h[0][0] - p) * n # 이때 힙에서 뽑지 말고 값만 조회한다. 확실히 뺴도 되는 상황인지 확인해야 하기 때문

        if k >= t:
            k -= t
            n -= 1
            p, _ = heapq.heappop(h)

        else:
            sortfood = sorted(h, key=lambda x:x[1]) # sort 할때 lambda 사용하면 key=lamdba x=x[1]
            idx = k % n
            answer = sortfood[idx][1]
            break

    return answer

print(solution([3,1,2],5))