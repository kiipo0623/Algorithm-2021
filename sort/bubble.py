list = [1, 9 ,3, 2, 2, 4, 3]

for i in range(1, len(list)):
    for j in range(0, len(list) - i):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print(list)