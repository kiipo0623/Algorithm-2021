def solution(arr, brr):
    answer = 0
    sum_a = 0
    sum_b = 0
    for i in range(len(arr)):
        sum_a += arr[i]
        sum_b += brr[i]
        if sum_a != sum_b:
            answer += 1

    return answer-1