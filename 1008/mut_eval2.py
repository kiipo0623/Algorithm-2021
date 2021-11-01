# 프로그래머스 코딩테스트 연습 위클리챌린지
# 상호평가
# 10:18-10:32

def solution(scores):
    student = len(scores)
    grade = []

    for i in range(student):
        temp = []
        for j in range(student):
            temp.append(scores[j][i])
            if i == j:
                self = scores[j][i]

        if (max(temp) == self or min(temp) == self) and temp.count(self) == 1:
            temp[i] = 0
            sum_ = sum(temp) / (student-1)
        else:
            sum_ = sum(temp) / student


        if sum_ >= 90:
            grade.append('A')
        elif sum_ >= 80:
            grade.append('B')
        elif sum_ >= 70:
            grade.append('C')
        elif sum_ >= 50:
            grade.append('D')
        else:
            grade.append('F')

    return ''.join(grade)


print(solution([[70,49,90],[68,50,38],[73,31,100]]))