from collections import defaultdict
def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    check_remote = [True] * len(employees)
    team_count = [0 for _ in range(num_teams+1)] # 0번은 없음! 출근 몇명하는지 카운트
    team_dict = defaultdict(list)

    print(team_count)

    office_set = set(office_tasks)
    for idx, employee in enumerate(employees):
        employee = employee.split()
        employee_team = int(employee[0])
        team_dict[employee_team].append(idx)
        employee_set = set(employee[1:])

        if office_set&employee_set: # 출근 당첨
            check_remote[idx] = False
            team_count[employee_team]+=1

    print(team_dict)
    print(check_remote)

    for idx, team in enumerate(team_count[1:]):
        if team == 0:
            person = sorted(team_dict[idx+1])
            check_remote[person[0]] = False
            team_count[idx] += 1

    for idx, c in enumerate(check_remote):
        if c:
            answer.append(idx+1)

    return answer

print(solution(
    3,
["development","marketing","hometask"],
["recruitment","education","officetask"],
["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]
))