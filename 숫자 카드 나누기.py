from functools import reduce
from math import gcd


def solution(A,B):
    gcd1 , gcd2 = reduce(gcd,A),reduce(gcd,B)
    print(gcd1)
    print(gcd2)
    answer = []
    if all(element % gcd2 for element in A):
        answer.append(gcd2)
    if all(element % gcd1 for element in B):
        answer.append(gcd1)

    return max(answer) if answer else 0



A = [14, 35, 119]
B = [18, 30, 102]
print(solution(A,B))