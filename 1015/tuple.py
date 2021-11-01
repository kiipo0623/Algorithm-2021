# 2019 카카오 개발자 겨울 인턴
# 튜플
# 6:25 - 6:37

def solution(s):
    answer = []
    tuples = dict()

    split1 = s[2:-2].split("},{")
    for s in split1:
        temp = s.split(",")
        temp2 = []
        for t in temp:
            temp2.append(int(t))
        tuples[len(temp2)] = temp2

    sorted_tuples = sorted(tuples.items())
    print(sorted_tuples)

    answer.append(sorted_tuples[0][1][0])

    for i in range(1, len(sorted_tuples)):
        now = sorted_tuples[i][1]
        before = sorted_tuples[i-1][1]

        for n in now:
            if n not in before:
                answer.append(n)
                break
    return answer

print(solution("{{123}}"))