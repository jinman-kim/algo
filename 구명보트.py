def solution(people, limit):
    people.sort()
    start = 0
    end = len(people)
    answer = 0
    if len(people) == 1:
        answer = 1
    else:
        while end > start:
            if people[start]+people[end-1] <= limit:
                answer += 1
                start += 1
                end -=1
            else:
                answer +=1
                end -= 1
    return answer


people = [70,50,80,40]
limit = 90
print(solution(people,limit))