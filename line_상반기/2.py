from itertools import combinations

def countUpper(string):
    count = 0
    for i in range(len(string)):
        if string[i].isupper():
            count += 1
    return count

def solution(sentences, n):
    length = len(sentences)
    grade = [0] * length
    dictionary = [[] for _ in range(length)]
    idxlist = [i for i in range(length)]
    max_grade = 0

    for i in range(length):
        shift = False

        grade[i] = len(sentences[i])

        if not sentences[i].islower(): # 전부 소문자인지?
            shift = True
            grade[i] += countUpper(sentences[i])
            sentences[i] = sentences[i].lower()

        sentence_set = set(sentences[i].replace(' ',''))
        if shift:
            sentence_set.add("shift")
        dictionary[i] = list(sentence_set)


    for i in range(1, length):
        for combi in combinations(idxlist, i): # [1,2] 이런식
            new_set = set()
            new_grade = 0
            for index in combi:
                now = set(dictionary[index])
                new_set |= now
                new_grade += grade[index]
            if len(new_set) <= n and new_grade > max_grade:
                max_grade = new_grade

    return max_grade


print(solution(
["line in line", "LINE", "in lion"]	, 5
))