from math import ceil
from collections import defaultdict

def solution(fees, records):
    answer = []
    car_list = defaultdict(list)
    car_money = defaultdict(int)
    default_time, default_fee, count_time, count_fee = fees

    for record in records:
        time, car, inout = record.split()
        time = changeTime(time)
        car_list[car].append(time)

    for car in car_list:
        time_sum = 0
        if len(car_list[car]) % 2 != 0:
            car_list[car].append(1439)

        for i in range(0, len(car_list[car]), 2):
            time_sum += car_list[car][i+1] - car_list[car][i]

        if time_sum > default_time:
            money_sum = default_fee + ceil((time_sum - default_time)/count_time) * count_fee
        else:
            money_sum = default_fee
        car_money[car] = money_sum

    keylist = sorted(car_money.keys())
    for k in keylist:
        answer.append(car_money[k])

    return answer


def changeTime(string):
    hour = int(string[:2])
    minute = int(string[3:])
    return hour * 60 + minute

print(solution(
[180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
))