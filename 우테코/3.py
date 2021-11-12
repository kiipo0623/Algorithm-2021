def solution(ings, menu, sell):
    answer = 0
    ingdict = {}
    menudict = {}

    for ing in ings:
        name, price = ing.split()
        ingdict[name] = int(price)

    for m in menu:
        name, list, price = m.split()
        makemoney = 0
        for i in range(len(list)):
            makemoney += ingdict[list[i]]
        profit = int(price) - makemoney
        menudict[name] = profit

    for s in sell:
        name, count = s.split()
        answer += (menudict[name]*int(count))

    return answer

print(solution(["r 10", "a 23", "t 124", "k 9"],
["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"],
["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]
))