n, m = map(int,input().split())

limit = []
real = []
for i in range(n):
    a,b = map(int,input().split())
    for _ in range(a):
        limit.append(b)
for i in range(m):
    a,b = map(int,input().split())
    for _ in range(a):
        real.append(b)
tmp = 0
for i in range(100):
    tmp = max(real[i]-limit[i],tmp)
print(tmp)