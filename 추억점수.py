def solution(name, yearning, photo):
    answer = []
    rem = {}
    for i in zip(name,yearning):
        rem[i[0]] = i[1]
    for i in photo:
        tmp = 0
        for j in i:
            try:
                tmp += rem[j]
            except:
                pass
        answer.append(tmp)
    return answer