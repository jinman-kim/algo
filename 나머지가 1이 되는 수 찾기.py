def solution(n):
    answer = [i for i in range(1,n) if n%i==1][0]
    return answer



print(solution(10))