from collections import defaultdict
import math
import sys
sys.setrecursionlimit(100000)

def sendmoney(sender, amount):
    send = math.floor(amount * 0.1)
    money[sender] += amount - send  # 받은 총액에서 보낼분량 빼고 내 지갑에 넣음

    if send < 1:
        return 0

    parent = tree[sender]  # 부모 노드 찾음
    if parent == "center":  # 부모 노드가 끝인 경우 그냥 끝냄
        return 0
    else:  # 부모노드가 끝이 아닌 경우
        sendmoney(parent, send)

# 재귀를 안쓸 수 없는 문제 ..
def solution(enroll, referral, seller, amount):
    answer = []
    global tree
    tree = defaultdict(str)
    global money
    money = defaultdict(int)

    for idx, e in enumerate(enroll):
        if referral[idx] == "-":
            tree[e] = "center"
            money[e] = 0
        else:
            tree[e] = referral[idx]

    for idx, s in enumerate(seller):
        sendmoney(s, amount[idx]*100) # 함수 실행

    for e in enroll:
        answer.append(money[e])

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))