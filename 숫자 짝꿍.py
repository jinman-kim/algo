from collections import Counter
def solution(X,Y):
    num=[]
    x,y = list(map(int,X)),list(map(int,Y))
    cx,cy = Counter(x),Counter(y)
    #Counter에서 정수 i를 공유하면 둘의 최소 공유횟수만큼 append
    for i in cx:
        if i in cy:
            for _ in range(min(cx.get(i),cy.get(i))):
                num.append(i)
    num.sort(reverse=True)
    #예외 처리 구간
    if not num:
        answer = '-1'
    elif max(num) == 0:
        answer = '0'
    else:
        answer = ''.join(list(map(str,num)))
    return answer

X='1255'
Y='5525'
print(solution(X,Y))

