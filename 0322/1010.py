from itertools import combinations
import sys

input = sys.stdin.readline

t = int(input())

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

for _ in range(t):
    n, m = map(int, input().split())
    print(int(factorial(m) / (factorial(n) * factorial(m-n))))