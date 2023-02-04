def solution(record):
    answer = []
    name = {}
    for i in record:
        if i.split()[0] == 'Enter':
            name[i.split()[1]] = i.split()[2]
        elif i.split()[0] == 'Change':
            name[i.split()[1]] = i.split()[2]
    for i in record:
        if i.split()[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(name[i.split()[1]]))
        elif i.split()[0] == 'Leave' and i.split()[1] in name.keys():
            answer.append("{}님이 나갔습니다.".format(name[i.split()[1]]))
    return answer

record = ["Leave uid1234"]
print(solution(record))