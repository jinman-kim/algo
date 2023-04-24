N, K = map(int, input().split())
a = list(map(int, input().split()))
coin = 0
while 1 :
    for x in range(0,len(a)):
        if len(list(str(K))) == len(list(str(a[x]))) :
            K =K - a[x]
            coin += 1
            if coin >= 5:
                coin -= 4
        elif K == 0:
            print(1)
            break
print(coin)