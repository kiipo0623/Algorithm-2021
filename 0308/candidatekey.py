from itertools import combinations

def solution(relation):
    candidate_key = []
    idx = [i for i in range(len(relation[0]))]

    db = list(map(list, zip(*relation)))

    for i in range(1, len(relation[0])+1):
        combi = list(combinations(idx, i))
        for c in combi:
            flag = True
            for key in candidate_key:# 최소성 검사
                if set(key).issubset(c):
                    flag = False

            if flag == True:
                checklist = [db[i] for i in list(c)]
                if len(set(map(tuple, zip(*checklist)))) == len(relation): # 유일성 검사
                    candidate_key.append(c)

    return len(candidate_key)
