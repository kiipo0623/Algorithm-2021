def solution(id_list, report, k):
    answer = []
    reporter = {} # 누구를 신고했는지 리스트
    report_count = {} # 몇번 신고당했는지 리스트
    out = []
    report = list(set(report))

    for id in id_list:
        report_count[id] = 0
        reporter[id] = []

    for r in report:
        a, b = r.split()
        reporter[a].append(b)
        report_count[b] += 1

    for rc in report_count:
        if report_count[rc] >= k:
            out.append(rc)

    for r in reporter:
        count = 0
        for person in reporter[r]:
            if person in out:
                count += 1
        answer.append(count)

    return answer

print(solution(
["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    2
))