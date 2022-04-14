import sys
input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))

front = 0
back = 1
min_length = N+1
sum = array[front]

while True: # front를 더 늘릴 수 있다
    if sum < S:
        if back == N:
            break
        sum += array[back]
        back += 1


    elif sum >= S:
        if back-front < min_length:
            min_length = back-front
        sum -= array[front]
        front += 1

if min_length == N+1:
    print(0)
else:
    print(min_length)