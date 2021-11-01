# 2020 카카오 인턴십
# 수식 최대화
# 10:37 - 11:11
# 11:30 -

# 연산자를 어떻게 취급할 수 있는지
import copy

def solution(expression):
    answer = 0
    operator = ["+", "-", "*"]
    maximum = -1
    exp = []

    # operator 중에 안쓰는 게 있는지 확인 : 특수성 없애기 위해서 추후 삭제
    for i in range(3):
        if operator[i] not in expression:
            operator.pop(i)

    # 수식을 list로
    temp = []
    for i in range(len(expression)):
        if expression[i] != "+" and expression[i] != "-" and expression[i] != "*":
            temp.append(expression[i])
        else:
            exp.append(int(''.join(temp)))
            exp.append(expression[i])
            temp = []

    if temp:
        exp.append(int(''.join(temp)))

    print("exp", exp)

# 걍 플마곱 따로 짜는 게 나을지 ?
    # 플러스 첫빠따
    plus_ = copy.deepcopy(exp)
    for i, o in enumerate(exp):
        if o == "+":
            temp = plus_[i-1]+plus_[i+1]
            plus_[i] = temp
            plus_.pop(i-1)
            plus_.pop(i)

    print("plus", plus_)

    plus_minus_ = copy.deepcopy(plus_)
    print("pm", plus_minus_)
    for i, o in enumerate(plus_):
        if o == "-":
            temp = plus_minus_[i-1]-plus_minus_[i+1]
            plus_minus_[i] = temp
            plus_minus_.pop(i-1)
            plus_minus_.pop(i)

    print("pm", plus_minus_)

    plus_multi_ = copy.deepcopy(plus_)
    for i, o in enumerate(plus_):
        if o == "*":
            temp = plus_multi_[i-1]*plus_multi_[i+1]
            plus_multi_[i] = temp
            plus_multi_.pop(i-1)
            plus_multi_.pop(i)
    print("mul", plus_multi_)








    return answer

print(solution("100-200*300-500+20"))