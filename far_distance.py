from collections import deque
def solution(n,vertex):
    graph = [[]for _ in range(n+1)]
    visit=[0]*(n+1)
    visit[1]=1
    for a,b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    q=deque([1])
    while q:
        x=q.popleft()
        for i in graph[x]:
            if visit[i]==0:
                visit[i]=visit[x]+1
                q.append(i)
    return visit.count(max(visit))

n,vertex=6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,vertex))