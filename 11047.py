n, k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
cnt = 0
for i in coin:
    while True:
        if k >= i:
            tmp = k//i
            cnt += tmp
            k %= i
        else:
            break
    if k == 0:
        break

print(cnt)
