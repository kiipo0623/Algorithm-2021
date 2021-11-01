# 오픈채팅방
# 11:13 - 11:22
from collections import defaultdict

def solution(record):
    answer = []
    uidnick = defaultdict(str)

    for r in record:
        choprecord = r.split()
        if len(choprecord) == 3:
            uidnick[choprecord[1]] = choprecord[2]

    for r in record:
        choprecord = r.split()
        temp = ''
        temp += uidnick[choprecord[1]]

        if choprecord[0] == "Enter":
            temp += "님이 들어왔습니다."
        elif choprecord[0] == "Leave":
            temp += "님이 나갔습니다"
        elif choprecord[0] == "Change":
            continue
        answer.append(temp)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))