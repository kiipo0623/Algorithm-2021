from collections import defaultdict


def solution(req_id, req_info):
    answer = []
    person_dict = defaultdict(list)  # 골드 실버
    sell_queue = []
    buy_queue = []

    for id in req_id:
        person_dict[id] = [0, 0]

    for i in range(len(req_id)):
        now_id = req_id[i]
        now_do, now_amount, now_price = req_info[i]
        now_idx = i
        flag = False
        if now_do == 0:  # 구매 요청
            while now_amount and sell_queue:
                for index, sell in enumerate(sell_queue):
                    sell_id, sell_amount, sell_price, sell_idx = sell
                    del sell_queue[index]
                    if sell_price <= now_price:  # 가격 맞는 경우
                        amount = min(now_amount, sell_amount)
                        person_dict[now_id][0] -= amount * sell_price  # 사려는 애 실버
                        person_dict[now_id][1] += amount
                        person_dict[sell_id][0] += amount * sell_price  # 파는 애골드
                        person_dict[sell_id][1] -= amount

                        if sell_amount - amount > 0:
                            sell_queue.append([sell_id, sell_amount - amount, sell_price, sell_idx])

                        if now_amount - amount > 0:
                            buy_queue.append([now_id, now_amount - amount, now_price, now_idx])
                        now_amount -= amount
                        flag = True
            if flag == False:          # 가격 안맞는 경우
                buy_queue.append([now_id, now_amount, now_price, now_idx])
            else:
                flag = False

            sell_queue = sorted(sell_queue, key=lambda x: (x[2], x[3]))
            buy_queue = sorted(buy_queue, key=lambda x: (x[2], x[3]))

        elif now_do == 1:  # 판 요청
            while now_amount and buy_queue:
                for index, buy in enumerate(buy_queue):
                    buy_id, buy_amount, buy_price, buy_idx = buy
                    del buy_queue[index]
                    if buy_price <= now_price:  # 가격 맞는 경우
                        amount = min(now_amount, buy_amount)
                        person_dict[now_id][0] -= amount * buy_price  # 사려는 애 실버
                        person_dict[now_id][1] += amount
                        person_dict[buy_id][0] += amount * buy_price  # 파는 애골드
                        person_dict[buy_id][1] -= amount

                        if buy_amount - amount > 0:
                            buy_queue.append([buy_id, buy_amount - amount, buy_price, buy_idx])

                        if now_amount - amount > 0:
                            sell_queue.append([now_id, now_amount - amount, now_price, now_idx])
                        now_amount -= amount
                        flag = True
            if flag == False:
                sell_queue.append([now_id, now_amount, now_price, now_idx])
            else:
                flag = True

            sell_queue = sorted(sell_queue, key=lambda x: (x[2], x[3]))
            buy_queue = sorted(buy_queue, key=lambda x: (x[2], x[3]))

    for item in sorted(person_dict.keys()):
        gold = person_dict[item][0]
        silver = person_dict[item][1]
        if gold > 0:
            gold = '+'+str(gold)
        else:
            gold = str(gold)

        if silver > 0:
            silver = '+'+str(silver)
        else:
            silver = str(silver)

        answer.append(item+' '+gold+' '+silver)
    return answer

print(solution(
["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"],
[[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]
))
