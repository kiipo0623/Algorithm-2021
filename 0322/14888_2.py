from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

maxvalue = -int(1e9)
minvalue = int(1e9)

def dfs(depth, total, plus, minus, multiply, divide):
    global minvalue, maxvalue
    if depth == n:
        maxvalue = max(maxvalue, total)
        minvalue = min(minvalue, total)
        return

    if plus:
        dfs(depth + 1, total + numbers[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-numbers[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*numbers[depth], plus, minus, multiply-1, divide)
    if divide:
        if total < 0:
            temp = -(-total//numbers[depth])
        else:
            temp = total // numbers[depth]
        dfs(depth+1, temp, plus, minus, multiply, divide-1)


dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])
print(maxvalue)
print(minvalue)