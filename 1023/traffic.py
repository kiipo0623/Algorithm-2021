# 추석 트래픽
# 9:29
# 9:48

def solution(lines):
    answer = 0
    log = []
    for l in lines:
        l = l.split()
        hour = l[1][:2]
        minute = l[1][3:5]
        sec = l[1][6:8]
        milisec = l[1][9:]
        T = l[2][:-1]
        endtime = (int(hour) * 3600 + int(minute) * 60 + int(sec)) * 1000 + int(milisec)
        starttime = endtime - int(float(T) * 1000) + 1
        log.append((endtime, starttime))

    for l in log:
        answer = max(answer, count_traffic(log, l[0], l[0] + 1000), count_traffic(log, l[1], l[1] + 1000))

    return answer


def count_traffic(log, start, end):
    cnt = 0
    for l in log:
        if l[1] >= start and l[0] < end:
            cnt += 1
    return cnt

print(solution(["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"]))