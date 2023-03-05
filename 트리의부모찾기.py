n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1]*(n+1)

from sys import setrecursionlimit as ssl
ssl(10 ** 9)


def dfs(x):
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = x
            dfs(i)

dfs(1)
for i in range(2,n+1):
    print(visited[i])



