if now_do == 1:  # 판 요청
    while now_amount and buy_queue:
        for index, buy in enumerate(buy_queue):
            buy_id, buy_amount, buy_price, buy_idx = buy
            del buy_amount[index]
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
            else:  # 가격 안맞는 경우
                sell_queue.append([now_id, now_amount, now_price, now_idx])

    sell_queue = sorted(sell_queue, key=lambda x: (x[2], x[3]))
    buy_queue = sorted(buy_queue, key=lambda x: (x[2], x[3]))