def solution(log):
    answer = 0
    for i in range(0, len(log), 2):
        start = changetime(log[i])
        end = changetime(log[i+1])
        time = end - start

        if time < 5:
            time = 0
        elif time > 105:
            time = 105

        answer += time

    hour = str(answer // 60)
    minute = str(answer % 60)

    sol = hour.zfill(2)+':'+minute.zfill(2)

    return sol

def changetime(string):
    hour = int(string[:2])
    minute = int(string[3:])
    return (hour*60)+minute

print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))