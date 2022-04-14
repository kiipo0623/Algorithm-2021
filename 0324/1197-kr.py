import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = []
parents = [i for i in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

def find_parents(x):
    global parents
    if parents[x] == x:
        return x
    else:
        return find_parents(parents[x])

def parents_check(a, b):
    par_a = find_parents(a)
    par_b = find_parents(b)
    if par_a == par_b: return True
    else: return False

def union_parents(a, b):
    global parents
    par_a = find_parents(a)
    par_b = find_parents(b)
    if par_a < par_b: parents[b] = par_a # 절댓값 더 작은 쪽으로
    else: parents[a] = par_b

def kruskal():
    answer = 0
    graph.sort(key = lambda x : (x[2]))

    for edge in graph:
        a, b, cost = edge
        if parents_check(a, b): # 두개 부모 같음
            continue
        else: # 두개 부모 다름
            union_parents(a, b)
            answer += cost
    return answer

print(kruskal())

