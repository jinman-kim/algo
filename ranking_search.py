def solution(info,query):
    new_query = []
    for q in range(len(query)):
        new_query.append(query[q].replace('and', '').split())
        if new_query[q][0] == '-':
            new_query[q][0] = 'python,java,cpp'
        if new_query[q][1] == '-':
            new_query[q][1] = 'backend,frontend'
        if new_query[q][2] == '-':
            new_query[q][2] = 'senior,junior'
        if new_query[q][3] == '-':
            new_query[q][3] = 'pizza,chicken'
    new_info = []
    for i in info:
        new_info.append(i.split())
    answer = [0] * (len(query))
    for i in range(len(new_query)):
        for j in range(len(new_info)):
            for k in range(5):
                if int(new_info[j][4]) < int(new_query[i][4]):
                    break
                elif new_info[j][k] not in new_query[i][k] and k!=4:
                    break
                elif k == 4:
                    answer[i] += 1

    return answer
info = ["java backend junior pizza 150","python frontend senior chicken 210",
        "python frontend senior chicken 150","cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info,query))

