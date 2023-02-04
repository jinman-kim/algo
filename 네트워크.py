def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for com in range(n):
        if visited[com] == False:
            dfs(n, computers,com,visited)
            answer += 1
    return answer


def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == 0:
                dfs(n,computers,connect, visited)


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))