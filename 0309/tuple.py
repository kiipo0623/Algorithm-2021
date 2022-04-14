def solution(s):
    answer = []
    s = s.split('},')
    new_s = []
    for tmp in s:
        tmp = tmp.replace('{', '')
        tmp = tmp.replace('}', '')
        new_s.append(tmp)

    new_s.sort(key = lambda x: len(x))

    answer.append(int(new_s[0]))

    for k in new_s[1:]:
        k = k.split(',')
        k = list(map(int, k))

        for a in answer:
            k.remove(a)
        answer.append(k[0])

    return answer

print(solution(
"{{2},{2,1},{2,1,3},{2,1,3,4}}"
))
print(solution(
"{{1,2,3},{2,1},{1,2,4,3},{2}}"
))