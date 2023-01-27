def solution(weights):
    answer = 0
    from itertools import combinations
    import numpy as np
    couple = []
    weights.sort()
    print(weights)
    for i in combinations(weights,2):
        couple.append(i)
    couple = set(couple)
    for i in couple:
        if i[0] == i[1]:
            answer+=1
            continue
        if min(i[0],i[1])/max(i[0],i[1]) == 0.5:
            answer += 1
            continue
        if min(i[0],i[1])/max(i[0],i[1]) == 0.75:
            answer += 1
            continue
        if min(i[0],i[1])*3==max(i[0],i[1])*2:
            answer += 1
            continue
    return answer

weights = [100,180,100,270,360]
print(solution(weights))