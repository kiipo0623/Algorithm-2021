from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))
# idx0 덧셈 idx1 뺄셈 idx2 곱셈 idx3 나눗셈
op = []
for i in range(len(operator)):
    op.extend([i]*operator[i])

check = list(permutations(op, (n-1)))
maxim, minim = -int(1e9), int(1e9)

for c in check:
    answer = numbers[0]
    for i in range(1, n):
        if c[i-1] == 0: # 덧
            answer += numbers[i]
        elif c[i-1] == 1: # 뺄
            answer -= numbers[i]
        elif c[i-1] == 2: # 곱
            answer *= numbers[i]
        elif c[i-1] == 3: # 나
            if answer < 0:
                answer = -(-answer // numbers[i])
            else:
                answer = answer // numbers[i]

    if answer > maxim: maxim = answer
    if answer < minim: minim = answer

print(maxim)
print(minim)

