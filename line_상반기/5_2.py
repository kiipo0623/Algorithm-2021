from collections import deque
maxscore = 0
# turn 0 : 상대 1: 나
def dfs(ateam, myteam, cnt, prior, queue):
    global maxscore
    print(cnt, queue)
    if cnt == 0:
        maxscore = max(maxscore, myteam)
        return
    else:
        now1 = queue.popleft()
        now2 = queue.popleft()

        if prior>0: # 쓰는 경우
            dfs(ateam+now2, myteam + now1, cnt - 2, prior - 1, queue)
        dfs(ateam+now1, myteam+now2, cnt-2, prior, queue)

        queue.appendleft(now2)
        queue.appendleft(now1)


def solution(abilities, k):
    global maxscore
    person = len(abilities)
    if person %2 != 0:
        abilities.append(0)
        person += 1

    abilities.sort(reverse=True)
    abilities = deque(abilities)
    dfs(0, 0, person, k, abilities)
    return maxscore

# print(solution(
# [2, 8, 3, 6, 1, 9, 1, 9], 2
# ))
print(solution(
[7, 6, 8, 9, 10], 1
))