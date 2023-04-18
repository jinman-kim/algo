n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
answer = 0
for i in coin[::-1]:
    if k >= i:
        answer += k // i
        k -= i * (k // i)
print(answer)