import collections
def solution(arrows):
    answer = 0
    move = [(-1, 0), (-1,1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0)

    visited = collections.defaultdict(int)
    visited_dir = collections.defaultdict(int)

    queue = collections.deque([now])
    for i in arrows:
        for _ in range(2):
            next = (now[0] + move[i][0], now[1] + move[i][1])
            queue.append(next)

            now = next

    now = queue.popleft()
    visited[now] = 1

    while queue:
        next = queue.popleft()

        if visited[next] == 1:
            if visited_dir[(now, next)] == 0:
                answer += 1
        else:
            visited[next] = 1

        visited_dir[(now, next)] = 1
        visited_dir[(next, now)] = 1
        now = next

    return answer

# 사방이 막힌걸 어떻게 알아내서 카운트하면 되는 문제
# 한 점이 두 번 방문되면 하나의 방이 만들어진 것
# 만약에 똑같은 곳을 반복해서 방문하게 된다면 ..? 똑같은 네모 두개는 결국 하나의 방인데

# 방문하는 점을 모두 리스트에 지정 해 두고,
# 그다음 그래프 사용해서 어떻게 카운트
# 기본이 dfs bfs
# 한 점 씩 붙잡고 도형 나올때까지 캐는거? 캐고나면 뭘 기준으로 삭제해야 하는지

# 반만 제대로 한것
# 똑같은 곳을 다시 반복/만들어지는 간선이 기존에 만들어진 적 없음
# 고려해야 하는 것 : 정수가 아닌 곳에서 교차 모래시계
