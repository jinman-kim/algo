def solution(s):
    zero,trans = 0,0
    while True:
        if s == '1':
            break
        zero += s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]
        trans += 1

    return [trans,zero]


s = "1111111"
print(solution(s))