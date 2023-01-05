def solution(today, terms, privacies):
    answer = []
    term = dict()
    privacy = []
    today = list(map(int,today.split('.')))
    new_today = today[0]*336 + (today[1]-1)*28 +today[2]
    for i in terms:
        term[i[0]] = i[2:]
    for i in privacies:
        privacy.append(i.replace(' ','.').split('.'))
    for i in range(len(privacy)):
        num = int(privacy[i][0])*336 + (int(privacy[i][1])-1)*28 + int(privacy[i][2]) +int(term[privacy[i][3]])*28-1
        if new_today > num:
            answer.append(i+1)
    answer.sort()
    return answer


today = "2020.02.01"
terms = ["Z 100", "D 5","A 1"]
privacies = ["2019.05.03 A", "2018.04.02 A", "2018.04.02 A", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today,terms,privacies))