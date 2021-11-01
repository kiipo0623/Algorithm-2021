def solution(genres, plays):
    answer = []
    real = []
    music = dict()

    for i in range(len(genres)):
        if genres[i] in music:
            music[genres[i]].append((i, plays[i]))
        else:
            music[genres[i]] = [(i, plays[i])]

    print(music)

    for song in music:
        total = 0
        music[song].sort(key = lambda x:x[1], reverse=True)
        for i in range(len(music[song])):
            total += music[song][i][1]
        answer.append((song, total, len(music[song])))

    answer.sort(key = lambda x:x[1], reverse=True)

    for item in answer:
        if item[1] == 0:
            pass
        if item[2] == 1:
            real.append(music[item[0]][0][0])
        else:
            real.append(music[item[0]][0][0])
            real.append(music[item[0]][1][0])

    return real

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))