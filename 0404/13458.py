import sys
input = sys.stdin.readline

count = 0
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

for student in A:
    count += 1
    if student <= B:
        continue
    else:
        n, q = divmod(student-B, C)
        if q == 0:
            count += n
        else:
            count += n+1

print(count)