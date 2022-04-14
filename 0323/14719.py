import sys
input = sys.stdin.readline

H, W = map(int, input().split())
world = list(map(int, input().split()))

answer = 0

for i in range(1, W-1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    lr = min(left_max, right_max)

    if world[i] < lr:
        answer += lr - world[i]

print(answer)