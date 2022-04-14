def solution(s):
    answer = ''
    numdict = {'ze': [0, 4], 'on': [1, 3], 'tw': [2, 3], 'th': [3, 5],
               'fo': [4, 4], 'fi': [5, 4], 'si': [6, 3], 'se': [7, 5],
               'ei': [8, 5], 'ni': [9, 4]}
    while len(s):
        if s[0].isdigit():
            answer += s[0]
            s = s[1:]
        else:
            number, length = numdict[s[0:2]]
            answer += str(number)
            s = s[length:]

    return int(answer)

print(solution("2three45sixseven"))