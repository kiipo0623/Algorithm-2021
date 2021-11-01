def solution(s):
    n = len(s)
    answer = n + 1
    repeat = n // 2

    for i in range(1, repeat+1): # i개짜리가 반복된다는 뜻
        count = 1
        newstr = ''
        before = s[:i]

        for j in range(i, n, i):
            now = s[j:j+i]
            if before == now:
                count += 1
            else:
                if count == 1:
                    newstr += before
                else:
                    newstr += str(count) + before
                count = 1
                before = now # 여기서 잘못됨

        # 짬처리
        if count == 1:
            newstr += before
        else:
            newstr += str(count) + before

        # 최소 비교
        if answer > len(newstr):
            answer = len(newstr)
            temp = newstr

    return answer, temp

print(solution("abcabcdede"))