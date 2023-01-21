def solution(n):
    answer = [[0 for i in range(j)] for j in range(1,n+1)]
    answer[0][0]=1
    row = 1
    col = 1
    diag = 1
    cnt = 0
    for i in range(n):
        for i in range((row-1)*2,n-row+1): #수직 아래로
            answer[i][row-1] = answer[i-1][row-1] + 1
        row +=1
        cnt += 1
        if cnt == n:
            break

        for j in range(col,n-col*2+2): #수평 우측으로
            answer[n-col][j] = answer[n-col][j-1]+1
        col +=1
        cnt += 1
        if cnt == n:
            break

        for i in range(n - diag - 1, 2 * (diag - 1), -1): #대각선 왼쪽 위로
            answer[i][i - diag + 1] = answer[i + 1][i - diag + 2] + 1
        diag += 1
        cnt += 1
        if cnt == n:
            break
    result = []
    for i in answer:
        result += i
    return [1] if n == 1 else result

n = 1
print(solution(n))