from functools import reduce
def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))
    return reduce(lambda a,b : a^b,
                  [sum(map(lambda x:x%(i+1),data[i])) for i in range(row_begin-1,row_end)])

data = [[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]]
print(solution(data, 2, 2, 4))
