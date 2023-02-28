def solution(keymap, targets):
    answer = []
    alpha = dict()
    for key in keymap:
        for i in range(len(key)):
            if key[i] in alpha:
                alpha[key[i]] = min(i+1,(alpha[key[i]]))
            else:
                alpha[key[i]] = i+1
    for target in targets:
        try:
            cnt = 0
            for i in target:
                cnt += alpha[i]
            answer.append(cnt)
        except Exception as e:
            answer.append(-1)
            pass
    return answer

keymap, targets = ["AAAA"],["BBBBB",'BBBB']
print(solution(keymap,targets))