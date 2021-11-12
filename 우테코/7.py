def solution(grid, clockwise):
    answer = []
    answerstr = []

    n = len(grid)
    rowchange = []
    colchange = []

    # 행
    for i in range(1, n):
        for j in range(i):
            rowchange.append(n-i)

    for i in range(n):
        rowchange.append(0)

    for i in range(n-1, 0, -1):
        for j in range(i):
            rowchange.append(-(n-i))

    # 열
    for i in range(n):
        for j in range(i, 0, -1):
            colchange.append(j*2)

        colchange.append(0)

        for j in range(1, i+1, 1):
            colchange.append(-j*2)

    count = 0
    for rowidx in range(len(grid)):
        for colidx in range(len(grid[rowidx])):
            answer.append(grid[rowidx+rowchange[count]][colidx+colchange[count]])
            count += 1

    for i in range(n):
        temp = ""
        for j in range((i*2)+1):
            temp += answer[i+j]
        answerstr.append(temp)


    return answerstr

print(solution(
["A","MAN","DRINK","WATER11"], False
))