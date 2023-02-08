def solution_1(number, k):
    from itertools import combinations
    num = list(map(int ,number))
    new_num = []
    for i in combinations(num, len(num)-k):
        new_num.append(int(''.join(list(map(str,i)))))
    new_num.sort(key=lambda x:-x)
    return str(new_num[0])


def solution_2(number, k):
    answer = ''
    stack = [0]
    for num in number:
        stack.append(num)
    return answer

number = "4177252841"
k = 4
print(solution_2(number,k))