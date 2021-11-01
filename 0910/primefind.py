import itertools

def solution(numbers):
    answer = 0
    length = len(numbers)
    numberlist = []
    numberset = set()

    for i in range(length):
        numberlist.append(numbers[i])

    for i in range(1, length + 1):
        primecandidate = itertools.permutations(numberlist, i)
        for number in primecandidate: # tuple로 반환받음
            # 내가 꺼내고 싶은 형식은 이걸 합쳐서 숫자로 만드는
            temp = int(''.join(number))
            numberset.add(temp)

    for num in numberset:
        # 모아서 set에 넣고 나중에 한번에 돌려야
        if ifprime(num):
            answer +=1

    return answer

def ifprime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(solution("011"))