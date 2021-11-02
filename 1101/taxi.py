def solution(n, s, a, b, fares):
    graph = [[100001]*(n+1) for _ in range(n+1)]
    # 초기값을 100001에서 inf로 바꾸니까 정답이 됐다.. 왜 ?
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    for start, end, fare in fares:
        graph[start][end] = fare
        graph[end][start] = fare

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    # graph 플로이드 워셜로 구하는 부분까지는 문제 없음
    print(graph)
    answer = graph[s][a] + graph[s][b]

    # i번까지 합승한다고 가정
    for i in range(1, n+1):
        temp = graph[s][i] + graph[i][a] + graph[i][b]
        if temp < answer:
            answer = temp
    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
               ))