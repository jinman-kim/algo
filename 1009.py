div_hash = dict()
for i in range(1, 100):
    tmp = []
    for j in range(1, 6):
        if (i**j) % 10 not in tmp:
            tmp.append((i**j) % 10)
        else:
            div_hash[i] = tmp
print(div_hash)
answer = []
for _ in range(int(input())):
    a,b = map(int, input().split())
    data_size = len(div_hash[a])
    print(div_hash[a][b % data_size]-1)
