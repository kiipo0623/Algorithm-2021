# 가사 검색
# 5:13 - 5:52 효율성만 두개맞음 정확도 다틀림 대체왜 ?
# for문 조건을 잘못 작성했기 때문 : 깨달음 = 뭔가 완벽한 것 같은데 문제가 생긴다면 내가 무언가를 놓치고 있을 확률이 크다 하나씩 직접 디버깅해봐야 한다
# 효율이 필요할 때 : 이진 탐색 힙 트라이 자료구조

from collections import defaultdict

def solution(words, queries):
    answer = []
    head = {}
    tail = {}
    count = defaultdict(int)

    for i in range(ord('a'), ord('z')+1):
        head[chr(i)] = []
        tail[chr(i)] = []

    for word in words:
        head[word[0]].append(word)
        tail[word[-1]].append(word)
        count[len(word)] += 1

    for query in queries:
        querycount = 0
        n = len(query)
        if set(list(query)) == {'?'}:
            querycount = count[n]

        elif query[-1] == '?': # 끝에 와일드카드 = 앞이 정해짐 fro??
            for i in range(n):
                if query[i] == '?':
                    wildcard = i
                    break

            for w in head[query[0]]:
                if n == len(w) and w[:wildcard] == query[:wildcard]:
                    querycount += 1

        elif query[0] == '?': # 앞이 와일드카드 = 뒤가 정해짐 ??kao
            for i in range(n):
                if query[i] != '?':
                    wildcard = i
                    break

            for w in tail[query[-1]]:
                if n == len(w) and w[wildcard:] == query[wildcard:]:
                    querycount += 1

        answer.append(querycount)
    return answer

print(solution(
["frodo", "front", "frost", "frozen", "frame", "kakao"],
["???", "fro??", "????o", "fr???", "fro???", "pro?"]
))
