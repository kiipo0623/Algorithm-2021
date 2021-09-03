# N으로 표현

def solution(N, number):

    arr = [0, [N]]

    for i in range(2, 9):
        imsi = []
        for j in range(1, i):
            for num1 in arr[j]:
                for num2 in arr[i-j]:
                    imsi.append(num1 + num2)
                    imsi.append(num1 - num2)
                    imsi.append(num2 - num1)
                    imsi.append(num1 * num2)
                    if num1 != 0:
                        imsi.append(num2 / num1)
                    if num2 != 0:
                        imsi.append(num1 / num2)

        if number in imsi:
            return i
        arr.append(imsi)

    return -1

print(solution(5, 12))