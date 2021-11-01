#도둑질

def solution(money):
    answer = money[0]

    for i in range(1, len(money)):
        answer = max(answer - money[i-1] + money[i], answer)

    return answer

print(solution([1, 2, 3, 1]))

def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1): # 첫 집을 무조건 터는 경우[마지막집은 무조건 제외된다[
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)): # 마지막 집을 무조건 터는 경우
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대