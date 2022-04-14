import math
S = int(input())
num = math.floor(math.sqrt(2*S))
if num * (num+1) > 2*S:
    print(num-1)
else:
    print(num)
