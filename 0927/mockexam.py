def solution(answers):
    answer = []
    n = len(answers)
    student1 = [1, 2, 3, 4, 5] * (n//5 + 1)
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * (n//8 + 1)
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (n//10 + 1)

    score1 = [0,1]
    score2 = [0,2]
    score3 = [0,3]

    for k, a, b, c in zip(answers, student1[:n], student2[:n], student3[:n]):
        if k == a:
            score1[0] += 1
        if k == b:
            score2[0] += 1
        if k == c:
            score3[0] += 1

    best = max(score1[0], score2[0], score3[0])

    for item in [score1, score2, score3]:
        if item[0] == best:
            answer.append(item[1])


    return answer



print(solution([1,2,3,4,5]))