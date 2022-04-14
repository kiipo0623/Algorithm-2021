from collections import deque

def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for a, b in edges:
        tree[a].append(b)
    q = deque([1, 0, tuple([1]+[0]*(len(info))-1)])
    visited = set()

    while q:
        s, w, visit = q.popleft()
        if s == w:
            continue
        if (s, w, visit) in visited:
            continue
        visited.add((s, w, visit))

        for i in range(len(info)):
            if visit[i] == 1: # 이전에 방문했다면
                for j in tree[i]:
                    if not visit[j]: # 자식 노드가 방문하지 않았다면
                        temp = list(visit) # 튜플 값 변경하기 위해 리스트로
                        temp[j] = 1 # 튜플 값 변경
                        if info[j] == 0: #양
                            q.append((s+1, w, tuple(temp)))
                        else:
                            q.append((s, w+1, tuple(temp)))
    return max(visited)[0]
