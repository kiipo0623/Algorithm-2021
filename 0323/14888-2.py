def array(depth, before, plus, minus, multiply, divide):
    global N, max_value, min_value
    if depth == N:
        max_value = max(max_value, before)
        min_value = min(min_value, before)
        return
    
    if plus:
        array(depth + 1, before + A[depth], plus - 1, minus, multiply, divide)
    if minus:
        array(depth + 1, before - A[depth], plus, minus - 1, multiply, divide)
    if multiply:
        array(depth + 1, before * A[depth], plus, minus, multiply - 1, divide)
    if divide:
        if before < 0:
            sol = -((-before)//A[depth])
        else:
            sol = before // A[depth]
        array(depth + 1, sol, plus, minus, multiply, divide-1)

import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
max_value, min_value = -(1e9), 1e9
array(1, A[0], plus, minus, mul, div)
print(max_value)
print(min_value)

