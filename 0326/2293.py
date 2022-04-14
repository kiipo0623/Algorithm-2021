import sys
input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for i in coin:
    for j in range(i, k+1):
        if j-i>=0:
            dp[j] += dp[j-i]

print(dp[k])
