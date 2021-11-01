def solution(name):
    answer = 0
    # 커서 방향 결정
    joystick = [True] * len(name)

    for i in range(len(name)):
        if name[i] == 'A':
            joystick[i] = False

    cursor = 0

    while any(joystick):
        # 앞에 False가 많은지 뒤에 False가 많은지
        go, back = 0, 0

        temp = cursor + 1
        while True: # 순방향
            if temp == -1:
                temp = len(name)-1
            if temp == len(name):
                temp = 0

            if joystick[temp] == False:
                go += 1
                temp += 1
            else:
                break

        temp = cursor - 1
        while True:  # 역방향
            if temp == -1:
                temp = len(name) - 1
            if temp == len(name):
                temp = 0

            if joystick[temp] == False:
                back += 1
                temp -= 1
            else:
                break

        if go <= back: # 순방향
            joystick[cursor] = False
            answer += 1
            answer += ascii(name[cursor])
            cursor += 1
            if cursor == len(name):
                cursor = 0

        else: # 역방향
            joystick[cursor] = False
            answer += 1

            answer += ascii(name[cursor])

            cursor -= 1
            if cursor == -1:
                cursor = len(name)-1

    return answer - 1


def ascii(character):
    if character <= 'M':
        return ord(character) - ord('A')
    else:
        return ord('Z') - ord(character) + 1

print(solution("BABAAAAB"))

