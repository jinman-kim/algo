def solution_1(n):
    answer = []
    start = 0
    for i in range(int(n**0.5)):
        if 3**i >= n:
            start = i
            break
    for i in range(start,-1,-1):
        tmp = n//3**i
        answer.append(tmp)
        n -= tmp*(3**i)
    if answer[0] == 0:
        answer.pop(0)
    rev_three = 0
    for i in range(len(answer)):
        rev_three += answer[i]*3**i
    return rev_three

def solution_2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer


print(solution_2(125))