def solution(data, col, row_begin, row_end):
    answer = []
    result = 0
    tmp=0
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin, row_end + 1, 1):
        for j in data[i-1]:
            tmp+=j%i
        answer.append(tmp)
        tmp=0
    for i in answer:
        result ^= i
    return result


data = [[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]]
print(solution(data, 2, 2, 4))
