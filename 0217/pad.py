def solution(numbers, hand):
    answer = ''
    position = {1:(0, 0), 2:(0, 1), 3:(0, 2),
                4:(1, 0), 5:(1, 1), 6:(1, 2),
                7:(2, 0), 8:(2, 1), 9:(2, 2),
                '*':(3, 0), 0:(3, 1), '#':(3, 2)}
    Lfinger = '*'
    Rfinger = '#'
    left = [1, 4, 7]
    mid = [2, 5, 8, 0]
    right = [3, 6, 9]

    for number in numbers:
        if number in left:
            answer += 'L'
            Lfinger = number
        elif number in right:
            answer += 'R'
            Rfinger = number
        elif number in mid:
            now_row, now_col = position[number]
            Llength = abs(position[Lfinger][0] - now_row) + abs(position[Lfinger][1] - now_col)
            Rlength = abs(position[Rfinger][0] - now_row) + abs(position[Rfinger][1] - now_col)
            if Llength < Rlength:
                answer += 'L'
                Lfinger = number
            elif Llength > Rlength:
                answer += 'R'
                Rfinger = number
            elif Llength == Rlength:
                if hand == 'right':
                    answer += 'R'
                    Rfinger = number
                elif hand == 'left':
                    answer += 'L'
                    Lfinger = number

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

