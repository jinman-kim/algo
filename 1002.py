# Baekjoon 1002번 터렛

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = list(map(int,input().split()))
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
    if dist == 0 and r1 == r2:
        print(-1)
    elif dist == r1 + r2 or dist == abs(r1-r2):
        print(1)
    elif abs(r1-r2) < dist < r1 + r2:
        print(2)
    else:
        print(0)