dx, dy = [1,-1,0,0], [0,0,1,-1]
# answer, max_connect  , depth
def dfs(depth,cnt,connect):
    global answer
    global max_connect
    if depth == core_len:
        if connect > max_connect:
            max_connect = connect
            answer = cnt
        elif connect == max_connect and answer > cnt:
            answer = cnt
        return
    for k in range(depth, core_len):
        cx,cy = core[k]
        for d in range(4):
            nx, ny = cx, cy
            flag=False
            tmp=set()
            leng=0
            while True:
                nx += dx[d]
                ny += dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    flag=True
                    break
                if room[nx][ny] == 1:
                    break
                tmp.add((nx,ny))
                leng += 1
            if flag:
                for px,py in tmp:
                    room[px][py] = 1
                dfs(k+1,cnt+leng,connect+1)

                for px,py in tmp:
                    room[px][py] = 0


t = int(input())
for tc in range(t):
    answer = 1e9
    max_connect = 0
    room, core = [],[]
    n = int(input())
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(1,n-1):
            if i == 0 or i == n-1:
                break
            if tmp[j] == 1:
                core.append([i,j])
        room.append(tmp)
    core_len = len(core)
    visited = [[False]*n for _ in range(n)]
    dfs(0, 0, 0)
    print('#%d %d'%(tc+1, answer))