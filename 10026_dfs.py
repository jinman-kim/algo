import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[x][y] = True
    c_color = site[x][y]
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == 0:
                if site[nx][ny] == c_color:
                    dfs(nx,ny)


n = int(input())
site = []
# 적록색약  G=R (Green and Red)
for _ in range(n):
    rgb = list(input())
    site.append(rgb)
visited = [[0] * n for _ in range(n)]

normal_cnt, disabled_cnt = 0,0

#일반인이 보는 구역 개수 세기
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 :
            dfs(i,j)
            normal_cnt += 1

#적록색맹 R을 G로 커버, visited 초기화
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if site[i][j] == 'R':
            site[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            disabled_cnt += 1
print(normal_cnt, disabled_cnt)