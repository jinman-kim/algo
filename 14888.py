from itertools import permutations

##  caution : 나누기 연산시에  음수 // 양수를 하면 -1//3=0 이아닌 -1이 나옴 주의해야함
def arith(num_list,oper):
    tmp = num_list[0]
    for i in range(len(oper)):
        if oper[i] == 0:
            tmp += num_list[i+1]
        if oper[i] == 1:
            tmp -= num_list[i+1]
        if oper[i] == 2:
            tmp *= num_list[i+1]
        if oper[i] == 3:
            tmp = int(tmp / num_list[i+1])
    return tmp


n = int(input())
num = list(map(int,input().split()))
count = list(map(int,input().split()))
tool = [i for i in range(4) for _ in range(count[i])]
answer = [arith(num,list(p)) for p in permutations(tool,n-1)]
print(max(answer))
print(min(answer))
