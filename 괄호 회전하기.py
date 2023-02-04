def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        #print('i=',i)
        stack = []
        idx = 0
        for j in range(len(s)):
            stack.append(s[j])
            idx += 1
            #print('전:', stack)
            if idx >= 2:
                if stack[idx-2] + stack[idx-1] == '()' or stack[idx-2] + stack[idx-1] == '{}' or stack[idx-2] + stack[idx-1] == '[]':
                    #print('삭제 = ',stack)
                    del stack[idx-1]
                    del stack[idx-2]
                    idx = len(stack)
            #print('후', stack)

        if not stack:
            answer += 1
        k = s[0]
        del s[0]
        s.append(k)

    return answer
