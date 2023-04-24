n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
dice = [0,0,0,0,0,0]
def move(dir):
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c#421653
    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d#326154
    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b#513462
    elif dir == 4: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e #263415

# no , no , 북 남
dx = [0, 0, -1, 1]
#  동 , 서  , no , no
dy = [1, -1, 0, 0]

act = list(map(int, input().split()))
for i in act:
    x += dx[i - 1]
    y += dy[i - 1]

    if x < 0 or x >= n or y < 0 or y >= m:
        x -= dx[i - 1]
        y -= dy[i - 1]
        continue
    move(i)
    if board[x][y] == 0:
        board[x][y] = dice[-1] #dice 마지막원소가 바닥
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0
    print(dice[0])

