# 7:40 -
# 매 번 조건에 맞는지 확인해서 건설 하거나 건설 하지 않음
# 테케는 다맞고 19.2
def checkbo(x, y, do, snowtown):
    if do == 0:  # 삭제
        if [x, y, 0] in snowtown or [x + 1, y, 0] in snowtown:  # 위에 기둥 있는 경우
            return False
        elif [x - 1, y, 1] in snowtown and [x + 1, y, 1] in snowtown:  # 앞뒤로 보가 있는 경우
            if [x - 1, y, 1] in snowtown and [x - 1, y - 1, 0] not in snowtown and [x, y - 1, 0] not in snowtown:
                return False
            elif [x + 1, y, 1] in snowtown and [x + 1, y - 1, 0] not in snowtown and [x + 2, y - 1, 0] not in snowtown:
                return False
        return True


    elif do == 1:  # 추가
        if [x, y - 1, 0] in snowtown or [x + 1, y - 1, 0]:
            return True
        elif [x - 1, y, 1] in snowtown and [x + 1, y, 1] in snowtown:
            return True
        return False


def checkgidung(x, y, do, snowtown):
    if do == 0:  # 삭제
        if [x, y + 1, 0] in snowtown:  # 다른 기둥이 내 위에 있는 경우
            return False
        elif [x, y + 1, 1] in snowtown:  # 내 위에 보가 있는 경우
            if [x + 1, y, 0] not in snowtown and not ([x - 1, y + 1, 1] in snowtown and [x + 1, y + 1, 1] in snowtown):
                return False
        elif [x - 1, y + 1, 1] in snowtown:  # 내 위에 보가 있는 경우
            if [x - 1, y, 0] not in snowtown and not ([x - 2, y + 1, 1] in snowtown and [x, y + 1, 1] in snowtown):
                return False
        return True

    elif do == 1:  # 추가
        if y == 0:
            return True
        elif [x, y - 1, 0] in snowtown:
            return True
        elif [x, y, 1] in snowtown or [x - 1, y, 1] in snowtown:
            return True
        return False


def solution(n, build_frame):
    answer = []

    for build in build_frame:
        x, y, a, b = build
        if a == 0:
            sol = checkgidung(x, y, b, answer)
            if sol and b == 0:  # True면 동시에 삭제면
                answer.remove([x, y, a])
            elif sol and b == 1:
                answer.append([x, y, a])
        elif a == 1:
            sol = checkbo(x, y, b, answer)
            if sol and b == 0:
                answer.remove([x, y, a])
            elif sol and b == 1:
                answer.append([x, y, a])

    # sort : 첫번째 두번째 세번째 어떻게 하는지 기록
    answer.sort()

    return answer

# [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]