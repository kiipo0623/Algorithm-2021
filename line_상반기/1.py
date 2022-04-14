def solution(logs):
    answer = 0 # 통과한 놈들
    search = ['team_name', 'application_name', 'error_level', 'message']
    for log in logs:
        flag = False
        if len(log) >100: # 길이 초
            continue
        while ' ' in log:
           log = log.replace(' ', '0')
        if log.count('0') != 11: # 공백 확
            continue
        log_split = log.split('0')
        if len(log_split) != 12:
            continue
        for i in range(len(log_split)):
            if i%3==0:
                if log_split[i] != search[int(i/3)]:
                    flag = True
                    break
            if i%3==1:
                if log_split[i] != ':':
                    flag = True
                    break
            if i%3==2:
                if not log_split[i].isalpha():
                    flag = True
                    break
        # 통과 한
        if flag == False:
            answer += 1

    return len(logs) - answer

print(solution([
"team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"
]))
#
# print(solution(
# ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
# ))

# print(solution(
# ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
# ))


