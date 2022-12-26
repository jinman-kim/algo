def solution(elements):
    answer=[]
    elements+=elements
    for i in range(1,len(elements)//2+1): #1,2,3,4,5
        for j in range(1,len(elements)//2+1):
            answer.append(sum(elements[i:i+j]))
    answer=list(set(answer))
    return len(answer)
elements=[1,1,4,7,9]
print(solution(elements))