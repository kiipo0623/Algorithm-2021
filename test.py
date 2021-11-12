def solution(n, k, cmd):
    linked_list = {i : [i-1, i+1] for i in range(1, n+1)}
    OX = ["O" for i in range(1, n+1)]
    stack = []

    k += 1

    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = linked_list[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = linked_list[k][0]
        elif c[0] == 'C':
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            OX[k-1] = "X"
#
            if next == n+1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]
#
            if prev == 0:
                # prev가 0이라는 건.. 원래거가 첫번째였다는뜻
                # 이 경우에는 다음것만 정하면 된다
                linked_list[next][0] = prev
                # 마지막
            elif next == n+1:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev
        elif c[0] == 'Z':
            prev, next, now = stack.pop()
            OX[now-1] = "O"

            if prev == 0:
                linked_list[next][0] = now
            elif next == n+1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return ''.join(OX)


# 실제로 없는 건 없애는 게 제일 낫다 ( 어떠한 방법으로 리스트를 써서 표시하기보다)
# 링크드 리스트를 구현하는 방법
# 뭔가 효율성 테스트 있으면 우선 생각해볼것들이 힙과 링크드리스

print(solution(20, 15, ["C", "U 4", "U 5", "Z", "C", "C", "C", "C", "C", "Z"]))