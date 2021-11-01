def solution(n, k):
    answer = 0

    #진수 변환
    num = convert(n, k)

    temp = ''
    for i in range(len(num)):
        if temp and num[i] == '0':
            if isprime(int(temp)):
                answer += 1
            temp = ''
        elif num[i] == 0:
            continue
        else:
            temp += num[i]

    if temp:
        answer += isprime(int(temp))

    return answer

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def isprime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(solution(110011, 10))