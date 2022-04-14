
def Daum(N, M):
    n = str(N)
    res = 0
    for i in n:
        res += pow(int(i), M)
    return res

def DFS(N, M, iteration, check):
    # 이미 한 번 계산 됐다면, 이제 반복된다고 판단
    if check[N] != 0:
        return check[N] - 1 # 여기까지 리턴

    check[N] = iteration # 몇번째인지
    daum = Daum(N, M)
    iteration += 1
    return DFS(daum, M, iteration, check)

def DFS_ITR(N, M, iteration, check):
    stack = [N]
    while stack: # 방문한 적이 없는 경
        now = stack.pop()

        if check[now] != 0:
            return check[now] - 1

        check[now] = iteration
        daum = Daum(now, M)
        stack.append(daum)
        iteration += 1


# N : 처음 값 M : 몇제곱
N, M = map(int, input().split())

check = [0] * 236197 # 전체 리스트를 미리 만들어둠
iteration = 1

print(DFS_ITR(N, M, iteration, check))