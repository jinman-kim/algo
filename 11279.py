from heapq import heappush, heappop
import sys

n = int(input())
h_list = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a > 0:  #0이 아닐때,
        heappush(h_list, -a) #최소힙   [- a,   ~~~~  b]
    else: #0일떄
        if not h_list: #   []
            print(0)
        else:  #[-3,-1]
            print(-heappop(h_list))