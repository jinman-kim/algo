def solution(picks, minerals):
    from collections import Counter
    from itertools import permutations
    result = []
    # [다이아,아이언, 스톤] 곡괭이 수
    #  최소 피로도
    # 다이아 : 다이아:1 , 철:1 돌:1
    # 철 : 다이아:5 철:1 돌:1
    # 돌 : 다이아:25 철:5 돌:1
    mine = Counter(minerals)
    picket = []
    for i in range(3):
        if i == 0:
            picket.extend(['diamond' for _ in range(picks[i])])
        if i == 1:
            picket.extend(['iron' for _ in range(picks[i])])
        if i == 2:
            picket.extend(['stone' for _ in range(picks[i])])
    for i in list(set(permutations(picket, len(picket)))):
        answer = 0
        mineral = minerals[:]
        for j in i:
            if j == 'diamond':
                for _ in range(5):
                    try:
                        mineral.pop(0)
                        answer += 1
                    except:
                        pass
            if j == 'iron':
                for _ in range(5):
                    try:
                        if mineral[0] == 'diamond':
                            mineral.pop(0)
                            answer += 5
                        else:
                            mineral.pop(0)
                            answer += 1
                    except:
                        pass
            if j == 'stone':
                for _ in range(5):
                    try:
                        if mineral[0] == 'diamond':
                            mineral.pop(0)
                            answer += 25
                        if mineral[0] == 'iron':
                            mineral.pop(0)
                            answer += 5
                        else:
                            mineral.pop(0)
                            answer += 1
                    except:
                        pass
            result.append(answer)

    return min(result)