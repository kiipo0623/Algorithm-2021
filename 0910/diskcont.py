import heapq

def solution(jobs):
    time = 0
    spend = 0
    nanu = len(jobs)
    heapq.heapify(jobs)

    while len(jobs) > 0:
        candidate = []
        for job in jobs:
            req, run = job
            if req <= time:
                heapq.heappush(candidate, [run, req])

        if len(candidate) == 0:
            time += 1
        else:
            out = heapq.heappop(candidate)
            running, request = out
            time += running
            spend += time - request

            jobs.remove([request, running])

    return spend // nanu



print(solution([[0, 3], [1, 9], [2, 6]]))