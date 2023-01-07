# unsolved

def solution(cap, n, deliveries, pickups):
    answer1 = 0
    answer2 = 0
    origin = cap
    for i in range(n):
        if deliveries[i]==0:
            continue
        while True:
            deliveries[i]-=1
            cap-=1
            if cap == 0 and i==n-1:
                answer1 += (i + 1) * 2
                break
            if cap == 0:
                answer1 += (i+1)*2
                cap = origin
            if deliveries[i] == 0 and i==n-1:
                answer1 += (i+1)*2
            if deliveries[i] == 0:
                break
    cap = origin
    for i in range(n):
        if pickups[i] == 0:
            continue
        while True:
            pickups[i] -= 1
            cap -= 1
            if cap == 0 and i == n - 1:
                answer2 += (i + 1) * 2
                break
            if cap == 0:
                answer2 += (i + 1) * 2
                cap = origin
            if pickups[i] == 0 and i == n - 1:
                answer2 += (i + 1) * 2
            if pickups[i] == 0:
                break
    # print(answer1,answer2)
    return max(answer1,answer2)


cap,n,deliveries,pickups=2,7,[1,0,2,0,1,0,2],[0,2,0,1,0,2,0]
print(solution(cap,n,deliveries,pickups))