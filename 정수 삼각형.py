def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
    answer = max(triangle[-1:][0])
    return answer

#4,5 의 경우 , 0이면 인덱스 0이랑결합,  인덱스1이면 ,인덱스0,1 중 큰거랑 결합, 인덱스2이면, 인덱스1,2중 큰거랑 결합 ,
triangle = [[7], [3, 8]]
print(solution(triangle))