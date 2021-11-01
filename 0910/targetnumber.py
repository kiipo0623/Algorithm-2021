from collections import deque

def solution(numbers, target):
    graph = [numbers[0]]
    


def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()

        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
