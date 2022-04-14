def changetime(start, end):
    starthour = start[:2]
    endhour = end[:2]
    startminute = start[3:]
    endminute = end[3:]

    starttime = int(starthour) * 60 + int(startminute)
    endtime = int(endhour) * 60 + int(endminute)

    return endtime - starttime


def changecode(code):
    code = ''.join(reversed(code))
    dict = {'A': 'a', 'B':'b', 'C':'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g'}
    answer = ''
    cnt = 0
    while cnt < len(code):
        if code[cnt] == '#':
            answer += dict[code[cnt+1]]
            cnt += 2
        else:
            answer += code[cnt]
            cnt += 1
    return ''.join(reversed(answer))


def solution(m, musicinfos):
    answer = '(None)'
    candidate = []
    m = changecode(m)
    for musicinfo in musicinfos:
        stime, etime, title, code = musicinfo.split(',')
        times = changetime(stime, etime)
        code = changecode(code)

        # 음악 길이를 time 길이에 맞춤
        q, r = divmod(times, len(code))
        music = code * q + code[:r]

        if m in music:
            candidate.append([title, music])

    max = 0 # 음악 제목 길
    for title, music in candidate:
        if len(music) > max:
            answer = title
            max = len(music)

    return answer

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	))