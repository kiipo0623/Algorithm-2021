def str2int(string):
    hour, minute, second = string.split(':')
    return int(hour) * 3600 + int(minute) * 60 + int(second)


def int2str(time):
    hour = str(time // 3600).zfill(2)
    time = time % 3600
    minute = str(time // 60).zfill(2)
    second = str(time % 60).zfill(2)
    return hour + ':' + minute + ':' + second


def solution(play_time, adv_time, logs):
    play_time = str2int(play_time)
    adv_time = str2int(adv_time)
    all_time = [0 for _ in range(len(play_time) + 1)]

    for log in logs:
        start, end = log.split('-')
        start = str2int(start)
        end = str2int(end)
        all_time[start] += 1
        all_time[end] -= 1

    maxtime = 0
    starttime = 0

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(adv_time - 1, play_time):
        if adv_time >= i:
            if all_time[i] - all_time[i - adv_time] > maxtime:
                maxtime = all_time[i] - all_time[i - adv_time]
                starttime = i - adv_time + 1

        else:
            if all_time[i] > maxtime:
                maxtime = all_time[i]
                starttime = i - adv_time + 1

    return str2int(starttime)