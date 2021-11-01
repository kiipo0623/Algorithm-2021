from collections import deque

def solution(tickets):
    answer = []
    send = []
    for ticket in tickets:
        a_sub_b = [x for x in tickets if x not in ticket]
        if ticket[0] == "ICN":
            send.append([ticket, a_sub_b])
    print(send)

    bfs(tickets, send)
    return answer

# 출발지 도착지 없이 리스트 통채로 넣기
def bfs(tickets, root):
    visited = []
    queue = deque()
    queue.append(root)

    while queue:
        print(queue.popleft())
        nowticket, leftticket = queue.popleft()
        templist = []
        for ticket in leftticket:
            a_sub_b = [x for x in leftticket if x not in ticket]
            if nowticket[1] == ticket[0]: # 중복 방문 가능하다는 점에서 수정 필요
                templist.append([ticket, a_sub_b])

        queue.append(templist)

        answer = []
        for visit in visited:
            answer.append(visit[0])

    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))