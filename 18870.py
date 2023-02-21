n = int(input())
axis = list(map(int,input().split()))
sorted_axis = sorted(set(axis),reverse=True)
num_dict = {}
cnt = 1
for i in range(len(sorted_axis)):
    num_dict[sorted_axis[i]] = len(sorted_axis)-cnt
    cnt += 1
answer = []
for i in axis:
    answer.append(num_dict[i])
print(*answer)
