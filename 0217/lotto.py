def solution(lottos, win_nums):
    win_nums.sort()
    count = 0
    zero = 0
    print("win", win_nums)

    for lotto in lottos:
        if lotto == 0:
            zero += 1
        else:
            if binary_search(0, 5, lotto, win_nums):
                count += 1

    best = 7-(count + zero)
    worst = 7-count
    if best > 6:
        best = 6
    if worst > 6:
        worst = 6
    return [best, worst]


def binary_search(start, end, target, array):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return True
    return False

print(solution(
[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]
))