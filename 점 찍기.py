def solution(k,d):
    import math
    answer = 0
    for x in range(0,d+1,k):
        y = (d**2-x**2)**0.5 # 원에서
        answer += math.ceil(y / k) + (1 if y % k == 0 else 0)
    return answer

print(solution(1,5))