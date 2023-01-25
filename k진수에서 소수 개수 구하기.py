def solution(n,k):
    num = []
    tmp = 0
    answer = 0
    jinsoo = ''
    for i in range(1,n):
        if n < k**i:
            tmp = i
            break
    for i in range(tmp-1,-1,-1):
        jinsoo += str(n//(k**i))
        n -= (k**i)*(n//k**i)
    for i in jinsoo.split('0'):
        if i != '':
            num.append(int(i))
    num.sort()
    while True:
        if 1 in num:
            num.remove(1)
        else:
            break

    def is_prime(number):
        if number == 1:
            return False
        for i in range(2, int(number ** (0.5)) + 1):
            if number % i == 0:
                return False
        return True

    for i in num:
        if is_prime(i):
            answer += 1
    return answer


n = 11113
k = 10
print(solution(n,k))