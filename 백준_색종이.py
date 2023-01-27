n = int(input())
width, height = [], []
rect = []
for _ in range(n):
    a,b = map(int,input().split())
    width.append(a)
    height.append(b)
    rect.append([a,b])
colored_paper = [[0]*(max(width)+11) for _ in range(max(height)+11)]

for i in range(len(rect)):
    for j in range(10):
        for k in range(10):
            colored_paper[rect[i][1]+k][rect[i][0]+j] = 1

answer = 0
for row in colored_paper:
    answer += sum(row)
print(answer)