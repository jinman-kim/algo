def solution(number, limit, power):
    answer = 0
    b = []
    for n in range(1,number+1):
        a = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                a.append(i)
        for i in a[:]:
            if n % i == 0:
                a.append(n//i)
        b.append(len(set(a)))
    for i in range (len(b)):
        if b[i] <= limit:
            answer += b[i]
        else:
            answer += power
    return answer

number,limit,power = 10,3,2
print(solution(number,limit,power))