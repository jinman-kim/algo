def solution(n, lost, reserve):

    reserve = set(reserve)

    for size in [0, 1, -2]:
        lost = set(map(lambda x : x+size, lost))
        reserve, lost = reserve - lost, lost - reserve

    return n - len(lost)

n = 2
lost = [1,2]
reserve = [1]
print(solution(n,lost,reserve))

