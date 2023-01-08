def solution(a,b,n):
    answer = 0
    while True:
        answer += b * (n // a)
        n = n-a*(n//a)+b*(n//a)
        if n<a:
            break
    return answer


a,b,n=3,1,20
print(solution(a,b,n))