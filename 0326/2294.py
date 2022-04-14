import sys
input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0
coin = []
INF = 10001
dp = [INF]*(k+1)

for _ in range(n):
    now = int(input())
    coin.append(now)

dp[0] = 0

for i in range(1, k+1):
    for c in coin:
        if i-c>=0:
            dp[i] = min(dp[i-c]+1, dp[i])
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
