def solution(left, right):
    answer = 0
    for i in range(left,right+1,1):
        cnt = 0 #1포함 ㅎ
        for j in range(1,1+i//2):
            if i%j == 0:
                cnt+=1
        if cnt%2 == 1:
            answer += i
        elif cnt%2 == 0:
            answer -= i
    if right == 1:
        answer = -1

    return answer


left,right = 2,3
print(solution(left,right))