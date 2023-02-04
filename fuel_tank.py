from itertools import combinations_with_replacement
s = int(input())
a = []
for i in combinations_with_replacement(range(1,51),3):
    steel = i[0] * i[1] * i[2]
    pyo = i[0]*i[1] + i[0]*i[2] + i[1]*i[2]
    if i[0]*i[1]*i[2] >= s:
        a.append([i,steel,pyo])
a.sort(key=lambda x : (x[1],x[2]))
print(*a[0][0])
