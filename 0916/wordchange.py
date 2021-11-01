from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    # 딕셔너리 구
    graph = dict()

    graph[begin] = []
    graph[target] = []

    for word in words:
        graph[word] = []

    print("그래프",graph)

    for word in words:
        for i in range(len(begin)):
            if begin[:i] + begin[i + 1:] == word[:i] + word[i + 1:]:
                graph[begin].append(word)

    for word in words:
        for i in range(len(target)):
            if target[:i] + target[i + 1:] == word[:i] + word[i + 1:]:
                graph[target].append(word)

    for word_standard in words:
        for word in words:
            for i in range(len(word_standard)):
               if word_standard[:i] + word_standard[i+1:] == word[:i] + word[i+1:]:
                    graph[word_standard].append(word)

    for item in graph:
        graph[item] = list(set(graph[item]))

    print(graph)

    depth = 1
    queue = deque()
    queue.append([depth, [begin]])

    while queue:
        temp = queue.popleft()
        tempdepth = temp[0]
        tempword = temp[1]
        templist = []

        for bigword in tempword:
            for smallword in graph[bigword]:
                if smallword == target:
                    return tempdepth

                templist.append(smallword)

        tempdepth += 1
        queue.append([tempdepth, templist])

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));