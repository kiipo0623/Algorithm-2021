from collections import defaultdict
from itertools import combinations

def solution(logs):
    answer = []
    student = defaultdict(list)
    # student key = no 리스트 형태 [문제번호, 점수]
    for log in logs:
        no, question, grade = log.split()
        question = int(question)
        grade = int(grade)
        isin = False
        for i in range(len(student[no])):
            if student[no][i][0] == question and student[no][i][1] < grade:
                student[no][i][1] = grade
                isin = True
        if isin == False:
            student[no].append([question, grade])

    combi = list(combinations(student.keys(), 2))
    print(combi)
    for st1, st2 in combi:
        if sorted(student[st1]) == sorted(student[st2]) and len(student[st1])>=5:
            answer.append(st1)
            answer.append(st2)
    if answer:
        return sorted(list(set(answer)))
    else:
        return ["None"]
print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))