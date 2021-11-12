# 표 편집
# 2:23 -
# 시간 초과가 뜨는건 알겠는데 논리에 맞춰서 코딩을 헀으면 시간 안에 풀 수 있는건 분명히 맞아야 되는데 왜 틀리는건지

def solution(n, k, cmd):
    temp = [True] * n
    ptr = k
    last = []
    updown = 0

    for c in cmd:
        if c[0] == "U":
            updown -= int(c[2:])

        elif c[0] == "D":
            updown += int(c[2:])

        elif c[0] == "C":
            if updown > 0:  # down해야 하는 거임
                while updown > 0:
                    ptr += 1
                    if temp[ptr] == True:
                        updown -= 1

                while temp[ptr] == False:
                    ptr += 1

            elif updown < 0:  # up해야 하는 거임
                while updown < 0:
                    ptr -= 1
                    if temp[ptr] == True:
                        updown += 1
                while temp[ptr] == False:
                    ptr -= 1

            last.append(ptr)
            temp[ptr] = False

            # n-1만 마지막이 아님 ! 1번쨰라도 밑에 다 false면 그거임
            check = False
            for i in range(ptr + 1, n):
                if temp[i] == True:
                    check = True
                    break

            if ptr == n - 1 or check == False:
                ptr -= 1
                while temp[ptr] == False:
                    ptr -= 1

            else:
                ptr += 1
                while temp[ptr] == False:
                    ptr += 1

        elif c[0] == "Z":
            now = last.pop()
            temp[now] = True


    answer = ''
    for t in temp:
        if t == True:
            answer += 'O'
        else:
            answer += 'X'
    return answer


print(solution(20, 15, ["C", "U 4", "U 5", "Z", "C", "C", "C", "C", "C", "Z"]))