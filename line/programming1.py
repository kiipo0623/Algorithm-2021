def solution(student, k):
    answer = 0

    if student.count(1) < k:
        return 0
    senior_list = list(filter(lambda x: student[x] == 1, range(len(student))))

    for i in range(len(senior_list)):
        if len(senior_list) - i < k:
            break
        else:
            answer += countstudent(student, senior_list[i], senior_list[i+k-1])

    return answer

def countstudent(student, start, finish):
    answer = 0
    answer += 1  # 자기 자신으로 구성

    # 앞으로
    tempfront = start - 1
    if start != 0:
        while tempfront != -1 and student[tempfront] != 1:
            tempfront -= 1
        tempfront += 1  # 반복문에서 자꾸 더해지는 문
        answer += start - tempfront

    # 뒤
    tempback = finish + 1
    if finish != len(student) - 1:
        while tempback != len(student) and student[tempback] != 1:
            tempback += 1
        tempback -= 1
        answer += tempback - finish

    # 앞뒤
    answer += (start - tempfront) * (tempback - finish)
    return answer


print(solution([0, 1, 0, 0, 1, 1, 0], 2))