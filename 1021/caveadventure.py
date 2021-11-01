# 동굴 탐험
# 3:44 - 4:14
# dfs와 위상정렬로 구현할 수 있을거라고 생각했는데,
# dfs로 구현할 수 없는 문제다. visited더라도 다시 방문할 수 있다.

from collections import deque, defaultdict

# 이 함수 자체가 target을 찾으려고 있는건데 target을 못찾음
# False인 경우에는 for문을 계속 돌게 된다 : queue를 도니까 !!
# 뭔가 이상하고 부족한 코드 ..
def find(now, target, can, cannot, graph):
    visit = []
    stack = [now]

    while stack:
        temp = stack.pop()

        if temp not in visit:
            visit.append(temp)

            if temp in can:
                idx = can.index(temp)
                del can[idx]
                del cannot[idx]

            for new in graph[temp]:
                if new not in visit and new not in cannot:
                    stack.append(new)

    return visit


# find에서 dfs로 target 찾을때까지만 돌고 여기서 방문한 모든 노드 다시 solution으로 가져와서 visited에 추가
# 만약에 방문했던 곳이면 queue에서 그냥 pop하고 먼저 방문해야 하는 곳이 있으면 queue에 다시 넣음
# 만약에 선방문해야 하는 곳이면 order에서 제거함

def solution(n, path, order):
    visited = set() # visited라는 set을 준비 : 어디 방문했는지 확인
    graph = defaultdict(list) # graph 정리

    for p in path: # 그래프 정리
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])

    first = [] #선 방문 정리
    second = []

    for o in order:
        first.append(o[0])
        second.append(o[1])

    # queue에 모든 노드 담아 두고, 타겟으로 함
    queue = deque([i for i in range(n)])
    now = 0 # 어디까지 이동했는지. 일종의 포인터

    while queue:
        temp = queue.popleft() # 하나씩 꺼내서
        leave = queue #

        if temp in second: # 먼저 방문해야 되는게 있으면 큐의 맨 뒤에 넣고 다음 것
            queue.append(temp)
            continue

        if temp in visited: # 이미 방문했다면 pop 한 채로 둠
            continue

        finding = find(now, temp, first, second, graph)
        now = finding[-1]

        for f in finding: # temp에 해당하는 걸 찾기 위한 여정
            visited.add(f)

        if leave == queue:
            break

    if len(visited) == n:
        return True
    else:
        return False

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))