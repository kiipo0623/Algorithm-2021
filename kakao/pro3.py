import math
def solution(fees, records):
    cars = dict()
    temp = dict()
    # cars 안에 누적시간 입력
    # temp 안에 in만 있을 때
    answer = dict()

    for record in records:
        time, car, inout = record.split()
        print("car:",car)

        if inout == 'IN':
            temp[car] = time

        if inout == 'OUT':
            intime = temp[car]
            del temp[car]
            if car not in cars:
                cars[car] = 0

            in_hour = int(intime[0:2])
            in_minute = int(intime[3:5])
            in_time = in_hour*60 + in_minute
            print("in_time:", in_time)
            out_hour = int(time[0:2])
            out_minute = int(time[3:5])
            out_time = out_hour*60 + out_minute
            print("out_time", out_time)

            cars[car] += out_time - in_time

    for remainder in temp:
        if remainder not in cars:
            cars[remainder] = 0

        intime = temp[remainder]

        in_hour = int(intime[0:2])
        in_minute = int(intime[3:5])
        in_time = in_hour * 60 + in_minute

        cars[remainder] += (23*60 + 59) - in_time

    for number in cars:
        if cars[number] <= fees[0]:
            answer[number] = fees[1]
        else: # 올림 내림 해야
            cal = (cars[number] - fees[0])
            if cal % fees[2] != 0:
                calculated = cal // fees[2] + 1
            else:
                calculated = cal // fees[2]
            answer[number] = int(calculated * fees[3] + fees[1])

    answer = dict(sorted(answer.items(), key = lambda x: x[0]))
    print(answer)

    return list(answer.values())

fees =[180, 5000, 10, 600]
records =["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))