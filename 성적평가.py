n = int(input())
olympic = [0,0,0]

for _ in range(n):
    a,b,c = map(int,input().split())
    study = [a,b,c]
    olympic[0] += a
    olympic[1] += b
    olympic[2] += c
    cnt = 1
    tmp = []
    for i in study:
        if i > a:
            cnt+=1
    tmp.append(cnt)
    cnt = 1
    for i in study:
        if i > b:
            cnt+=1
    tmp.append(cnt)
    cnt = 1
    for i in study:
        if i > c:
            cnt+=1
    tmp.append(cnt)
    print(*tmp)
cnt = 1
rank = []
for i in olympic:
    if i > olympic[0]:
        cnt+=1
rank.append(cnt)
cnt = 1
for i in olympic:
    if i > olympic[1]:
        cnt+=1
rank.append(cnt)
cnt = 1
for i in olympic:
    if i > olympic[2]:
        cnt+=1
rank.append(cnt)
print(*rank)