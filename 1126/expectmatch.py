# 예상 대진표
# 11:08 - 11:03
def solution(n, a, b):
    answer = 1
    A = min(a, b)
    B = max(a, b)

    while True:
        if A + 1 == B and A % 2 == 1:
            return answer

        if A % 2 == 0:
            A = A / 2
        else:
            A = (A + 1) / 2

        if B % 2 == 0:
            B = B / 2
        else:
            B = (B + 1) / 2
        answer += 1

    return answer