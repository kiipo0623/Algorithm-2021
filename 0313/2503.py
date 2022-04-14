from itertools import permutations

def solution(records):
    ans = 0

    def check(base1, record):
        base2, strike, ball = record
        base1, base2 = str(base1), str(base2)
        strike_count = sum(b1 == b2 for b1, b2 in zip(base1, base2))
        ball_count = len(set(base1)&set(base2)) - strike_count
        return (strike_count == strike) and (ball_count == ball)

    candidate = list(map(list, permutations([1,2,3,4,5,6,7,8,9], 3)))
    for cand in candidate:
        cand = 100*cand[0] + 10*cand[1] + cand[2]
        if all(check(cand, rc) for rc in records):
            ans += 1
    return ans

n = int(input())
rcd = []
for _ in range(n):
    rcd.append(list(map(int, input().split())))

print(solution(rcd))