from copy import deepcopy
from collections import defaultdict

def solution(goods):
    answer = []
    dict = defaultdict(str)

    for i in range(len(goods)):
        dict[goods[i]] = ""

    for test in goods:
        length = len(test)
        for i in range(1, length):
            check = [test[k:k + i] for k in range(0, len(test), 1)]
            check = list(set(check))
            print("before", check)

            for good in goods: # 비교 대상
                if good == test:
                    continue; # 자기 자신인 경우 제외

                for c in check[:]: # 글자 하나씩 비교
                    if c in good:
                        print("중복", c, good)
                        check.remove(c)

            if check: # 비어 있지 않으면
                check = sorted(check)
                dict[test] = ' '.join(check)
                break

    for key, value in dict.items():
        if value == "":
            answer.append("None")
        else:
            answer.append(value)


    return answer

print(solution(
["pencil","cilicon","contrabase","picturelist"]
))