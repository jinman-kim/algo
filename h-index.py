def solution(citations):
    citations.sort(reverse=True)
    tmp = 0
    if not max(citations):
        return 0
    else:
        for i in range(0, len(citations)):
            if citations[i] <= i:
                break
            else:
                tmp += 1
    return tmp


citations = [0,0,0,0] # 3,3,5,6,8,25
print(solution(citations))