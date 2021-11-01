# 다단계 칫솔 판매
# 1:44 - 2:37
# 한번 삽질/ 10/13 맞춤
from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    rcmd = defaultdict(list)
    money = defaultdict(int)

    def find_rcmd(enroll_index):
        temp = []
        while True:
            recommendername = referral[enroll_index]
            recommenderindex = enroll.index(recommendername)
            if referral[recommenderindex] == "-":
                temp.append("center")
                break
            else:
                temp.append(referral[recommenderindex])
                return find_rcmd(referral[recommenderindex])
        return temp

    for idx, e in enumerate(enroll):
        if referral[idx] == "-": # 추천자가 없으면 민호 추가
            rcmd[e].append("center")
        else: #추천자가 있으면 바로 위의 사람부터
            rcmd[e]=find_rcmd(idx)

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))