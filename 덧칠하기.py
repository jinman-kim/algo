def solution(n, m, section):
    answer = 0
    while section:
        tmp = section[0]
        for i in range(m):
            if tmp + i == section[0]:
                section.pop(0)
            if len(section) == 0:
                break
        answer += 1
    return answer

# n	m	section	result
# 8	4	[2, 3, 6]