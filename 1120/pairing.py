def solution(s):
    answer = 0
    ptr1 = 0
    ptr2 = 1

    while True:
        if set(s) == '0':
            return 1

        if s[ptr1]!='0' and s[ptr1] == s[ptr2]: # ptr1 == 0인 경우는 못함
            s[ptr1] = '0'
            s[ptr2] = '0'

            if ptr1 == 0:
                ptr1 = ptr2+1
                ptr2 = ptr2+2
            else:
                ptr1 -= 1
                ptr2 += 1




    return answer

# 투포인터 써서 문제 한번 풀어보