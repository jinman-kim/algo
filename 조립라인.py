cost = [(list(map(int,input().split()))) for _ in range(int(input()))]
if len(cost) == 1:
    print(min(cost[-1]))
else:
    for i in range(1,len(cost)):
        a_to_a = cost[i][0] + cost[i-1][0]
        b_to_b = cost[i][1] + cost[i-1][1]
        a_to_b = cost[i-1][0] + cost[i-1][2] + cost[i][1]
        b_to_a = cost[i-1][1] + cost[i-1][3] + cost[i][0]
        cost[i][0] = min(a_to_a,b_to_a)
        cost[i][1] = min(b_to_b,a_to_b)
    print(min(cost[-1]))

# input TC
# 2
# 1 3 1 2
# 10 2
# output
# 4