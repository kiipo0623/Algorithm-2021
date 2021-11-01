# 타겟 넘버
def solution(numbers, target):
    answer = 0
    array = [[0]]

    for number in numbers:
        temp = []
        arr = array[-1]
        for item in arr:
            temp.append(number + item)
            temp.append(item - number)
        array.append(temp)

    for item in array[-1]:
        if item == target:
            answer += 1

    return answer

print(solution([1,1,1,1,1], 3))

def solution(numbers, target):
    if not numbers and target == 0: # 남은 숫자가 없고 target이 0일때
        return 1
    elif not numbers: # 남은 숫자가 없을 때
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])