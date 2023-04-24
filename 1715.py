from heapq import heappush, heappop
n = int(input())
card = []
for _ in range(n):
    heappush(card,int(input()))
answer = 0
# if len(card) == 1:
#     print(0)
# else:
while len(card) > 1:
    a = heappop(card)
    b = heappop(card)
    heappush(card, a+b)
    answer += a+b
print(answer)