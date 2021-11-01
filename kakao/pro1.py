def solution(id_list, report, k):
    answer = [0] * len(id_list)
    people = dict()

    report = list(set(report))

    reportedcount = dict()
    reportmail = dict()

    for i in range(len(id_list)):
        people[id_list[i]] = 0

    for i in range(len(id_list)):
        reportedcount[id_list[i]] = 0
        reportmail[id_list[i]] = []


    for talk in report:
        user, reported = talk.split()
        reportmail[user].append(reported)
        reportedcount[reported] = reportedcount[reported]+1

    for person in reportedcount:
        if reportedcount[person] >= k:
            for mailperson in reportmail:
                if person in reportmail[mailperson]:
                    people[mailperson] += 1

    return list(people.values())

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))