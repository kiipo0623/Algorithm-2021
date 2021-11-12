def solution(arr):
    answer = []
    dict = {1:0, 2:0, 3:0}
    for atom in arr:
        dict[atom] += 1
    maxnum = max(dict.values())
    for k in dict:
        answer.append(maxnum - dict[k])
    return answer