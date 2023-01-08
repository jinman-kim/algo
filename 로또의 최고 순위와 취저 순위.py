def solution(lottos, win_nums):
    answer = []
    chance = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            answer.append(lotto)
    result = [6 if len(answer)==0 and chance == 0 else 7-len(answer)-chance,7-len(answer) if 7-len(answer)<=6 else 6]
    return result


lottos = [1, 2, 3, 4, 5, 7]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos,win_nums))
