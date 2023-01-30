def solution(numbers):
    answer = [-1]
    tmp = -1
    max_crew = [-1]
    for i in range(len(numbers)-1,-1,-1):
        max_crew.append(numbers[i])
        if numbers[i] > tmp:
            answer.insert(0,-1)
            tmp = max(numbers[i], tmp)
        elif numbers[i] == tmp:
            answer.insert(0,-1)
            tmp = max(numbers[i], tmp)
        else:
            for j in range(len(max_crew)):
                if max_crew[j] > numbers[i]:
                    answer.insert(0,max_crew[j])
                    break
        print(max_crew)
    answer.pop()
    return answer


numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))