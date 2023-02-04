def solution(rows, columns, queries):
    answer = []
    square = [[i+1+columns*(j) for i in range(columns)] for j in range(rows)]
    for query in queries:
        king_query = []
        for i in range(query[2]-query[0]):
            square[query[0]-1+i][query[1]-1] = square[query[0]+i][query[1]-1]
            square[query[0]+i][query[3]-1] = square[query[0]-1+i][query[3]-1]
            king_query.append(min(square[query[0]-1+i][query[1]-1],square[query[0]+i][query[3]-1]))
        for i in range(query[3]-query[1]):
            square[query[0]-1][query[1]+i] = square[query[0]-1][query[1]-1+i]
            square[query[2]-1][query[1]-1+i] = square[query[2]-1][query[1]+i]
            king_query.append(min(square[query[0]-1][query[1]+i], square[query[2]-1][query[1]-1+i]))
        answer.append(min(king_query))
    return answer

rows,columns = 6,6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))