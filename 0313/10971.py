n = int(input())
arr = []

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

def tsp(D):
    N = len(D)
    INF = int(1e9)
    cache = [[None] * (1<<N) for _ in range(N)]
    VISITED_ALL = (1<<N)-1

    def find_path(last, visited):
        if visited == VISITED_ALL:
            return D[last][0] or INF

        if cache[last][visited] is not None:
            return cache[last][visited]

        tmp = INF
        for city in range(N):
            if visited&(1<<city) == 0 and D[last][city] != 0:
                tmp = min(tmp, find_path(city, visited|(1<<city)) + D[last][city])
        cache[last][visited] = tmp
        return tmp

    return find_path(0, 1<<0)

print(tsp(arr))
