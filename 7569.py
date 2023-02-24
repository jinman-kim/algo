from collections import deque
tomato = []
q = deque([])
n,m,h = map(int,input().split())
for _ in range(h):
    tomato.append([list(map(int,input().split())) for _ in range(m)])
for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        for k in range(len(tomato[i][j])):
            if tomato[i][j][k] == 1:
                q.append([i,j,k])
dx,dy,dz = [1,-1,0,0,0,0] ,[0,0,1,-1,0,0], [0,0,0,0,1,-1]
while q:
    x,y,z = q.popleft()
    for i in range(6):
        nx,ny,nz = x+dx[i], y+dy[i], z+dz[i]
        if 0<= nx < h and 0<= ny < m and 0<= nz < n and tomato[nx][ny][nz] == 0:
            q.append([nx,ny,nz])
            tomato[nx][ny][nz] = tomato[x][y][z] + 1

tmp = 0
for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        for k in range(len(tomato[i][j])):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            tmp = max(tomato[i][j][k],tmp)
print(tmp-1)
