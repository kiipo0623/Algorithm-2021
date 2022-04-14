def binarysearch(target, lst):
    start, end = 0, len(lst)
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] > target:
            end = start - 1
        elif lst[mid] < target:
            start = end + 1
        else:
            return mid
    return mid

def solution(info, query):
    answer = []
    developer = []
    for i in info:
        a, b, c, d, grade = i.split()
        grade = int(grade)
        developer.append([grade, a, b, c, d])
    developer.sort(key = lambda x : x[0])
    developer_grade = list(map(list, zip(*developer)))[0]

    for q in query:
        counter = 0
        cjp, _, bf, _, js, _, cp, g = q.split()
        g = int(g)
        check = binarysearch(g, developer_grade)

        while True:
            if check == -1:
                break
            if developer_grade[check] >= g:
                check -= 1
            else:
                break
        if check <= 0:
            check = 0
        else:
            check += 1

        for dev in developer[check:]:
            if cjp != '-' and cjp != dev[1]:
                continue
            if bf != '-' and bf != dev[2]:
                continue
            if js != '-' and js != dev[3]:
                continue
            if cp != '-' and cp != dev[4]:
                continue
            counter += 1
        answer.append(counter)
    return answer

print(solution(
["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
))