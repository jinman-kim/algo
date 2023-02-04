def solution(s, n):
    answer = ''
    for i in s:
        print(ord(i)+n)
    return answer


s = 'abc'
n=3
print(solution(s,n))