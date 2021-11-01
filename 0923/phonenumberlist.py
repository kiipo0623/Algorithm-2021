from collections import defaultdict
def solution(phone_book):
    call_book = defaultdict(list)

    # 같은 앞자리끼리만 비교하도록
    for phone in phone_book:
        call_book[int(phone[0])].append(phone)

    for number in call_book: # 콜북에 있는 번호 전체 (1~9)
        call_book[number].sort()
        for i in range(len(call_book[number])): # 해당 넘버(1~9)에 딸린 리스트 하나씩 : 비교 주체
            length = len(call_book[number][i])
            length = len(call_book[number][i])
            for j in call_book[number][i+1:]: # 그 다음 순번부터 비교 대상
                if len(j) >= length and call_book[number][i] == j[:length]:
                    return False
    return True

print(solution(["123", "456", "789"]))

# 보통 효율성에서 막히면 새로운 알고리즘을 제시해야 되는 경우밖에 없다(완전 갈엎)
