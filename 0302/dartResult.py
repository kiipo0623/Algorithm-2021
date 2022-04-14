def solution(dartResult):
    string = []
    cal = []

    temp = dartResult[0]
    for d in dartResult[1:]:
        if d.isdigit():
            if len(temp) == 1:
                temp += d
            else:
                string.append(temp)
                temp = d
        else:
            temp += d
    string.append(temp)

    print("string", string)

    for s in string:
        if s[1].isdigit():
            num = 10
        else:
            num = int(s[0])

        for k in s:
            if k in ['S', 'D', 'T']:
                if k == 'D':
                    num = num * num
                elif k == 'T':
                    num = num * num * num
            if k in ['*', '#']:
                if k == '*':
                    num *= 2
                    if len(cal):
                        cal[-1] = cal[-1]*2
                if k == '#':
                    num *= (-1)
        cal.append(num)

    return sum(cal)

print(solution('1D2S#10S'))