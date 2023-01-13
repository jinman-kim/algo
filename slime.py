from copy import deepcopy

def solution(graph):
    import time
    start = time.time()
    for i in graph:
        i.insert(0,0)
        i.insert(len(i),0)
    graph.insert(0, [0 for _ in range(len(graph)+2)])
    graph.insert(len(graph),[0 for _ in range(len(graph)+1)])
    while True:
        tmp = deepcopy(graph)
        for i in range(len(graph)-1):
            for j in range(len(graph)-1):
                if graph[i][j] == 1:
                    if graph[i+1][j] == 3 or graph[i-1][j] == 3 or graph[i][j+1] == 3 or graph[i][j-1] == 3 or graph[i+1][j]==2:
                        pass
                    else:
                        if graph[i+1][j] == 0:
                            graph[i][j] = 0
                            graph[i+1][j] = 1
        if tmp == graph:
            break
        # if time.time() - start > 0.2:
        #     break
    answer = []
    for i in range(1,len(graph)-1):
        answer.append(graph[i][1:len(graph)-1])
    for i in answer:
        print(i)
    return answer


graph = [
    [1,1,1,3,1],
    [0,1,1,1,3],
    [1,0,0,1,1],
    [1,2,1,2,1],
    [3,2,0,0,0]]
# 아래는 2가 있으면 안 되고, 3은 상하좌우에 다 있어도 안되고

print(solution(graph))