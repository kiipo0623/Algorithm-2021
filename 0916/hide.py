import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque()
queue.append([0, [n]])

def bfs():
    while queue:
        temp = queue.popleft()
        depth = temp[0]
        walk = temp[1]
        templist = []

        for item in walk:
            if item-1>=0:
                templist.append(item-1)
            if item+1<=100000:
                templist.append(item+1)
            if item*2<=100000:
                templist.append(item*2)

        if k in templist:
            return [depth + 1, templist.count(k)]

        queue.append([depth+1, list(set(templist))])

if n==k:
    print(0)
    print(1)
else:
    asdf = bfs()
    print(asdf[0])
    print(asdf[1])




