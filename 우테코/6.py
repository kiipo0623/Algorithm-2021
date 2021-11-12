def solution(time, plans):
    answer = '호치민'

    gowork = 13
    offwork = 18

    for place, depart, arrive in plans:
        print("outtime", offwork - changetime(depart))
        if offwork - changetime(depart) > 0:
            time -= offwork - changetime(depart)
        print("outtime", changetime(arrive) - gowork)
        if changetime(arrive) - gowork > 0:
            time -= changetime(arrive) - gowork


        if time >= 0:
            answer = place
        else:
            break
    return answer

def changetime(string):
    if string[-2:] == 'AM':
        return int(string[:-2])
    else:
        return int(string[:-2])+12

print(solution(3.5,
[ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]
))