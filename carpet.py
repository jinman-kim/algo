def solution(brown,yellow):
    answer,result=[],[]
    for i in range(1,int(yellow**0.5)+1):
        if yellow%i==0:
            answer.append([yellow//i,i])
    for i in answer:
        if i[0]+i[1]+2==brown//2:
            result=[i[0]+2,i[1]+2]
            break
    return result
brown,yellow=24,24
print(solution(brown,yellow))