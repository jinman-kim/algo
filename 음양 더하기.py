def solution(absolutes , signs):
    answer = 0
    for abs_num,sign in zip(absolutes,signs):
        if not sign:
            answer -= abs_num
        else:
            answer += abs_num
    return answer


absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes,signs))