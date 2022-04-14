graph = [[1, 0, 1],
         [2, 0, 2],
         [1, 1, 2],
         [5, 1, 3],
         [8, 2, 3]]
# cost node1 node2 순
N = 4 # node 수
V = 5 # edge 수

def prim(start):
    global graph, N, V
    list2D = [[0]*(N) for _ in range(N)]
    answer = 0

    for i in range(len(graph)): # 이차원 리스트로 만들기
        list2D[graph[i][1]][graph[i][2]] = graph[i][0]
        list2D[graph[i][2]][graph[i][1]] = graph[i][0]

    # visit와 unvisit 초기화
    visited = []
    unvisited = []

    visited.append(start)
    for i in range(N):
        if i not in visited:
            unvisited.append(i)

    for i in range(1, N): # 전체 노드 수
        min = int(1e9)
        min_index = 0
        for j in range(i): # visit 노드 탐색
            for k in range(N-i): # unvisit 노드 탐색
                # 연결되어 있고, 거리가 최소라면
                if (list2D[visited[j]][unvisited[k]] > 0 and min > list2D[visited[j]][unvisited[k]]):
                    min = list2D[visited[j]][unvisited[k]]
                    min_index = k
        visited.append(unvisited[min_index])
        unvisited.remove(unvisited[min_index])
        answer += min
    return answer

print(prim(0))