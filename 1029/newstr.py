# 문자열 압축
def solution(s):
    n = len(s)
    answer = n+1
    repeat = n // 2

    for i in range(1, repeat+1): # 몇개씩 컷하는게 나을지
        count = 1
        newstr = ''
        before = s[:i]

        for j in range(1, n-i+1): # 한 알파벳씩 도는 거
            if before == s[j:j+i]: # 앞이랑 중복
                count += 1
                before = s[j:j+1]
            else: # 중복 아님
                if count == 1:
                    newstr += before
                else:
                    newstr += str(count) + before
                count = 1
                before = s[j:j+1]
        if count == 1: # 남은거 처리
            newstr += before
        else:
            newstr += str(count) + before
        answer = min(answer, len(newstr))

    return answer

print(solution("aabbaccc"))