from itertools import permutations


def arith(num_list,oper):
    tmp = num_list[0]
    maximum = -1e9
    minimum = 1e9
    for i in range(len(oper)):
        if oper[i] == 0:
            tmp += num_list[i+1]
        if oper[i] == 1:
            tmp -= num_list[i+1]
        if oper[i] == 2:
            tmp *= num_list[i+1]
        if oper[i] == 3:
            tmp = abs(abs(tmp) // num_list[i + 1])
    if tmp > maximum:
        maximum = tmp
        return maximum
    if tmp < minimum:
        minimum = tmp
        return minimum
    else:
        return tmp


n = int(input())
num = list(map(int,input().split()))
count = list(map(int,input().split()))
tool = [i for i in range(4) for _ in range(count[i])]
answer = [arith(num,list(p)) for p in permutations(tool,n-1)]
print(max(answer))
print(min(answer))
