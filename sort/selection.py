list = [1, 9 ,3, 2, 2, 4, 3]

for i in range(len(list)):
    min_value = int(1e9)
    index = 0
    for j in range(i, len(list)):
        if list[j] < min_value:
            min_value = list[j]
            index = j

    temp = list[i]
    list[i] = list[index]
    list[index] = temp

print(list)