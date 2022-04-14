from itertools import combinations
from copy import deepcopy

def solution(relation):
    len_relation = len(relation)
    rel = [i for i in range(len(relation[0]))]
    candkey = []

    for i in range(1, len_relation+1):
        check = list(combinations(rel, i))

        for che in check:
            temp = []
            for idx, item in enumerate(relation):
                now = []
                for c in che:
                    now.append(relation[idx][c])
                temp.append(tuple(now))
            print("temp", temp)
            if len(set(temp)) == len_relation:
                candkey.append(che)
    print(candkey)
    answer = deepcopy(candkey)
    print(candkey)
    # candkey 중복제거
    for i in range(len(candkey)):
        for j in range(i+1, len(candkey)):
            if len(candkey[i]) == len(set(candkey[i])&set(candkey[j])):
                if candkey[j] in answer:
                    answer.remove(candkey[j])


    return len(answer)

print(solution(
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
))