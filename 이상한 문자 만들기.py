def solution(s):
    answer = ''
    for word in s.split(' '):
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    return answer[:-1]


s = "Tr5y     Hello World good"
print(solution(s))
