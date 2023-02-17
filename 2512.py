n = int(input())
req = list(map(int,input().split()))
limit = int(input())
start,end = 0, max(req)
while start <= end:
    mid = (start+end)//2
    num = 0
    for i in req:
        if i >= mid: num += mid
        else: num += i
    if num <= limit: start = mid + 1
    else: end = mid - 1
print(end)

