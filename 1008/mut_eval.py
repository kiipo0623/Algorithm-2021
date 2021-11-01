# 상호평가
# 프로그래머스 위클리 챌린지 2주차
# 4:32 - 5:00
# 일단 문제 제대로 안읽음 : 자체평가가 최고/최저인 경우인데 그냥 최고/최저로 함
# 코드 잘못 짬 : 같은 점수가 없으면 > 있으면 으로 ㅅㅂ
# 길을 잃음. . 다시 풀기
def solution(scores):
    answer = ''
    check = []
    grades = []

    for i in range(len(scores)):
        temp = scores[i]
        for j in range(len(scores)):
            # 유일성 점검 : 가로가 아니라 세로로 해야 함
            if i==j and (temp[j] == max(temp) or temp[j] == min(temp)):
                check.append(temp[i])
            else:
                check.append(0)

        print(scores)

    for i in range(len(scores)):
        deno = len(scores)
        sum_ = 0
        flag = False
        for j in range(len(scores)):
            # 세로로 검색해서 포함되는 지 확인. 포함 안되면 여기서 더해줘야 되는데 ..
            if check[i] == scores[j][i] and i!=j:
                flag = True


        grade = sum_/deno
        print("sum", sum_)
        print("deno", deno)

        if grade >= 90:
            grades.append("A")
        elif grade >= 80:
            grades.append("B")
        elif grade >= 70:
            grades.append("C")
        elif grade >= 50:
            grades.append("D")
        else:
            grades.append("F")

    return ''.join(grades)

print(solution([[70,49,90],[68,50,38],[73,31,100]]))