def solution(student, k):
    answer = 0

    if student.count(1) < k:
        return 0

    # 한 개일 경우
    for i in range(len(student)):

        if student[i] == 1:
            answer += 1  # 자기 자신으로 구성


            #앞으로
            tempfront = i - 1
            if i != 0:
                while tempfront != -1 and student[tempfront] != 1:
                    tempfront -= 1
                tempfront += 1 # 반복문에서 자꾸 더해지는 문
                answer += i - tempfront


            #뒤
            tempback = i + 1
            if i != len(student)-1:
                while tempback != len(student) and student[tempback] != 1:
                    tempback += 1
                tempback -= 1
                answer += tempback - i

            #앞뒤
            answer += (i-tempfront) * (tempback - i)

    return answer

def countstudent(student, start, finish)


print(solution([0, 1, 0, 0, 1, 1, 0], 2))
