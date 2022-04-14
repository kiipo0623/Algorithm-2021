import sys
input = sys.stdin.readline

string = list(input().strip())
stack = []
answer = 0
temp = 1

for i in range(len(string)):
    if string[i] == '(':
        temp *= 2
        stack.append(string[i])

    elif string[i] == '[':
        temp *= 3
        stack.append(string[i])

    elif string[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if string[i-1] == '(':
            answer += temp
        temp //= 2 # 왜 if문 밖에서 하는건지 : 처리 완료 했으니까 관계 없이 정리해줘야 함
        stack.pop()

    elif string[i] == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if string[i-1] == '[':
            answer += temp
        temp //= 3
        stack.pop()

if stack:
    answer = 0

print(answer)