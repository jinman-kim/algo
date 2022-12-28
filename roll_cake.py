def solution(topping):
    from collections import Counter
    elder_roll = Counter(topping)
    younger_roll = set()
    answer = 0
    for i in topping:
        elder_roll[i] -= 1
        younger_roll.add(i)
        if elder_roll[i]==0:
            elder_roll.pop(i)
        if len(elder_roll) == len(younger_roll):
            answer+=1
    return answer


topping = [1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping))
