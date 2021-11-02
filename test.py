def solution(n, t, m, timetable):
    timetable = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    timetable.sort()
    last_time = (60 * 9) + (n-1) * t # 마지막 배차의 시간표 (분단위)

    # 배차 횟수만큼 반복
    for i in range(n):
        # timetable의 길이가 한면 번에 태울 수 있는 인원보다 적으
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)

        # 마지막 배차의 경우
        if i == n-1:
            # timetable에 마지막 배차 때 우선순위가 높은 크루가 있다면
           if timetable[0] <= last_time:
               # 마지막 탑승자보다 1초 빠르게
               last_time = timetable[m-1] - 1
               return '%02d:%02d' % (last_time // 60, last_time % 60)
           # del로 인한 index 변화에 영향을 주지 않게 위해서 거꾸로 반복
           for j in range(m-1, -1, -1, -1):
               bus_arrive = (60 * 9) + i * t
               if timetable[j] <= bus_arrive:
                   del timetable[j]