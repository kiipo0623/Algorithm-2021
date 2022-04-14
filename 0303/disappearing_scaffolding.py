dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = 0, 0

def OOB(x, y):
    return x < 0 or x >= n or y <0 or y >= m

vis = [[0]*5 for _ in range(5)] # 사라진 발판 : 1인 경우 사라졌음
block = [[0]*5 for _ in range(5)] # 원래 발판 : 0인 경우 원래 없음

# 현재 상태에서 둘 다 최적의 플레이를 할 때 남은 이동 횟수
# 반환 값이 짝수 : 플레이어가 패배 홀수 : 플레이어가 승리
# curx, cury : 현재 좌표, opx, opy : 상대 좌표

def solve(curx, cury, opx, opy):
    global vis, block
    # 플레이어가 밟고 있는 발판이 사라졌다면 플레이어 패배(짝)
    if vis[curx][cury]:
        return 0

    ret = 0 # 반환 값 : 플레이어 패배수 그냥 default값 지정

    # 플레이어를 네 빙향으로 이동시켜 다음 단계 진행
    for dir in range(4):
        nx = curx + dx[dir]
        ny = cury + dy[dir]

        if OOB(nx, ny) or vis[nx][ny] or block[nx][ny] == 0: # 만약에 갈수 없는 곳이다 : return ret(0)
            continue
        vis[curx][cury] = 1 # 방문했던 곳 발판 없앰

        # val = 플레이어를 dir 방향으로 이동시켰을 때 턴의 수
        # 다음 함수를 호출할 때 opx, opy, nx, ny 순으로 호출
        val = solve(opx, opy, nx, ny) + 1 # 재귀로 빡 빢빢해서 이겼는지 졌는지 알수있음

        # 방문 표시 해제 : 또 새로운 반복문[평행세계]
        vis[curx][cury] = 0

        # 1. 현재 저장된 턴은 패배인데 새로 계산된 턴은 승리인 경우
        if ret % 2 == 0 and val % 2 == 1:
            ret = val
        # 2. 현재 저장된 턴과 새로 계산된 턴이 모두 패배인 경우
        elif ret % 2 == 0 and val % 2 == 0:
            ret = max(ret, val) # 최대한 늦게 지는 걸 선택
        # 3. 현재 저장된 턴과 새로 계산된 턴이 모두 승리인 경우
        elif ret % 2 == 1 and val % 2 == 1:
            ret = min(ret, val) # 최대한 빨리 이기는 걸 선택
    return ret

def solution(board, aloc, bloc):
    global n, m
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            block[i][j] = board[i][j]
    return solve(aloc[0], aloc[1], bloc[0], bloc[1])
