import sys
input = sys.stdin.readline

x = int(input())
stack = []

for _ in range(x):
    now = input().split()
    if len(now)>1:
        stack.append(now[1])
    elif now[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    elif now[0] == 'size':
        print(len(stack))
    elif now[0] == 'pop':
        if len(stack):
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif now[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
