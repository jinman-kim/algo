def solution(babblings):
    answer = 0
    nephews = ['aya','ye','woo','ma']
    for babbling in babblings:
        for nephew in nephews:
            if nephew*2 not in babbling: #핵심
                babbling = babbling.replace(nephew,' ')
        if babbling.strip() =='':
            answer+=1
    return answer
#연속된것이 한번이라도 나오면 False
babblings = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babblings))