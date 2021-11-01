def solution(records, k, date):
    answer = []
    new_records = []

    year = int(date[0:4])
    month = int(date[6:7])
    day = int(date[9:10])
    print(year, month, day)


    # 그 달에서 쇼부볼 수 있는지
    # 그 해에서 쇼부 볼 수 있는지

    # 연도 기준으로 며칠째인지 계산한 다음에 빼는게 좋을듯
    countdays = (month * 30) + day

    if countdays < k: # 해당 연도에서 쇼부볼 수 있다
        month -= k // 30
        day =


    # # 범위에 해당하는 날짜 구하기 => 월 구하기
    # if int(date[-2:]) >= k:
    #     startdate = int(date[-2:])-k+1
    #     finishdate = int(date[-2:])
    #
    #
    # else:
    #     startdate = 30 - (k - int(date[-2:])) + 1
    #     finishdate = int(date[-2:])
    #
    # for i in range(len(records)):
    #     if records[i] ==



    return answer

records = ["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3", "2020-03-06 uid1 pid4"]
k = 10
date = "2020-03-05"
print(solution(records, k, date))