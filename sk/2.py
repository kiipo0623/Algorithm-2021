def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    if clockwise == True: # 시계방향
        drow = [0,1,0,-1] # 오른쪽 아래쪽 왼쪽 위쪽
        dcol = [1,0,-1,0]
        start = [[0, 0], [0, n - 1], [n - 1, n - 1], [n - 1, 0]]

    if clockwise == False:
        drow = [1,0,-1,0]
        dcol = [0,1,0,-1]
        start = [[0, 0], [n-1, 0], [n-1, n-1], [0, n-1]]


    for idx, s in enumerate(start):  # 시작점 반복문
        row, col = s
        counter = 0  # 입력 값
        direction = idx
        turn = n+1
        row = row - drow[direction % 4]
        col = col - dcol[direction % 4]
        direction -= 1

        while turn > 0:  # 종료 조건=몇칸남기면 돌려야되는데 더이상 돌릴 수 없을때
            turn -= 2
            direction += 1


            for i in range(turn):
                counter += 1
                nrow = row + drow[direction % 4]
                ncol = col + dcol[direction % 4]
                answer[nrow][ncol] = counter
                row, col = nrow, ncol

    if n%2 == 1: # 홀수인 경우
        answer[n//2][n//2] = answer[n//2+1][n//2]+1


    return answer