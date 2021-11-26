# 124 나라의 숫자
# 6:18 - 6:51
# 결과 : 감은 잡았지만 실패

def solution(n):
    answer = ''
    while n > 0:
        nanu = n%3
        if nanu == 1:
            answer = '1' + answer
        elif nanu == 2:
            answer = '2' + answer
        elif nanu == 0:
            answer = '4' + answer
        n = n//3
    return answer
# 왜 1을 매번 빼줘야 하는지 . 나눗셈 할 때 넣으면 안되는지 설명하기
# 3개씩 끊기는데, 3으로 나눈다 치면 3의 배수들이 튀게 됨..

print("3:",solution(3))
print("4:",solution(4))
print("5:",solution(5))
print("6:",solution(6))
print("7:",solution(7))
print("8:",solution(8))
print("9:",solution(9))
print("10:",solution(10))
print("11:",solution(11))
print("12:",solution(12))

