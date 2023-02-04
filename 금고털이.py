m , n = map(int, input().split())
jewerly = []
bag = [0,0]
for i in range(n):
    a, b = map(int,input().split())
    jewerly.append([a,b])
jewerly = sorted(jewerly, key=lambda x: -x[1])
for i in range(len(jewerly)):
    if bag[0] == m:
            break
    while True:
        jewerly[i][0] -= 1
        bag[0] += 1
        bag[1] += jewerly[i][1]
        if jewerly[i][0] == 0:
            break
        if bag[0] == m:
            break
print(bag[1])