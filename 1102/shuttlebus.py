# 셔틀버스
# 10:04 -
# 시간은 보통 숫자로 바꿔서 하는데 .. 바꿔야 되는지 ? 바꾸는 게 편할 거 같
# 87점(3개틀림) -> 100점 : timetable을 sort하지 않아서 ..
def timechangetoint(time):
    hour = int(time[0:2]) * 60
    minute = int(time[3:5])
    return hour + minute

def intchangetotime(inttime):
    hour = str(inttime // 60)
    minute = str(inttime % 60)
    if len(hour) == 1:
        hour = '0'+hour
    if len(minute) == 1:
        minute = '0'+minute
    time = hour + ':' + minute
    return time

def solution(n, t, m, timetable):
    bus = {}
    start = 540

    for i in range(n):
        bus[start] = []
        start += t

    for i in range(len(timetable)):
        new = timechangetoint(timetable[i])
        timetable[i] = new

    timetable.sort()

    for time in timetable: # 크루원들 출근 시간을 하나씩 받아와서
# 여기서 에러 났을 것 같음
        for b in bus: # 버스 시간 처음부터 탐색 :
            if time <= b and len(bus[b]) < m: # 조건(크루원이 먼저 와야 되고 버스 좌석 있어야) 맞으면
                bus[b].append(time) # 추가
                break
    # 정리 완료 이제 콘이 몇시에 들어갈지 알고리즘 정하고 코딩하면 됨
    # 일단 마지막 셔틀 시간에 자리가 있는지 확인 -> 있으면 들어감
    # 마지막 셔틀 시간에 자리가 없다면? 셔틀 안에서 가장 늦은 애(max값) 보다 1 줄임
    # 다루지 못한 부분 : 앞에 시간이 꽉차있고 뒷시간 1분 땡기는걸로 안되면 ?

    print(bus)
    con = list(bus.keys())[-1]
    print("con", con)

    if len(bus[con]) < m:
        return intchangetotime(con)
    else:
        return intchangetotime(max(bus[con])-1)

print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))