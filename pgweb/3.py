def solution(s):
    answer = 0
    keyboard = [list('qwertyuio'), list('pasdfghjk'), list('lzxcvbnm')]
    print(keyboard)

    complexity = {}

    for i in range(len(s)-1):
        firstalpha = s[i]
        secondalpha = s[i+1]
        for i in range(3):
            if firstalpha in keyboard[i]:
                firstrow = i
                firstcol = keyboard[i].index(firstalpha)
            if secondalpha in keyboard[i]:
                secondrow = i
                secondcol = keyboard[i].index(secondalpha)

        dis = abs(firstrow-secondrow) + abs(firstcol-secondcol)
        complexity[firstalpha+secondalpha] = dis

    for i in range(len(s)-1): # 0 1 2 3 시작하는 점
        beforestring = s[i:i+2]
        beforecount = complexity[beforestring]
        answer += beforecount
        for j in range(3, len(s)-i+1):
            nowstring = s[i:i+j]
            if nowstring[-1] == nowstring[-2]:
                answer += beforecount
            else:
                beforecount = beforecount + complexity[nowstring[-2:]]
                answer += beforecount

    return answer % (int(1e9+7))
