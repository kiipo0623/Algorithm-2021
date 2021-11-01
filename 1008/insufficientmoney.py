# 부족한 금액 계산하기
# 프로그래머스 위클리 챌린지
# 4:27 - 4:31

def solution(price, money, count):
    countsum = count*(count+1)/2
    pricesum = price * countsum

    if pricesum > money:
        return pricesum-money
    else:
        return 0

