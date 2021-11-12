def solution(s):
    answer = []
    n = len(s)

    before = s[0]
    count = 1

    for i in range(1, n):
        if before == s[i]:
            count += 1
        else:
            answer.append(count)
            before = s[i]
            count = 1

    answer.append(count)

    if s[0] == s[n-1] and len(answer)>1:  # 처음과 끝이 같은 경우
        new = answer[0] + answer[-1]
        del answer[0]
        del answer[-1]
        answer.append(new)

    return sorted(answer)

print(solution("aaaaaa"))