def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]
    dp = [[0] * (m+1) for i in range(n+1)]
    dp[1][1] = 1

    for i in range(1, n+1): #세로
        for j in range(1, m+1): #가로
            if i == 1 and j == 1:
                continue
            if [i,j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n][m] % 100000007



print(solution(4, 3,[[2, 2]] ))
