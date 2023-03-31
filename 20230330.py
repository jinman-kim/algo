def solution(k, m, score):
    answer = 0
    Fruit = []
    while True:
        if len(score) < m:
            break
        else:
            score.sort(reverse = True)
            print(score)
            min_score = min(score[:m])
            Fruit.append(min_score * m)
            score = score[m:]
    answer = sum(Fruit)
    return answer


a = solution(3,4,[1,2,3,4,1])
print(a)
