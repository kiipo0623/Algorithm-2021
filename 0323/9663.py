n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False

def n_queens(x): # x 는 row를 의미
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            row[x] = i # [x,i]에 퀸을 놓겠다
            if is_promising(x): # 거기 놔두 되면
                n_queens(x+1)


n_queens(0)
print(ans)