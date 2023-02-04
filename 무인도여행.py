import sys
def solution(maps):
    global cnt
    answer = []
    graph = [[]for _ in range(len(maps))]
    cnt = 0
    for i in range(len(maps)):
        for j in maps[i]:
            if j == 'X':
                graph[i].append(0)
            else:
                graph[i].append(int(j))
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(maps) or y >= len(maps):
            return False
        global cnt
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if graph[mx][my] != 0:
                cnt += graph[mx][my]
                dfs(mx, my)

    sys.setrecursionlimit(10 ** 5)
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            cnt = graph[i][j]
            dfs(i, j)
            if cnt != 0:
                answer.append(cnt)
    print(graph)
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)


maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))