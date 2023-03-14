def solution(babbling):
    sep = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for i in babbling:
        tmp = i
        for j in sep:
            tmp = tmp.replace(j,' '*len(j),1)
        tmp = tmp.replace(' ','')
        if tmp == '':
            answer += 1
    return answer