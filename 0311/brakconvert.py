def balance(p):
    counter = 0
    answer = ''
    for string in p:
        if string == '(':
            counter += 1
            answer += string
        elif string == ')':
            counter -= 1
            answer += string
        if counter == 0:
            break
    return answer

def correct(p):
    stack = []
    success = True
    for string in p:
        if string == '(':
            stack.append('(')

        elif string == ')':
            if stack:
                stack.pop()
            else:
                success = False
                break

    return success

def reversing(p):
    answer = ''
    for string in p:
        if string == '(':
            answer += ')'
        else:
            answer += '('
    return answer

def process(p):
    # 1단계 : 빈 문자열
    if len(p) == 0:
        return p

    # 2단계 : u, v 분리
    u = balance(p)
    v = p[len(u):]

    # 3단계 : 올바른 괄호 문자열 확인
    if correct(u):
        return u + process(v)

    # 4단계 : 올바르게 만들기
    empty = '('
    empty += process(v)
    empty += ')'
    empty += reversing(u[1:-1])
    return empty


def solution(p):
    return process(p)

print(solution(
"(()())()"
))