def check(alphabet_list):
    antatica = ['a', 'n', 't', 'i', 'c']
    global words
    count = len(words)
    for word in words:
        for w in word[4:-4]:
            if w not in alphabet_list and w not in antatica:
                count -= 1
                break
    return count


import sys
from itertools import combinations
input = sys.stdin.readline
N, K = map(int, input().split())
words = []
alphabet_list = []

max_word_count = 0

for _ in range(N):
    words.append(input().strip())

if K<5:
    print(0)
else:
    for word in words:
        for w in word:
            if w not in alphabet_list:
                alphabet_list.append(w)

    if len(alphabet_list) <= K: # 사용하는 알파벳이 K개 안에 들어가는 경우
        print(N)

    else: # 사용하는 알파벳이 다 포함되지 않는 경우
        K -= 5
        alphabet_list.remove('a')
        alphabet_list.remove('n')
        alphabet_list.remove('t')
        alphabet_list.remove('c')
        alphabet_list.remove('i')

        choice = list(combinations(alphabet_list, K))

        for c in choice:
            c = list(c)
            if check(c) > max_word_count:
                max_word_count = check(c)

    print(max_word_count)
