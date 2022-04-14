import sys
input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()
Slen = len(S)
Plen = len(P)
pi = [0] * Plen

def Fail(P):
    global Plen, pi
    begin, matched = 1, 0
    while begin+matched < Plen:
        if P[begin+matched] == P[matched]:
            matched+=1
            pi[begin+matched-1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]
def KMP(S, P):
    global Slen, Plen
    begin, matched = 0, 0
    while begin <= Slen - Plen:
        if matched < Plen and S[begin+matched] == P[matched]:
            matched += 1
            if matched == Plen:
                return True
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]
    return False


Fail(P)
if KMP(S, P):
    print(1)
else:
    print(0)

