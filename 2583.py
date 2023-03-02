import sys
sys.setrecursionlimit(10**6)
dx,dy = [1,-1,0,0] , [0,0,-1,1]


def dfs(x,y):
    global cnt
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
            paper[nx][ny] = 0
            cnt += 1
            dfs(nx,ny)
    return cnt


m,n,k = map(int, input().split())
paper = [[1]*m for _ in range(n)]
rect = []
for _ in range(k):
    a,b,c,d = map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            paper[i][j] = 0
for i in range(len(paper)):
    for j in range(len(paper[0])):
        cnt = 0
        if paper[i][j] == 1:
            dfs(i,j)
            rect.append(cnt)
rect.sort()
print(len(rect))
for i in rect:
    if i == 0:
        print(1,end=' ')
    else:
        print(i,end=' ')
