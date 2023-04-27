from heapq import heappush, heappop
n = int(input())
card = []
for _ in range(n):
    heappush(card,int(input()))
    # 들어오는 순서대로 정렬
print(card)
answer = 0
while card:
    print(heappop(card))
# while len(card) > 1:
#     a = heappop(card)
#     b = heappop(card)
#     heappush(card, a+b)
#     answer += a+b
print(answer)