def solution(numbers):
    from itertools import combinations
    answer = []
    for combi in combinations(numbers,2):
        if sum(combi) not in answer:
            answer.append(sum(combi))
    answer.sort()
    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))