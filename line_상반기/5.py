from collections import deque
maxscore = 0
# turn 0 : 상대 1: 나
def dfs(ateam, myteam, cnt, prior, queue, turn):
    global maxscore
    print("cnt, ", cnt, "queue", queue)
    if cnt == 0:
        maxscore = max(maxscore, myteam)
        return

    if turn == 0:
        now = queue.popleft()
        if prior>0:
            dfs(ateam, myteam+now, cnt-1, prior-1, queue, 0)
        dfs(ateam+now, myteam, cnt-1, prior, queue, 1)
        queue.appendleft(now)

    else:
        now = queue.popleft()
        dfs(ateam, myteam+now, cnt-1, prior, queue, 0)
        queue.appendleft(now)

def solution(abilities, k):
    global maxscore
    person = len(abilities)
    abilities.sort(reverse=True)
    abilities = deque(abilities)
    dfs(0, 0, person, k, abilities, 0)
    return maxscore

# print(solution(
# [2, 8, 3, 6, 1, 9, 1, 9], 2
# ))
print(solution(
[7, 6, 8, 9, 10], 1
))