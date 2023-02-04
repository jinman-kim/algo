from collections import defaultdict
n = int(input())
x = defaultdict(list)
print(x)
for i in range(n):
    a = input().split(',') # local=ulsan , state=Deployed
    b = []
    for word in a:
        b.append(word)
print(b)
q = int(input())
