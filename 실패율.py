def solution(N,stages):
    from collections import Counter
    stage_count = Counter(stages)
    answer = {}
    stages.sort()
    tmp = len(stages)
    for i in range(N):
        if tmp:
            answer[i+1] = (stage_count[i+1]/tmp)
            tmp -= stages.count(i+1)
        else:
            answer[i+1] = 0
    result = sorted(answer.items(), key = lambda x:-x[1])
    a = [i[0] for i in result]
    return a

#
N = 7
stages = [1,2,3,4,5]
print(solution(N,stages))