# 광고 삽입
# 11:00 - 11:23 시간초과
# 11:42 포기 어디가 틀린지 알수가없음
def timechange(string):
    hour = int(string[:2])
    minute = int(string[3:5])
    second = int(string[6:])
    return (hour*60*60) + (minute*60) + second

def solution(play_time, adv_time, logs):
    new_log = []
    max_time = 0
    max_index = 0

    if play_time == adv_time:
        return "00:00:00"

    adv_time = timechange(adv_time)

    for log in logs:
        start, end = log.split("-")
        newstart = timechange(start)
        newend = timechange(end)
        new_log.append((newstart, newend, start))

    new_log.sort()

    for i in range(len(new_log)):
        timecount = 0
        advstart = new_log[i][0]
        advend = new_log[i][0] + adv_time

        for j in range(i):
            # 끝나는 시간이 adv 시작 시간보다 늦어야 한다
            if new_log[j][1] > advstart:
                timecount += min(new_log[j][1], advend) - advstart

        for j in range(i, len(new_log)):
            # 시작 시간이 adv 끝나는 시간보다 빨라야 한다
            if new_log[j][0] <= advend:
                timecount += min(advend, new_log[j][1]) - new_log[j][0]

        if timecount > max_time:
            max_time = timecount
            max_index = i

    return new_log[max_index][2]