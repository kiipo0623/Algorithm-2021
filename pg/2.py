def work(time, gold, upgrade, level):
    # 0레벨로 계속한다
    # 1레벨로 올린
    money = 0
    for i in range(level):
        # 업그레이드 비용, 광석 하나 소요 시간됨
        upgrademoney, onetime = upgrade[i]

        # 마지막 레벨 : 그걸로 계속 파면
        if i == level:
            money += (time // onetime) * gold

        # 레벨업을 위해 애써야
        else:
            needtime = (upgrademoney // gold) # 하나에 얼마나 시간 드는지
            if upgrademoney % gold != 0:
                needtime += 1

            money += (needtime // onetime) * gold # 그만큼 일한다
            
            if needtime % onetime != 0:
                money += gold

    return money



def solution(time, gold, upgrade):
    answer = -1
    for i in range(len(upgrade)):
        work(time, gold, upgrade[:i], i)

    return answer