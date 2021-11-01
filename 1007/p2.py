def solution(n, m, x, y, queries):
    ans = 0
    count = 0
    asdf = 0
    row, col = 0, 0
    end = [(0,0), (n-1,0), (0,m-1), (n-1,m-1)]

    for dir, sqr in queries:
        if dir == 0:
            col -= sqr
        elif dir == 1:
            col += sqr
        elif dir == 2:
            row -= sqr
        elif dir == 3:
            row += sqr

    print(row, col)

    if col < 0:
        if n+col < x: # 넘어서 가는 경우
            count = n-x
        elif n+col > x:
            count = 0
        else:
            count = 1
    else:
        if col > x:
            count = n
        elif col < x:
            count = 0
        else:
            count = 1

    if row < 0:
        if n+row < y: # 넘어서 가는 경우
            asdf = n-y
        elif n+row > y:
            asdf = 0
        else:
            asdf = 1
    else:
        if row > y:
            asdf = n
        elif row < y:
            asdf = 0
        else:
            asdf = 1

    if (x, y) in end:
        ans = count * asdf
    elif x == 0 or x == n-1:
        ans = count
    elif y == 0 or y == m-1:
        ans = asdf
    else:
        if count == 1 and asdf == 1: ans = 1
        else: ans = 0

    return ans





print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))
