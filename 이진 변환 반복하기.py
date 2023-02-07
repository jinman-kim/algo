def solution(s):
    s = list(map(int,list(s)))
    zero,trans = 0,0
    while True:
        if 0 in s:
            s.remove(0)
            zero += 1
        if 0 not in s:
            s = list(map(int,list(format(len(s),'b'))))
            trans += 1
        if len(s) == 1:
            break
    return [trans,zero]


s = "1111111"
print(solution(s))