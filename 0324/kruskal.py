graph = [[1, 0, 1],
         [2, 0, 2],
         [1, 1, 2],
         [5, 1, 3],
         [8, 2, 3]]
# cost node1 node2 순
N = 4 # node 수
V = 5 # edge 수
parents = [0] * N

def findparent(a):
    global parents
    if parents[a] == a:
        return a
    else:
        return findparent(parents[a])

def find(a, b):
    a_parent = findparent(a)
    b_parent = findparent(b)
    if a_parent == b_parent:
        return True
    else:
        return False

def union(a, b):
    # 부모 노드 번호가 더 적은 쪽으로 합침
    a_parent = findparent(a)
    b_parent = findparent(b)
    if a_parent < b_parent: parents[b] = a_parent
    else: parents[a] = b_parent

def kruskal():
    answer = 0
    include_edges = []
    global N, V, graph, parents

    for i in range(len(parents)):
        parents[i] = i # 부모 자기자신 초기화

    graph.sort() # 첫 번째가 cost이기 때문에 cost순서대로 sort된다

    for i in range(V):
        cost, start, end = graph[i]
        if find(start, end): # 부모 노드가 같으면
            continue
        else: # 부모 노드가 다르면 : union
            union(start, end)
            answer += cost
            include_edges.append((start, end))
    print(include_edges)
    return answer

print(kruskal())
