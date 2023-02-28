from collections import deque
n = int(input())
card = deque(list(range(1,n+1)))
while card:
    a = card.popleft()
    if card:
        tmp = card.popleft()
        card.append(tmp)
print(a)