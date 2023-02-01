light= []
digit = [[1,1,1,1,1,1,0],[0,0,1,1,0,0,0],[0,1,1,0,1,1,1],[0,1,1,1,1,1,0],[1,0,1,1,0,0,1],
    [1,1,0,1,1,0,1],[1,0,1,1,1,1,1],[1,1,1,1,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,1,0,1],[0,0,0,0,0,0,0]]
for _ in range(int(input())):
    a, b = map(int,input().split())
    click = 0
    dig_a, dig_b = list(str(a)),list(str(b))
    new_a, new_b = [],[]
    for i in range(len(dig_a)-1,-1,-1):
        new_a.append(int(dig_a[i]))
    for i in range(len(dig_b)-1,-1,-1):
        new_b.append(int(dig_b[i]))
    if len(new_a) != 5:
        while True:
            new_a.append(10)
            if len(new_a) == 5:
                break
    if len(new_b) != 5:
        while True:
            new_b.append(10)
            if len(new_b) == 5:
                break
    for i in range(5):
        for j in range(7):
            click += abs(digit[new_a[i]][j] - digit[new_b[i]][j])
    print(click)