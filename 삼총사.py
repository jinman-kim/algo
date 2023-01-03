def solution(number):
    from itertools import combinations
    answer = 0
    for i in combinations(number,3):
        if sum(i)==0:
            answer+=1
    return answer


number = [-2, 3, 0, 2, -5]
print(solution(number))