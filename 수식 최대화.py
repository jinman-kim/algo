def solution(expression):
    answer = 0
    num = []
    oper = []
    tmp = 0
    for i in range(len(expression)):
        if not expression[i].isdigit():
            oper.append(expression[i])
            num.append(int(''.join(expression[tmp:i])))
            tmp = i+1
    num.append(int(''.join(expression[tmp:])))
    print(oper)
    print(num)
    from itertools import permutations
    for orders in permutations(['*','+','-'],3):
        for order in orders:
            for op in range(len(oper)):
                if order == oper[op]:

    # 순서가 총 6개
    # 연산자 n개, 수 n+1개
    return answer


expression = "100-200*300-500+20"
print(solution(expression))