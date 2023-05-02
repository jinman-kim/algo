n = int(input())
conf = [list(map(int,input().split())) for i in range(n)]

conf.sort(key=lambda x: x[0])
conf.sort(key=lambda x: x[1])

if n == 1: #회의가 하나일때
    print(1)
else:
    answer = 1
    tmp = conf[0]
    if tmp[0] == tmp[1]:
        answer = 0
    for i in range(len(conf)):
        if conf[i][0] >= tmp[1]:
            tmp = conf[i]
            answer += 1
    print(answer)