def solution(brown, yellow):
    g = 0
    s = 1

    while True:
        if yellow % s == 0:
            g = int(yellow / s)
        else:
            s += 1
            continue

        need = (g+2 + s+2)*2 - 4
        if need == brown:
            return [g+2, s+2]
        else:
            s += 1

print(solution(24, 24))

# 가로가 세로보다 큰 범위 내에서 테스트케이스가 나오겠지만
# 그것에 대한 처리는 없음
# 근데 뭐 .. 문제에서도 머 없으면 [0,0]을 return
# 이런게 없으니까



