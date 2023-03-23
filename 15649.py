n, m = map(int,input().split())
from itertools import permutations
for i in permutations(list(range(1,n+1)),m):
    print(*i)