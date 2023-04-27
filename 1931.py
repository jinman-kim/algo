n = int(input())
conf = [list(map(int,input().split())) for _ in range(n)]
conf.sort(key=lambda x: x[0])
conf.sort(key=lambda x: x[1])

if n == 1:
    print(1)
else:
    # 회의 하나씩 확인
    # 0번 회의를 tmp에 담고 시작
    # 최대 개수이니까
    # i 번째 회의가 tmp의
    print(conf)
    answer = 1
    tmp = conf[0]
    if tmp[0] == tmp[1]:
        answer = 0
    for i in range(len(conf)):
        if conf[i][0] >= tmp[1]:
            tmp = conf[i]
            answer += 1

    print(answer)