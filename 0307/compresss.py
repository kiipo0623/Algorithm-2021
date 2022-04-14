for i in range(len(imos)): # 가로
    now = 0
    for j in range(len(imos[0])): # 세로
            now += imos[i][j]
            imos[i][j] = now

    for i in range(len(imos[0])):
        now = 0
        for j in range(len(imos)):
            now += imos[j][i]
            imos[j][i] = now
