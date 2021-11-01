def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)

    imsi_h = 0
    while True:
        more_h, less_h = 0, 0

        for i in range(n):
            if citations[i] >= imsi_h:
                more_h += 1
            else:
               less_h += 1

        print(more_h, less_h)
        if more_h >= imsi_h and less_h <= imsi_h:
            answer = imsi_h
            imsi_h += 1
        else:
            break

    return answer
print(solution([3,0,6,1,5]))