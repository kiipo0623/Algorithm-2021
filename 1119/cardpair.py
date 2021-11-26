# 카드 짝 맞축
# 11:08ㅍ-
from collections import defaultdict
def checkrmove(rtarget, rnow, cnow, board):
    count = 1
    # target이 위에 있는 경우
    if rtarget < rnow:
        while rtarget < rnow:
            if board[rnow][cnow] == 0:
                pass
            else:
                count += 1
            rnow -= 1

    # target이 아래에 있는 경우
    elif rtarget > rnow:
        while rtarget > rnow:
            if board[rnow][cnow] == 0:
                pass
            else:
                count += 1
            rnow += 1
    # 같은 경우는 고려할 필요가 없다
    return count


def checkcmove(ctarget, rnow, cnow, board):
    count = 0
    if ctarget < cnow:
        while ctarget < cnow:
            if board[rnow][cnow] == 0:
                pass
            else:
                count += 1
            cnow -= 1

    elif ctarget > cnow:
        while ctarget > cnow:
            if board[rnow][cnow] == 0:
                pass
            else:
                count += 1
            cnow += 1
    return count


def solution(board, r, c):
    answer = 0
    rnow = r
    cnow = c
    carddict = defaultdict(list)

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                carddict[board[i][j]].append([i, j])

    # enter 처리
    answer += len(carddict) * 2

    for _ in range(len(carddict)):
        # 현재 커서가 있는 자리가 빈 카드가 아니라면
        if board[rnow][cnow] != 0:
            target = board[rnow][cnow]

            for which in carddict[target]:
                if which == [rnow, cnow]:
                    continue
                else:
                    rtarget, ctarget = which
        # 현재 커서가 있는 자리가 빈 카드라면 주변에서 가장 적은 이동으로 찾을 수 있는 곳으로 이동해야 한다
        # 여기서는 현재 위치(카드가 있는곳) 짝이 되는 카드의 위치를 제공
        else:
            moving = 100000
            target = 0

            for candidate in carddict:
                for card in carddict[candidate]:  # 카드가 두 개니까
                    movecount = 0
                    movecount += checkrmove(card[0], rnow, cnow, board)
                    movecount += checkcmove(card[1], rnow, cnow, board)

                    if movecount < moving:
                        moving = movecount
                        target = candidate
                        rtemp, ctemp = card[0], card[1]

            for card in carddict[candidate]:
                if [rtemp, ctemp] == card:
                    answer += moving
                    rnow, cnow = rtemp, ctemp
                else:
                    rtarget, ctarget = card[0], card[1]

        answer += checkrmove(rtarget, rnow, cnow, board)
        answer += checkcmove(ctarget, rnow, cnow, board)

        board[rnow][cnow] = 0
        rnow, cnow = rtarget, ctarget
        board[rnow][cnow] = 0

        del (carddict[target])

    return answer

print(solution(
[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0
))

print(solution(
[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1
))