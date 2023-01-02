def solution(n, l, r):
    answer = r-l+1
    for num in range(l-1,r):
        while num>=1:
            a,b=divmod(num,5)
            if b==2 or a==2:
                answer-=1
                break
            num=a

    return answer
# 0번째 : 1
# 1번째 : 11011
# 2번째 : 11011 11011 00000 11011 11011  ,  16 , 25 , 4/25  17/25 16-2-4
# 3번쨰 : 11011 11011 00000 11011 11011 11011 11011 00000 11011 11011 00000 00000 00000 00000 00000
# rule : (4/5) ^ n
print(solution(3,63,64))
