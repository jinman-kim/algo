# N개의 시험장
# i -> Ai 명
# 총감독, 부감독으로 나뉨
# 역량: 총감독 B명 , 부감독 C명
# 총감독 오직 1명
# i번시험장 총감독1 부감독 n명
# i = B + n*C
n = int(input())
stu = list(map(int, input().split()))
b,c = map(int, input().split())
for i in range(len(stu)):
    stu[i] = max(stu[i]-b,0)
#일단 총감독이 시험장개수 n만큼 있어야되니 answer = n 을 초기화
answer = n
for i in range(len(stu)):
    if stu[i] % c == 0:
        answer += stu[i]//c
    else:
        answer += 1 + stu[i]//c
print(answer)
