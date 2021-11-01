# 2019 카카오 겨울 인턴십
# 3:00 -
# 2019 카카오 겨울 인턴십
# 3:00 -
# 2019 카카오 겨울 인턴십
# 3:00 -
from collections import defaultdict
from itertools import product
def solution(user_id, banned_id):
    candidate = defaultdict(list)
    for k in range(len(banned_id)):
        for user in user_id:
            flag = True
            if len(banned_id[k]) != len(user):
                flag = False
            else:
                for i in range(len(banned_id[k])):
                    if banned_id[k][i] == '*':
                        continue
                    if banned_id[k][i] != user[i]:
                        flag = False
                        break

            if flag == True:
                candidate[k].append(user)


    ## 여기까지는 완성 : 입출력 예가 좀만 더 불친절했으면 해결 못햇다


    check = list(product(*candidate.values()))
    print(check)
    print(len(check))

    banned_set = []

    for c in check:
       if len(set(c)) != len(candidate):
           continue
       else:
           if set(c) not in banned_set:
               banned_set.append(set(c))

    return len(banned_set)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))