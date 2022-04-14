def check(row, col, machine):
    flag = False
    now = machine[row][col]
    while True:
        if now == '#':
            row += 1
        elif now == '>':
            col += 1
        elif now == '<':
            col -= 1
        else:
            if flag == False:
                flag = True
                row += 1
            else:
                return False

        if row == len(machine):
            return True
        else:
            now = machine[row][col]

def solution(drum):
    answer = 0
    machine = []
    for d in drum:
        machine.append(list(d))

    for i in range(len(drum)):
        if check(0, i, machine) == True:
            answer += 1

    return answer

print(solution(
["######",">#*###","####*#","#<#>>#",">#*#*<","######"]
))