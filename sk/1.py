def solution(money, costs):
    costmoney = [1,5,10,50,100,500]
    dictionary = dict(zip(costmoney, costs))
    INF = int(1e9)
    min_cost = [INF] * (money+1)
    min_cost[0] = 0

    for i in range(1, money+1):
        for cm in costmoney:
            if i >= cm and i%cm == 0:
                min_cost[i] = min(min_cost[i], min_cost[i-cm]+dictionary[cm])

    return min_cost[money]