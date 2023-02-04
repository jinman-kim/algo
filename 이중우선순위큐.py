def solution(operations):
    answer = []
    for i in operations:
        if i.split()[0] == 'I':
            answer.append(int(i.split()[1]))
        if i.split()[0] == 'D' and int(i.split()[1]) == 1 and answer != []:
            answer.remove(max(answer))
        if i.split()[0] == 'D' and int(i.split()[1]) == -1 and answer!= []:
            answer.remove(min(answer))

    if answer == []:
        result = [0,0]
    else:
        result = [max(answer),min(answer)]
    return result


operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))

