import sys
from collections import defaultdict

cpunum = int(sys.stdin.readline())
networknum = int(sys.stdin.readline())

network = defaultdict(list)

for i in range(networknum):
    temp = list(map(int, sys.stdin.readline().split()))
    network[temp[0]].append(temp[1])
    network[temp[1]].append(temp[0])

stack = [1]
visited = []

while stack:
    temp = stack.pop()

    if temp not in visited:
        visited.append(temp)

        for item in network[temp]:
            if item not in visited:
                stack.append(item)

print(len(visited)-1)