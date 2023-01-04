def solution(k,m,score):
    answer = 0
    box = []
    score.sort(reverse=True)
    for i in score:
        box.append(i)
        if len(box)==m:
            answer += min(box)*m
            box = []
    return answer


k,m = 4,3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k,m,score))