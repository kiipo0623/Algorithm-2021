def solution(N, number):
    pos_set = [0, [N]]

    if N == number:
        return 1

    for i in range(2, 9):
        imsi_set = []
        imsi_set.append(int(str(N) * i))
        for i_half in range(1, i / 2 + 1):
            for op1 in pos_set[i_half]:
                for op2 in pos_set[i - i_half]:
                    imsi_set.append(op1 + op2)
                    imsi_set.append(op1 - op2)
                    imsi_set.append(op2 - op1)
                    imsi_set.append(op1 * op2)

                    if op1 != 0:
                        imsi_set.append(op2 / op1)

                    if op2 != 0:
                        imsi_set.append(op1 / op2)

        if number in imsi_set:
            return i

        pos_set.append(imsi_set)

    return -1

print(solution(5, 12))