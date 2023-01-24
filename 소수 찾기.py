def solution(numbers):

    def is_prime(n):
        if n == 1:
            return 0
        else:
            for i in range(2, n + 1):
                if n % i == 0 and i != n:
                    return 0
                elif i == n:
                    return n

    from itertools import permutations
    answer = 0
    combi = []
    for num in range(len(numbers),0,-1):
        for i in permutations(list(numbers),num):
            combi.append(int(''.join(i)))
    combi = list(set(combi))
    for i in combi:
        if is_prime(i):
            answer+=1
    return answer

numbers = '17'
print(solution(numbers))