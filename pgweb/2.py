def solution(n, recipes, orders):
    answer = 0
    fire = [0 for i in range(n)]

    dish = {}
    for recipe in recipes:
        name, time = recipe.split()
        time = int(time)
        dish[name] = time

    for idx, order in enumerate(orders):
        food, ordertime = order.split()
        ordertime = int(ordertime)
        finishtime = 0

        usefire = fire.index(min(fire))
        if fire[usefire] <= ordertime: # 쓸 화구가 시간 남는 경우
            fire[usefire] = ordertime

        fire[usefire] += dish[food]
        finishtime = fire[usefire]

        if idx == len(orders)-1:
            return finishtime


print(solution(
    2, ["A 3","B 2"], ["A 1","A 2","B 3","B 4"]
))